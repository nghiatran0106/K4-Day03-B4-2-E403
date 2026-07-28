"""
🛠️ TOOL REGISTRY & SCHEMAS
Nơi khai báo tất cả các "món đồ nghề" mà ReAct Agent Tư Vấn Khóa Học có thể gọi.

Agent này tư vấn cho học sinh/thí sinh DỰA TRÊN ĐIỂM SỐ họ cung cấp trực tiếp
(không dựa trên tài khoản/mã sinh viên đã đăng ký trong hệ thống).
"""

from functools import wraps

# ==========================================
# 📚 DỮ LIỆU TUYỂN SINH (Dành cho Agent Gợi Ý Khóa Học)
# ==========================================

SUBJECTS = [
    {"subject_id": "TOAN", "name": "Toán Học", "field": "Khoa học máy tính"},
    {"subject_id": "LY", "name": "Vật Lý", "field": "Khoa học máy tính"},
    {"subject_id": "TIN", "name": "Tin Học", "field": "Khoa học máy tính"},
    {"subject_id": "HOA", "name": "Hóa Học", "field": "Khoa học máy tính"},
    {"subject_id": "ANH", "name": "Tiếng Anh", "field": "Kinh tế"},
    {"subject_id": "VAN", "name": "Ngữ Văn", "field": "Kinh tế"},
    {"subject_id": "GDCD", "name": "Giáo Dục Công Dân", "field": "Kinh tế"},
    {"subject_id": "SU", "name": "Lịch Sử", "field": "Sư phạm"},
    {"subject_id": "DIA", "name": "Địa Lý", "field": "Sư phạm"},
    {"subject_id": "SINH", "name": "Sinh Học", "field": "Sư phạm"},
]

COURSES = [
    {
        "course_id": "MJ_CS01",
        "name": "Khoa học Máy tính",
        "field": "Khoa học máy tính",
        "required_subjects": ["TOAN", "LY", "TIN"],
    },
    {
        "course_id": "MJ_CS02",
        "name": "Kỹ thuật Phần mềm",
        "field": "Khoa học máy tính",
        "required_subjects": ["TOAN", "LY", "HOA"],
    },
    {
        "course_id": "MJ_KT01",
        "name": "Kinh Tế Học",
        "field": "Kinh tế",
        "required_subjects": ["TOAN", "ANH", "VAN"],
    },
    {
        "course_id": "MJ_KT02",
        "name": "Quản Trị Kinh Doanh",
        "field": "Kinh tế",
        "required_subjects": ["TOAN", "ANH", "GDCD"],
    },
    {
        "course_id": "MJ_SP01",
        "name": "Sư Phạm Toán",
        "field": "Sư phạm",
        "required_subjects": ["TOAN", "LY", "SINH"],
    },
    {
        "course_id": "MJ_SP02",
        "name": "Sư Phạm Ngữ Văn",
        "field": "Sư phạm",
        "required_subjects": ["VAN", "SU", "DIA"],
    },
]

ADMISSION_2026 = {
    "MJ_CS01": {"year": 2026, "thresholds": {"TOAN": 8.5, "LY": 8.0, "TIN": 8.0}, "total_threshold": 24.5},
    "MJ_CS02": {"year": 2026, "thresholds": {"TOAN": 8.0, "LY": 7.5, "HOA": 7.5}, "total_threshold": 23.0},
    "MJ_KT01": {"year": 2026, "thresholds": {"TOAN": 7.5, "ANH": 8.0, "VAN": 7.0}, "total_threshold": 22.5},
    "MJ_KT02": {"year": 2026, "thresholds": {"TOAN": 7.0, "ANH": 7.5, "GDCD": 7.0}, "total_threshold": 21.5},
    "MJ_SP01": {"year": 2026, "thresholds": {"TOAN": 8.0, "LY": 7.0, "SINH": 6.5}, "total_threshold": 21.5},
    "MJ_SP02": {"year": 2026, "thresholds": {"VAN": 8.0, "SU": 7.0, "DIA": 7.0}, "total_threshold": 22.0},
}

# Các tool hiện có:
# - get_subjects_list: Lấy danh sách môn học thuộc các khối ngành CS/Kinh tế/Sư phạm.
# - get_courses_list: Lấy danh sách khóa học, mỗi khóa học có 3 môn học yêu cầu.
# - get_admission_info: Lấy mốc điểm tuyển sinh 2026 của một khóa học.
# - search_courses_by_keyword: Tìm kiếm khóa học theo từ khóa (tên/khối ngành).
# - check_eligibility_by_scores: Kiểm tra điểm số thí sinh có đạt mốc tuyển sinh của một khóa học hay không.
# - count_tools_used: Đếm số lần tool được gọi trong bộ nhớ của Agent.
#
# Lưu ý: Việc GỢI Ý ngành/khóa học phù hợp là suy luận của LLM (dựa trên get_courses_list,
# get_admission_info, check_eligibility_by_scores), KHÔNG có tool "recommend" trả kết quả cứng.


def _tool_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            return f"LỖI: {func.__name__} - {str(exc)}"
    return wrapper


@_tool_error_handler
def get_subjects_list() -> list:
    """
    Lấy danh sách môn học thuộc các khối ngành (Khoa học máy tính, Kinh tế, Sư phạm).

    Returns:
        list: Danh sách dict {subject_id, name, field}
    """
    return SUBJECTS


@_tool_error_handler
def get_courses_list() -> list:
    """
    Lấy danh sách khóa học (ngành đào tạo), mỗi khóa học có 3 môn học yêu cầu (required_subjects).

    Returns:
        list: Danh sách dict {course_id, name, field, required_subjects}
    """
    return COURSES


@_tool_error_handler
def get_admission_info(course_id: str, year: int = 2026) -> dict:
    """
    Lấy thông tin tuyển sinh của một khóa học, gồm mốc điểm (điểm chuẩn) từng môn yêu cầu và tổng điểm chuẩn.

    Args:
        course_id (str): Mã khóa học (Ví dụ: 'MJ_CS01')
        year (int): Năm tuyển sinh, hiện chỉ có dữ liệu năm 2026

    Returns:
        dict: Thông tin tuyển sinh {year, thresholds, total_threshold}, hoặc {"error": "..."} nếu không có dữ liệu
    """
    info = ADMISSION_2026.get(course_id)
    if info is None:
        return {"error": f"Không tìm thấy thông tin tuyển sinh cho khóa học '{course_id}'."}
    if info["year"] != year:
        return {"error": f"Không có dữ liệu tuyển sinh năm {year} cho khóa học '{course_id}'."}
    return info


@_tool_error_handler
def search_courses_by_keyword(keyword: str) -> list:
    """
    Tìm kiếm khóa học theo từ khóa (tên khóa học hoặc khối ngành).

    Args:
        keyword (str): Từ khóa tìm kiếm (Ví dụ: 'Máy tính', 'Kinh tế', 'Sư phạm')

    Returns:
        list: Danh sách khóa học phù hợp (dict {course_id, name, field, required_subjects})
    """
    keyword_lower = keyword.lower()
    return [
        course for course in COURSES
        if keyword_lower in course["name"].lower() or keyword_lower in course["field"].lower()
    ]


def _is_error_result(result):
    return isinstance(result, dict) and "error" in result


@_tool_error_handler
def check_eligibility_by_scores(scores: dict, course_id: str, year: int = 2026) -> dict:
    """
    Kiểm tra điểm số của thí sinh có đạt mốc điểm tuyển sinh của một khóa học hay không.

    Args:
        scores (dict): Điểm số thí sinh, dạng {subject_id: điểm} (Ví dụ: {"TOAN": 8.5, "LY": 8.0, "TIN": 7.5})
        course_id (str): Mã khóa học cần kiểm tra
        year (int): Năm tuyển sinh, hiện chỉ có dữ liệu năm 2026

    Returns:
        dict: {"eligible": bool, "missing_subjects": list điểm chưa đạt} hoặc {"error": "..."} nếu không có dữ liệu
    """
    admission = get_admission_info(course_id, year)
    if _is_error_result(admission):
        return admission

    missing_subjects = [
        subject_id for subject_id, threshold in admission["thresholds"].items()
        if scores.get(subject_id, 0) < threshold
    ]

    return {"eligible": len(missing_subjects) == 0, "missing_subjects": missing_subjects}


@_tool_error_handler
def count_tools_used(memory: list) -> int:
    """
    Đếm số lần các tool đã được gọi trong bộ nhớ của Agent.

    Args:
        memory (list): Danh sách các bước đã thực hiện và lưu trữ trong bộ nhớ

    Returns:
        int: Số lần tool được gọi
    """
    return sum(1 for entry in memory if "action" in entry and entry["action"].startswith("Call Tool"))


AVAILABLE_TOOLS = {
    "get_subjects_list": get_subjects_list,
    "get_courses_list": get_courses_list,
    "get_admission_info": get_admission_info,
    "search_courses_by_keyword": search_courses_by_keyword,
    "check_eligibility_by_scores": check_eligibility_by_scores,
    "count_tools_used": count_tools_used,
}
