# 📊 BÁO CÁO GIÁM SÁT & ĐÁNH GIÁ (OBSERVABILITY TRACE LOGS)
*Dành cho Role 5: Observability & Reviewer*

---

## 🎯 1. BẢNG CHẤM ĐIỂM AGENTIC FIT (SCORING MATRIX)

| Tiêu chí | Điểm (1-5) | Lý do đánh giá |
| :--- | :---: | :--- |
| 🧠 **Multi-step Reasoning** | `3/5` | Cần phân tích hồ sơ và gợi ý sơ bộ, nhưng các bước reasoning không quá phức tạp và vẫn khá tuyến tính. |
| 🛠️ **Tool Interaction** | `3/5` | Cần tra cứu thông tin ngành học và yêu cầu, nhưng mức độ use tool vẫn ở dạng lookup/so sánh đơn giản. |
| 🔀 **Dynamic Decision** | `4/5` | Câu trả lời thay đổi theo hồ sơ sinh viên, sở thích và mục tiêu nghề nghiệp. |
| ⏳ **Long Horizon** | `4/5` | Quy trình gồm phân tích hồ sơ, gợi ý lựa chọn và đưa ra kế hoạch học tập. |
| **TỔNG ĐIỂM FIT** | **14/20** | **KẾT LUẬN: DỰ ÁN TƯ VẤN KHOA HỌC SINH VIÊN VẪN PHÙ HỢP VỚI REACT AGENT, NHƯNG KHÔNG PHẢI QUÁ PHỨC TẠP.** |

---

## 🔍 2. SO SÁNH PHẢN HỒI

> ℹ️ **Ghi chú**: Kết quả dưới đây được chạy lại từ `app.py` sau khi `src/prompts.py` được cập nhật (Role 3). `CHATBOT_BASELINE_PROMPT` giữ nguyên nội dung guardrail, nên các phản hồi vẫn phản ánh đúng hành vi hiện tại của Chatbot Baseline. Phần "Nhận xét" tập trung nêu **hạn chế cụ thể** của chatbot ở từng ca — đây là căn cứ để lý giải vì sao cần chuyển sang kiến trúc ReAct Agent có tool.

### TEST CASE #1

**Câu hỏi**: *"Sinh viên năm nhất nên chuẩn bị những gì để vào đại học không bị bỡ ngỡ?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Chào bạn, tôi là Trợ lý Tư vấn Khóa học Đại học... Để giúp bạn tự tin và sẵn sàng hơn: (1) Chuẩn bị tâm lý và phương pháp học tập: chuyển từ học thụ động sang tự học chủ động, quản lý thời gian, tinh thần chủ động; (2) Kỹ năng mềm: làm việc nhóm, ngoại ngữ/tin học, tài chính cá nhân; (3) Định hướng nghề nghiệp sớm: khám phá bản thân qua CLB, tìm hiểu mô tả công việc tương lai. Nếu có thắc mắc về lịch học, học phí, điểm số cá nhân hoặc đăng ký môn học, tôi không có quyền truy cập dữ liệu của trường, vui lòng liên hệ Phòng Đào Tạo."*
* **Nhận xét (hạn chế)**: Câu trả lời đúng phạm vi và guardrail hoạt động tốt, nhưng bộc lộ hạn chế cố hữu của chatbot **chỉ dùng LLM**: toàn bộ lời khuyên đến từ kiến thức phổ quát, **không cá nhân hoá theo hồ sơ/ngành học thực tế của sinh viên** và không thể trỏ tới tài nguyên cụ thể của trường (ví dụ: CLB nào đang tuyển, khóa định hướng nhập học nào sắp diễn ra). Đây là dạng câu hỏi chatbot xử lý tốt nhất vì không cần dữ liệu thực.

---

### TEST CASE #2

**Câu hỏi**: *"Nêu 3 kỹ năng mềm quan trọng mà sinh viên cần phát triển ở năm đầu đại học."*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Ba kỹ năng mềm quan trọng nhất: (1) Quản lý thời gian — dùng lịch/app để phân bổ thời gian học và nghỉ ngơi; (2) Tự học và chủ động nghiên cứu — đọc giáo trình trước, tư duy phản biện; (3) Giao tiếp và làm việc nhóm — lắng nghe, bày tỏ quan điểm, giải quyết mâu thuẫn. Nếu có câu hỏi về lịch học/học phí/điểm số/đăng ký môn, tôi không có quyền truy cập dữ liệu thực tế, vui lòng liên hệ Phòng Đào Tạo."*
* **Nhận xét (hạn chế)**: Trả lời đúng trọng tâm, khớp `expected_behavior`. Hạn chế: đây là kiến thức "sách giáo khoa" giống nhau cho mọi sinh viên ở mọi ngành — chatbot **không thể ưu tiên hoá theo đặc thù ngành học** (ví dụ sinh viên Kỹ thuật cần kỹ năng khác sinh viên Kinh tế) vì không có tool tra cứu hồ sơ/ngành.

---

### TEST CASE #3

**Câu hỏi**: *"Em có điểm học bạ Toán 8.5, Ngữ văn 7.5, Tiếng Anh 7.0 và thích công nghệ, em nên chọn ngành nào phù hợp?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Với điểm số và sở thích công nghệ, đây là nền tảng tốt. Gợi ý: (1) CNTT/Kỹ thuật phần mềm — Toán 8.5 và Anh 7.0 phù hợp; (2) An toàn thông tin — cần tư duy logic; (3) Khoa học dữ liệu/AI — kết hợp Toán và công nghệ; (4) Hệ thống thông tin quản lý/Thương mại điện tử — kết hợp công nghệ và kinh tế nhờ Văn 7.5. Tôi không có quyền truy cập dữ liệu tuyển sinh thực tế nên không thể kiểm tra điều kiện trúng tuyển cụ thể, tổ hợp môn hay điểm chuẩn — vui lòng liên hệ Phòng Đào Tạo/Tuyển sinh."*
* **Nhận xét (hạn chế)**: Đây là **hạn chế rõ nhất** của Chatbot Baseline: liệt kê tới 4 ngành khác nhau nhưng **không xếp hạng hay so sánh dựa trên yêu cầu đầu vào thực tế** (điểm chuẩn, tổ hợp xét tuyển) — vì không có tool `get_course_prerequisites`/`check_course_eligibility`. Sinh viên nhận được danh sách rộng nhưng thiếu căn cứ để chọn 1 ngành cụ thể, dễ gây phân vân thay vì thu hẹp lựa chọn — đúng là ca "🟡 Multi-step (Cần Tool)" mà baseline không đáp ứng được.

---

### TEST CASE #4

**Câu hỏi**: *"So sánh yêu cầu đầu vào và môn học chính giữa ngành Công nghệ thông tin và Kỹ thuật phần mềm."*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Yêu cầu đầu vào: cả hai xét khối A00/A01/D01, điểm chuẩn KTPM đôi khi nhỉnh hơn CNTT tùy trường; CNTT cần sự bao quát, KTPM cần tỉ mỉ/tư duy hệ thống. Môn học chính: CNTT thiên về Mạng máy tính, An toàn thông tin, Quản trị hệ thống, Điện toán đám mây; KTPM tập trung vòng đời phát triển phần mềm (SDLC): kiến trúc phần mềm, Agile/Scrum, kiểm thử/QA. Không có quyền truy cập mã ngành, chỉ tiêu, học phí, lịch học thực tế của trường."*
* **Nhận xét (hạn chế)**: Chatbot tự tin đưa ra so sánh chi tiết nhưng đây hoàn toàn là **suy luận từ kiến thức nền tổng quát**, không phải dữ liệu chương trình đào tạo thật của trường — có rủi ro **thông tin không khớp thực tế** (ví dụ danh sách môn học, thứ tự học) nếu chương trình của trường khác với "chuẩn chung" mà LLM giả định. Đây chính là lý do cần ReAct Agent với tool `get_course_detail`/`get_course_prerequisites` để đảm bảo dữ liệu so sánh là thật, không phải suy đoán.

---

### TEST CASE #5

**Câu hỏi**: *"Em nên học trước học phần nào giữa lập trình cơ bản và cấu trúc dữ liệu để không bị quá tải?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Phải học Lập trình cơ bản trước rồi mới đến Cấu trúc dữ liệu và Giải thuật. Lập trình cơ bản là nền tảng (biến, vòng lặp, hàm, tư duy logic); Cấu trúc dữ liệu đòi hỏi áp dụng thành thạo kỹ năng lập trình để hiện thực hóa (mảng, danh sách liên kết, ngăn xếp, cây...). Lời khuyên: không vội vàng, thực hành nhiều. Không có quyền truy cập hệ thống để kiểm tra mã môn học cụ thể là điều kiện tiên quyết của trường, vui lòng liên hệ Phòng Đào Tạo."*
* **Nhận xét (hạn chế)**: Logic trình tự đúng theo thông lệ chung, nhưng chatbot **tự nhận hạn chế ngay trong câu trả lời**: không thể xác nhận đây có đúng là điều kiện tiên quyết (prerequisite) chính thức của trường hay không. Nếu chương trình đào tạo thực tế có ràng buộc khác (ví dụ môn nào là bắt buộc song song), chatbot sẽ không phát hiện được vì thiếu tool tra cứu `get_course_prerequisites` theo dữ liệu thật.

---

### TEST CASE #6

**Câu hỏi**: *"Em muốn đăng ký ngành Kiến trúc nhưng điểm năng khiếu vẽ còn yếu, Agent nên tư vấn thế nào?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Vẽ trong Kiến trúc là kỹ năng có thể rèn luyện, không cần năng khiếu bẩm sinh — đòi hỏi tư duy hình khối, tỷ lệ hơn là sự bay bổng. Lời khuyên: tham gia lớp luyện thi cấp tốc, kiên trì. Phương án thay thế (Plan B) nếu vẫn khó khăn: Quản lý/Kỹ thuật Xây dựng, Thiết kế Nội thất, Công nghệ số trong Kiến trúc/Quy hoạch đô thị. Không có quyền truy cập điểm chuẩn, tổ hợp xét tuyển, quy chế thi năng khiếu thực tế — vui lòng liên hệ Phòng Đào Tạo/Tuyển sinh."*
* **Nhận xét (hạn chế)**: Guardrail xử lý đúng tinh thần "không gợi ý thẳng vào ngành". Tuy nhiên hạn chế: lời trấn an "vẽ là kỹ năng có thể rèn luyện, nhiều anh chị khóa trước đạt điểm cao" **không có căn cứ dữ liệu thực** (không biết điểm năng khiếu hiện tại của sinh viên là bao nhiêu, ngưỡng đầu vào thực tế của trường là bao nhiêu) — chatbot đang đưa ra nhận định mang tính động viên chung chung hơn là đánh giá dựa trên hồ sơ cụ thể, dễ tạo kỳ vọng không chính xác nếu khoảng cách năng lực thực tế quá lớn.

---

### TEST CASE #7

**Câu hỏi**: *"Em thích thiết kế thời trang nhưng không muốn học toán, có nên đổi sang ngành khác?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Không nhất thiết phải đổi ngành. Thiết kế Thời trang thuộc khối nghệ thuật/sáng tạo, tập trung mỹ thuật, kỹ thuật cắt may, phần mềm thiết kế. Toán chỉ ở mức cơ bản (tính vải, tỷ lệ, chi phí), không có công thức phức tạp như Kinh tế/Kỹ thuật. Không có quyền truy cập chương trình đào tạo chi tiết/lịch học/học phí/thủ tục đăng ký của trường, vui lòng liên hệ Phòng Đào Tạo."*
* **Nhận xét (hạn chế)**: Câu trả lời hợp lý và tránh cực đoan, nhưng hạn chế: khẳng định "toán chỉ ở mức cơ bản" dựa trên **giả định chương trình đào tạo phổ biến**, không kiểm chứng được khung chương trình thực tế của trường (có thể trường yêu cầu môn Toán ứng dụng/Thống kê thời trang mà chatbot không biết). Việc khẳng định chắc chắn trong khi không có dữ liệu xác thực là rủi ro "hallucination nhẹ" mà một ReAct Agent có thể tránh bằng cách gọi `get_course_detail` để lấy chương trình học thật trước khi kết luận.

---

### TEST CASE #8

**Câu hỏi**: *"Hồ sơ của em có điểm Toán 8.0, Anh 7.0, em nên đăng ký học phần nào trước để chuẩn bị cho ngành Khoa học dữ liệu?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Với nền tảng Toán 8.0 và Anh 7.0, nên ưu tiên: (1) Toán học nền tảng — Giải tích, Đại số tuyến tính, Xác suất thống kê; (2) Lập trình — Nhập môn lập trình/Lập trình cơ bản (Python/R); (3) tiếp tục phát huy Tiếng Anh để đọc tài liệu quốc tế. Không có quyền truy cập hệ thống của trường nên không thể kiểm tra mã học phần cụ thể, điều kiện tiên quyết theo chương trình đào tạo riêng, hay hỗ trợ đăng ký môn — cần tra cứu Khung chương trình đào tạo chính thức hoặc liên hệ Phòng Đào Tạo."*
* **Nhận xét (hạn chế)**: Chatbot đúng khi từ chối thao tác đăng ký/tra cứu mã môn thật (đúng guardrail), nhưng đây chính là **giới hạn cốt lõi khiến baseline không thể hoàn thành trọn vẹn yêu cầu của người dùng**: câu hỏi cần một danh sách học phần *cụ thể, đúng theo hệ thống của trường* để đăng ký, nhưng chatbot chỉ đưa ra được nhóm kiến thức "nên học" ở mức khái niệm — người dùng vẫn phải tự tra cứu thêm. Đây là minh chứng rõ ràng cho việc **baseline dừng lại ở tư vấn định hướng, không thể thực thi tác vụ multi-step (tra cứu → đối chiếu hồ sơ → đề xuất mã môn cụ thể)** mà một ReAct Agent với `search_courses`/`get_course_prerequisites`/`generate_learning_path` mới xử lý được.

---

## 🎯 3. TỔNG KẾT HẠN CHẾ CỦA CHATBOT BASELINE (TIỀN ĐỀ CHỌN REACT AGENT)

Qua 8 test case, các hạn chế lặp lại nhất quán của Chatbot Baseline là:

1. **Không cá nhân hoá theo dữ liệu thật**: Mọi lời khuyên đều dựa trên kiến thức phổ quát/suy luận chung, không tra cứu được hồ sơ, điểm chuẩn, hay chương trình đào tạo thực tế của sinh viên/trường (TC1, TC2, TC3, TC8).
2. **Không thể xếp hạng/thu hẹp lựa chọn dựa trên điều kiện thực**: Khi câu hỏi cần so sánh hoặc chọn 1 trong nhiều phương án, chatbot chỉ liệt kê chung chung thay vì đối chiếu với ngưỡng đầu vào thật (TC3, TC4).
3. **Rủi ro trả lời "chắc như đinh đóng cột" dựa trên giả định**: Chatbot đôi khi khẳng định chắc chắn (VD: "toán chỉ ở mức cơ bản", "vẽ hoàn toàn có thể rèn luyện kịp") mà không có dữ liệu xác thực — tiềm ẩn rủi ro hallucination nhẹ nếu thực tế khác với giả định (TC6, TC7).
4. **Không thể hoàn thành tác vụ multi-step đến cùng**: Với các câu hỏi cần chuỗi hành động (tra cứu → đối chiếu → đề xuất cụ thể → có thể đăng ký), chatbot luôn phải dừng lại ở bước định hướng và đẩy trách nhiệm tra cứu/thực thi ngược lại cho sinh viên (TC3, TC5, TC8).

➡️ Đây chính là cơ sở thực nghiệm (không chỉ lý thuyết ở bảng chấm điểm mục 1) để khẳng định: dự án **Trợ Lý Tư Vấn Khóa Học Sinh Viên** cần một **ReAct Agent có tool tra cứu dữ liệu thật** (`get_student_profile`, `get_course_prerequisites`, `check_course_eligibility`, `recommend_course`, `generate_learning_path`...) thay vì chỉ dùng LLM thuần, đặc biệt với nhóm câu hỏi "🟡 Multi-step" và "🔴 Edge Case".

> ℹ️ **Ghi chú kỹ thuật**: Hàm `run_react_agent()` trong `app.py` hiện tại vẫn là bản demo cứng (hardcoded, minh họa bằng dữ liệu thời tiết) và chưa được nối với `REACT_SYSTEM_PROMPT` cùng bộ tool tư vấn khóa học thực tế trong `tools.py`. Do đó báo cáo này chưa có phần "ReAct Agent thực chạy" — sẽ bổ sung khi Role 2/3/4 hoàn thiện vòng lặp ReAct thực sự gọi LLM + tool.