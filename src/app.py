"""
🚀 CORE AGENT APP (Dành cho Role 4: Core Agent Developer)
File chính ghép nối tất cả các thành phần: Tools + Prompts + Test Cases + Multi-Provider.
"""

import ast
import json
import os
import re
import sys
from dotenv import load_dotenv

# Đảm bảo import các module cùng thư mục src/ hoạt động mượt mà
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Đảm bảo in ra Tiếng Việt và Emojis không bị lỗi trên Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from tools import (
    AVAILABLE_TOOLS,
    get_subjects_list,
    get_courses_list,
    get_admission_info,
    search_courses_by_keyword,
    check_eligibility_by_scores,
    count_tools_used,
)
from prompts import CHATBOT_BASELINE_PROMPT, REACT_SYSTEM_PROMPT, MAX_ITERATIONS
from providers import get_llm_provider

load_dotenv()

def load_test_cases():
    """Đọc bộ test cases từ config/test_cases.json của Role 1"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "test_cases.json")
    
    # Fallback kiểm tra nếu file ở thư mục hiện tại
    if not os.path.exists(config_path):
        config_path = "test_cases.json"
        
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_baseline_chatbot(user_query: str, provider):
    """
    Dựng Chatbot gốc (Baseline) không có công cụ.
    """
    print(f"\n💬 [CHATBOT BASELINE] Câu hỏi: {user_query}")
    print(f"⚙️ System Prompt: {CHATBOT_BASELINE_PROMPT.strip()}")
    
    # Gọi LLM Provider thực hiện sinh câu trả lời
    response = provider.generate(user_query, system_prompt=CHATBOT_BASELINE_PROMPT)
    print(f"🤖 Chatbot trả lời:\n{response}")

# Nhận diện dòng "Action: tên_tool[đối_số]" mà LLM sinh ra (theo định dạng bắt buộc trong REACT_SYSTEM_PROMPT)
_ACTION_PATTERN = re.compile(r"Action:\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\[(.*?)\]", re.DOTALL)
_FINAL_ANSWER_PATTERN = re.compile(r"Final Answer:\s*(.*)", re.DOTALL)


def _parse_action(llm_output: str):
    """
    Trích xuất tên tool và danh sách đối số từ dòng Action mà LLM sinh ra.
    Dùng ast.literal_eval (không phải eval) để parse an toàn các đối số dạng dict/str/số.
    """
    match = _ACTION_PATTERN.search(llm_output)
    if not match:
        return None

    tool_name = match.group(1).strip()
    raw_args = match.group(2).strip()
    if not raw_args:
        return tool_name, []

    try:
        parsed = ast.literal_eval(f"({raw_args},)")
    except (ValueError, SyntaxError):
        # Fallback: LLM có thể quên bọc chuỗi trong dấu nháy -> coi cả chuỗi là 1 đối số string
        parsed = (raw_args.strip("'\""),)

    return tool_name, list(parsed)


def run_react_agent(user_query: str, provider):
    """
    Reactive Agent THỰC THỤ: chính LLM (qua provider) tự suy nghĩ (Thought), tự quyết định
    gọi Tool nào (Action), hệ thống thực thi Tool đó và trả kết quả (Observation) lại cho LLM
    đọc tiếp ở vòng lặp sau — lặp lại tới khi LLM tự kết luận (Final Answer) hoặc chạm Guardrail.
    """
    print(f"\n🤖 [REACT AGENT v2 - LLM tự suy luận] Câu hỏi: {user_query}")

    transcript = f"Câu hỏi của thí sinh: {user_query}\n"
    step = 0

    while step < MAX_ITERATIONS:
        step += 1
        print(f"\n--- 🔄 Vòng lặp ReAct (Step {step}/{MAX_ITERATIONS}) ---")

        # 1) LLM tự suy nghĩ và quyết định bước tiếp theo dựa trên toàn bộ lịch sử hội thoại
        llm_output = provider.generate(transcript, system_prompt=REACT_SYSTEM_PROMPT)
        if not llm_output:
            print("⚠️ Provider không trả về nội dung (None/rỗng) — có thể bị chặn hoặc lỗi API. Dừng vòng lặp an toàn.")
            return None
        print(f"🗣️ LLM sinh ra:\n{llm_output.strip()}")

        action = _parse_action(llm_output)
        final_match = _FINAL_ANSWER_PATTERN.search(llm_output)

        # 2) LLM đã đủ thông tin và kết luận -> dừng vòng lặp
        if final_match and not action:
            final_answer = final_match.group(1).strip()
            print(f"🏁 Final Answer: {final_answer}")
            return final_answer

        # 3) LLM không sinh ra Action hợp lệ và cũng chưa Final Answer -> dừng an toàn, không đoán mò
        if not action:
            print("⚠️ LLM không sinh Action/Final Answer hợp lệ theo định dạng. Dừng vòng lặp an toàn.")
            return llm_output.strip()

        tool_name, args = action
        transcript += llm_output.strip() + "\n"

        # 4) Hệ thống (không phải LLM) thực thi Tool thật để lấy dữ liệu
        tool_func = AVAILABLE_TOOLS.get(tool_name)
        if tool_func is None:
            observation = f"LỖI: Không tìm thấy tool '{tool_name}'."
        else:
            try:
                observation = tool_func(*args)
            except Exception as exc:
                observation = f"LỖI: {tool_name} - {str(exc)}"

        print(f"👁️ Observation: {observation}")

        # 5) Ghi Observation vào lịch sử để LLM đọc và suy nghĩ tiếp ở vòng lặp sau
        transcript += f"Observation: {observation}\n"

    print(f"🛡️ GUARDRAIL TRIGGERED: Đã đạt giới hạn tối đa {MAX_ITERATIONS} bước. Ngắt lặp an toàn!")
    return None


if __name__ == "__main__":
    # print("==================================================")
    # print("🏫 ĐẠI HỌC VINUNI - BÀI LAB 3: CHATBOT VS REACT AGENT")
    # print("==================================================")
    
    # Khởi tạo Multi-Provider LLM Adapter (Đọc từ biến môi trường LLM_PROVIDER)
    provider = get_llm_provider()
    # model_name = getattr(provider, "model_name", "Offline Mock Mode")
    # print(f"🔌 LLM Provider đang hoạt động: {provider.__class__.__name__} (Model: {model_name})")
    
    tests = load_test_cases()
    # print(f"✅ Đã tải thành công {len(tests)} Test Cases từ config/test_cases.json\n")
    
    # # Chạy thử câu test số 3
    sample_query = tests[2]["question"]
    
    # print("--- DEMO 1: CHẠY TRÊN CHATBOT BASELINE ---")
    # run_baseline_chatbot(sample_query, provider)
    
    # print("\n--- DEMO 2: CHẠY TRÊN REACT AGENT (kịch bản dựng sẵn) ---")
    # run_react_agent(sample_query, provider)

    print("\n--- DEMO 3: CHẠY TRÊN REACT AGENT v2 (LLM tự suy luận Thought -> Action -> Observation) ---")
    run_react_agent(sample_query, provider)
