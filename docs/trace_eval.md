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

### TEST CASE #1

**Câu hỏi**: *"Sinh viên năm nhất nên chuẩn bị những gì để vào đại học không bị bỡ ngỡ?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Chào bạn, tôi là Trợ lý Tư vấn Khóa học của trường. Rất vui được hỗ trợ bạn! Bước chân vào môi trường đại học là một bước ngoặt lớn, và việc cảm thấy bỡ ngỡ ban đầu là hoàn toàn bình thường. Để giúp bạn nhanh chóng thích nghi và tự tin hơn, dưới đây là những sự chuẩn bị quan trọng dành cho một tân sinh viên:*
  *1. Chuẩn bị về tâm lý và phong cách học tập: Chủ động tìm kiếm tài liệu, đọc trước giáo trình, tư duy tự học, sẵn sàng đối diện với sự khác biệt.*
  *2. Phát triển các kỹ năng mềm cốt lõi: Quản lý thời gian, kỹ năng số, kỹ năng giao tiếp và thuyết trình.*
  *3. Định hướng nghề nghiệp sớm: Khám phá bản thân, tìm hiểu thị trường lao động, xây dựng mối quan hệ (networking).*
  *Nếu trong quá trình học tập, bạn có các thắc mắc liên quan đến lịch học cụ thể, học phí, điểm số cá nhân hoặc thủ tục đăng ký môn học, rất tiếc tôi không có quyền truy cập vào cơ sở dữ liệu của trường để tra cứu trực tiếp. Bạn vui lòng liên hệ trực tiếp với Phòng Đào Tạo để được hỗ trợ chính xác nhất nhé!"*
* **Nhận xét**: Chatbot trả lời đầy đủ, đúng phạm vi câu hỏi chung (kiến thức phổ quát, không cần dữ liệu thực tế của trường). Đúng như `expected_behavior`, chatbot chủ động từ chối/nhắc nhở khi chạm tới các thông tin cần dữ liệu thực (lịch học, học phí) dù câu hỏi không trực tiếp yêu cầu — cho thấy guardrail trong system prompt hoạt động tốt ngay cả ở câu hỏi đơn giản.

---

### TEST CASE #2

**Câu hỏi**: *"Nêu 3 kỹ năng mềm quan trọng mà sinh viên cần phát triển ở năm đầu đại học."*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Chào bạn! Bước vào năm nhất đại học, môi trường học tập thay đổi rất nhiều so với phổ thông. Dưới đây là 3 kỹ năng mềm quan trọng nhất:*
  *1. Kỹ năng quản lý thời gian (Time Management): Sử dụng lịch biểu, phân chia thời gian giữa học, làm thêm, câu lạc bộ và nghỉ ngơi.*
  *2. Kỹ năng thích nghi và tự học (Adaptability & Self-directed Learning): Chủ động tìm tài liệu, đặt câu hỏi, cởi mở với góc nhìn đa dạng.*
  *3. Kỹ năng giao tiếp và làm việc nhóm (Communication & Teamwork): Tích cực thảo luận, lắng nghe tích cực, thể hiện quan điểm xây dựng."*
* **Nhận xét**: Chatbot trả lời trực tiếp, đúng trọng tâm câu hỏi (3 kỹ năng: quản lý thời gian, tự học, giao tiếp/làm việc nhóm) — khớp với `expected_behavior`. Không có yêu cầu tra cứu dữ liệu nội bộ nên không kích hoạt guardrail, phù hợp với phân loại "🟢 Đơn giản (Chỉ cần LLM)".

---

### TEST CASE #3

**Câu hỏi**: *"Em có điểm học bạ Toán 8.5, Ngữ văn 7.5, Sinh 8.0 và thích công nghệ, em nên chọn chuyên ngành nào phù hợp?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Với điểm số này và sở thích công nghệ, em có thể cân nhắc các ngành như Công nghệ thông tin, Khoa học máy tính hoặc Khoa học dữ liệu. Hãy lựa chọn ngành có cả nội dung lập trình và ứng dụng công nghệ."*
* **Nhận xét**: Chatbot trả lời chung chung, không kiểm tra yêu cầu cụ thể của từng ngành và không lấy dữ liệu thực tế về điểm chuẩn, nên dễ thiếu chính xác.

<!-- #### 🧠 ReAct Agent (dự kiến):
* **Thought 1**: Cần tra cứu yêu cầu điểm và môn chính của ngành Công nghệ thông tin và Khoa học dữ liệu.
* **Action 1**: `get_course_prerequisites('Công nghệ thông tin')`
* **Observation 1**: `Yêu cầu: Toán 8.0, Anh 7.0, ưu tiên học sinh có nền tảng lập trình.`
* **Thought 2**: Kiểm tra nếu hồ sơ phù hợp với ngành này và so sánh với ngành Khoa học dữ liệu.
* **Action 2**: `get_course_prerequisites('Khoa học dữ liệu')`
* **Observation 2**: `Yêu cầu: Toán 8.5, Tiếng Anh 7.0, kỹ năng phân tích số liệu được ưu tiên.`
* **Final Answer**: *"Với điểm Toán 8.5 và niềm đam mê công nghệ, em phù hợp với cả Công nghệ thông tin và Khoa học dữ liệu. Nếu em thích lập trình và ứng dụng phần mềm, chọn Công nghệ thông tin. Nếu em quan tâm phân tích dữ liệu và thống kê, chọn Khoa học dữ liệu."*
* **Nhận xét**: Agent sẽ tận dụng tool lookup để đưa ra khuyến nghị sát thực tế hơn và giảm rủi ro trả lời bằng trực giác. -->

---

### TEST CASE #4

**Câu hỏi**: *"So sánh yêu cầu đầu vào và môn học chính giữa ngành Công nghệ thông tin và Kỹ thuật phần mềm."*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Chào bạn, tôi là Trợ lý Tư vấn Khóa học của trường... Liên quan đến câu hỏi so sánh giữa Công nghệ thông tin (CNTT) và Kỹ thuật phần mềm (KTPM): (1) Yêu cầu đầu vào: cả hai thường xét tuyển khối A00/A01/D01, CNTT phù hợp với tư duy logic và yêu thích công nghệ nói chung, KTPM đòi hỏi tỉ mỉ và tư duy hệ thống hơn. (2) Môn học chính: CNTT mang tính bao quát (Cấu trúc dữ liệu, Mạng máy tính, Hệ điều hành, Cơ sở dữ liệu...), còn KTPM tập trung sâu vào vòng đời phát triển phần mềm (Phân tích thiết kế hệ thống, Kiểm thử, Kiến trúc phần mềm, Agile/Scrum...). Nếu cần điểm chuẩn/chỉ tiêu/khung chương trình chính xác của trường, tôi không có quyền truy cập dữ liệu nội bộ, vui lòng liên hệ Phòng Đào Tạo."*
* **Nhận xét**: Chatbot đưa ra được sự khác biệt tổng quát khá hợp lý dựa trên kiến thức chung (broad-base vs. deep-dive), nhưng đây là thông tin mang tính phổ quát của ngành học nói chung, không phải dữ liệu thực tế của trường — đúng như dự đoán ở `expected_behavior`, một ReAct Agent có tool `get_course_prerequisites`/`get_course_detail` sẽ so sánh chính xác theo dữ liệu thật thay vì kiến thức nền chung chung.

---

### TEST CASE #5

**Câu hỏi**: *"Em nên học trước học phần nào giữa lập trình cơ bản và cấu trúc dữ liệu để không bị quá tải?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Em phải học Lập trình cơ bản trước. Lập trình cơ bản là nền móng đầu tiên (tư duy logic, cú pháp, biến, vòng lặp, hàm...). Cấu trúc dữ liệu là bước nâng cao hơn, đòi hỏi đã thành thạo lập trình để hiện thực hóa các cấu trúc (mảng, danh sách liên kết, ngăn xếp, hàng đợi, cây...). Lời khuyên: vững căn bản trước, thực hành liên tục. Nếu cần tra lịch trình cụ thể/điểm số/đăng ký môn, tôi không có quyền truy cập dữ liệu thực tế, vui lòng liên hệ Phòng Đào Tạo."*
* **Nhận xét**: Chatbot trả lời đúng về mặt logic trình tự học (lập trình cơ bản → cấu trúc dữ liệu), phù hợp với `expected_behavior` dù không tra cứu được quan hệ tiên quyết thực tế (`get_course_prerequisites`) từ hệ thống của trường — câu trả lời dựa trên suy luận chung, không phải dữ liệu chương trình đào tạo cụ thể.

---

### TEST CASE #6

**Câu hỏi**: *"Em muốn đăng ký ngành Kiến trúc nhưng điểm năng khiếu vẽ còn yếu, Agent nên tư vấn thế nào?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Vẽ năng khiếu đầu vào chủ yếu đánh giá khả năng quan sát, tỷ lệ, hình khối, tư duy không gian — có thể rèn luyện được. Lộ trình cải thiện: tham gia lớp luyện thi, xây dựng nền tảng từ khối hình học cơ bản, tận dụng phần mềm hỗ trợ (AutoCAD, Revit, SketchUp...). Phương án dự phòng nếu vẫn khó khăn: Quản lý/Kỹ thuật Xây dựng, Thiết kế Đô thị/Quy hoạch, Thiết kế nội thất/Đồ họa. Không cung cấp được điều kiện xét tuyển/chỉ tiêu cụ thể của trường vì không có quyền truy cập dữ liệu nội bộ."*
* **Nhận xét**: Đúng như `expected_behavior` — chatbot **không gợi ý thẳng vào ngành** mà phân tích hạn chế năng khiếu, đề xuất lộ trình cải thiện, đồng thời đưa thêm các ngành thay thế có yêu cầu tương tự nhưng phù hợp hơn. Guardrail hoạt động tốt: không hứa hẹn hay tự bịa khả năng trúng tuyển.

---

### TEST CASE #7

**Câu hỏi**: *"Em thích thiết kế thời trang nhưng không muốn học toán, có nên đổi sang ngành khác?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Ngành Thiết kế Thời trang không đòi hỏi giải toán phức tạp, chỉ toán cơ bản (hình học, đo lường, tỉ lệ) khi dựng rập, tính vải, ngân sách. Trọng tâm ngành là sáng tạo, thẩm mỹ, kỹ thuật vẽ phác thảo và may vá. Nếu vẫn thích thời trang, hoàn toàn có thể theo đuổi vì lượng toán rất ít. Nếu muốn né toán hoàn toàn, có thể tham khảo Ngôn ngữ học, Báo chí, Truyền thông đa phương tiện, Văn học, Quản trị sự kiện — nhưng lưu ý ngành nào cũng có thể có ít môn mang tính số liệu. Lời khuyên: đừng vì sợ toán mà từ bỏ đam mê nếu thực sự có năng khiếu."*
* **Nhận xét**: Đúng như `expected_behavior` — chatbot cân nhắc cả sở thích lẫn yêu cầu ngành, không vội đưa ra quyết định thay sinh viên mà làm rõ hiểu lầm (toán trong ngành này không nặng), đồng thời gợi ý lựa chọn thay thế nếu sinh viên vẫn kiên quyết né toán. Cách xử lý cân bằng, không cực đoan.

---

### TEST CASE #8

**Câu hỏi**: *"Hồ sơ của em có điểm Toán 8.0, Anh 7.0, em nên đăng ký học phần nào trước để chuẩn bị cho ngành Khoa học dữ liệu?"*

#### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Không có quyền truy cập vào cơ sở dữ liệu cá nhân, hệ thống đăng ký môn học hay danh mục học phần cụ thể của trường nên không thể tra cứu chính xác mã môn/thời khóa biểu. Dựa trên khung chương trình chuẩn chung của ngành Khoa học Dữ liệu, nên ưu tiên: (1) Toán cho Khoa học Dữ liệu (Giải tích, Đại số tuyến tính, Xác suất - Thống kê), (2) Lập trình cơ bản (Python/R), (3) Tiếng Anh chuyên ngành. Khuyên liên hệ Phòng Đào Tạo/Cố vấn học tập để có danh sách học phần chính xác."*
* **Nhận xét**: Chatbot xử lý đúng guardrail — từ chối tra cứu/đăng ký học phần cụ thể (vì đây là yêu cầu cần dữ liệu thực + đăng ký môn học), nhưng vẫn hữu ích khi đưa ra định hướng nhóm kiến thức nền tảng chung. Đúng như `expected_behavior` về mặt định hướng, tuy chưa thể tra cứu học phần nền tảng chính xác (toán rời rạc, lập trình Python...) như một ReAct Agent có tool `search_courses`/`get_course_prerequisites` sẽ làm được.

---

<!-- #### 🧠 ReAct Agent (dự kiến):
* **Thought 1**: Cần tra cứu yêu cầu điểm và môn chính của ngành Công nghệ thông tin và Khoa học dữ liệu.
* **Action 1**: `get_course_prerequisites('Công nghệ thông tin')`
* **Observation 1**: `Yêu cầu: Toán 8.0, Anh 7.0, ưu tiên học sinh có nền tảng lập trình.`
* **Thought 2**: Kiểm tra nếu hồ sơ phù hợp với ngành này và so sánh với ngành Khoa học dữ liệu.
* **Action 2**: `get_course_prerequisites('Khoa học dữ liệu')`
* **Observation 2**: `Yêu cầu: Toán 8.5, Tiếng Anh 7.0, kỹ năng phân tích số liệu được ưu tiên.`
* **Final Answer**: *"Với điểm Toán 8.5 và niềm đam mê công nghệ, em phù hợp với cả Công nghệ thông tin và Khoa học dữ liệu. Nếu em thích lập trình và ứng dụng phần mềm, chọn Công nghệ thông tin. Nếu em quan tâm phân tích dữ liệu và thống kê, chọn Khoa học dữ liệu."*
* **Nhận xét**: Agent sẽ tận dụng tool lookup để đưa ra khuyến nghị sát thực tế hơn và giảm rủi ro trả lời bằng trực giác. -->
