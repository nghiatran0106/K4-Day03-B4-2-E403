# """
# 🛠️ TOOL REGISTRY & SCHEMAS (Dành cho Role 2: Tool & Spec Engineer)
# Nơi khai báo tất cả các "món đồ nghề" mà ReAct Agent có thể gọi.
# """

# def get_weather(location: str) -> str:
#     """
#     Tra cứu thời tiết hiện tại của một thành phố.
    
#     Args:
#         location (str): Tên thành phố (Ví dụ: 'Hà Nội', 'TP.HCM', 'Đà Nẵng')
        
#     Returns:
#         str: Thông tin thời tiết chi tiết
#     """
#     loc_lower = location.lower()
#     if "hà nội" in loc_lower or "ha noi" in loc_lower:
#         return "Thời tiết Hà Nội: 28°C, Nắng nhẹ, Độ ẩm 65%."
#     elif "hồ chí minh" in loc_lower or "tp.hcm" in loc_lower or "hcm" in loc_lower:
#         return "Thời tiết TP.HCM: 33°C, Nắng nóng, Có mây."
#     elif "đà nẵng" in loc_lower or "da nang" in loc_lower:
#         return "Thời tiết Đà Nẵng: 30°C, Gió nhẹ, Mát mẻ."
#     else:
#         return f"LỖI: Không tìm thấy dữ liệu thời tiết cho địa điểm '{location}'."


# def search_flights(origin: str, destination: str) -> str:
#     """
#     Tra cứu chuyến bay giữa hai địa điểm.
    
#     Args:
#         origin (str): Nơi đi (Ví dụ: 'TP.HCM')
#         destination (str): Nơi đến (Ví dụ: 'Hà Nội')
        
#     Returns:
#         str: Danh sách chuyến bay khả dụng và giá vé
#     """
#     return (
#         f"Chuyến bay từ {origin} -> {destination} ngày mai:\n"
#         f"1. VN123 (08:00) - Giá: 1,500,000 VNĐ (Còn vé)\n"
#         f"2. VJ456 (14:30) - Giá: 1,200,000 VNĐ (Còn vé)"
#     )


# # Danh sách các tool được đăng ký để Agent sử dụng
# AVAILABLE_TOOLS = {
#     "get_weather": get_weather,
#     "search_flights": search_flights,
# }

# Các tool hiện có:
# - get_student_profile: Lấy hồ sơ sinh viên, bao gồm thông tin cá nhân và học tập.
# - check_actived_skills: Kiểm tra kỹ năng đang được kích hoạt hoặc khả dụng cho sinh viên.
# - get_course_prerequisites: Lấy điều kiện tiên quyết của một khóa học cụ thể.
# - recommend_course: Đề xuất khóa học phù hợp dựa trên hồ sơ và mục tiêu học tập.
# - search_courses: Tìm kiếm khóa học theo từ khóa hoặc bộ lọc.
# - get_course_detail: Lấy chi tiết về một khóa học, ví dụ nội dung, giảng viên, lịch học.
# - check_course_eligibility: Kiểm tra sinh viên có đủ điều kiện đăng ký khóa học hay không.
# - generate_learning_path: Sinh lộ trình học tập cá nhân hóa cho sinh viên.
# - find_schedule: Tìm thời khóa biểu hoặc lịch học phù hợp.
# - register_course: Đăng ký khóa học cho sinh viên.
def get_student_profile(student_id: str) -> dict:
    """
    Lấy hồ sơ sinh viên dựa trên ID sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        dict: Thông tin hồ sơ sinh viên
    """
    # Giả lập dữ liệu hồ sơ sinh viên
    profiles = {
        "SV001": {"name": "Nguyễn Văn A", "major": "Công nghệ thông tin", "year": 2},
        "SV002": {"name": "Trần Thị B", "major": "Kinh tế", "year": 3},
        "SV003": {"name": "Lê Văn C", "major": "Điện tử viễn thông", "year": 1},
    }
    return profiles.get(student_id, {"error": f"Không tìm thấy hồ sơ cho ID '{student_id}'."})

def check_actived_skills(student_id: str) -> list:
    """
    Kiểm tra các kỹ năng đang được kích hoạt cho sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        list: Danh sách kỹ năng đang được kích hoạt
    """
    # Giả lập dữ liệu kỹ năng
    skills = {
        "SV001": ["Python", "Machine Learning", "Data Analysis"],
        "SV002": ["Marketing", "Sales", "Business Strategy"],
        "SV003": ["Circuit Design", "Embedded Systems"],
    }
    return skills.get(student_id, [])

def get_course_prerequisites(course_id: str) -> list:
    """
    Lấy điều kiện tiên quyết của một khóa học cụ thể.
    
    Args:
        course_id (str): Mã khóa học
        
    Returns:
        list: Danh sách các khóa học tiên quyết
    """
    # Giả lập dữ liệu điều kiện tiên quyết
    prerequisites = {
        "CS101": [],
        "CS201": ["CS101"],
        "CS301": ["CS201"],
        "ECON101": [],
        "ECON201": ["ECON101"],
    }
    return prerequisites.get(course_id, [])

def recommend_course(student_id: str) -> list:
    """
    Đề xuất khóa học phù hợp dựa trên hồ sơ và mục tiêu học tập của sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        list: Danh sách khóa học được đề xuất
    """
    # Giả lập dữ liệu đề xuất khóa học
    recommendations = {
        "SV001": ["CS201", "CS301"],
        "SV002": ["ECON201", "ECON301"],
        "SV003": ["EE201", "EE301"],
    }
    return recommendations.get(student_id, [])

def search_courses(keyword: str) -> list:
    """
    Tìm kiếm khóa học theo từ khóa.
    
    Args:
        keyword (str): Từ khóa tìm kiếm
        
    Returns:
        list: Danh sách khóa học phù hợp
    """
    # Giả lập dữ liệu khóa học
    courses = {
        "CS101": "Introduction to Computer Science",
        "CS201": "Data Structures and Algorithms",
        "CS301": "Machine Learning",
        "ECON101": "Principles of Economics",
        "ECON201": "Microeconomics",
    }
    return [course_id for course_id, title in courses.items() if keyword.lower() in title.lower()]

def get_course_detail(course_id: str) -> dict:
    """
    Lấy chi tiết về một khóa học cụ thể.
    
    Args:
        course_id (str): Mã khóa học
        
    Returns:
        dict: Thông tin chi tiết về khóa học
    """
    # Giả lập dữ liệu chi tiết khóa học
    course_details = {
        "CS101": {"title": "Introduction to Computer Science", "instructor": "Dr. A", "schedule": "Mon/Wed 10:00-11:30"},
        "CS201": {"title": "Data Structures and Algorithms", "instructor": "Dr. B", "schedule": "Tue/Thu 14:00-15:30"},
        "CS301": {"title": "Machine Learning", "instructor": "Dr. C", "schedule": "Mon/Wed 16:00-17:30"},
        "ECON101": {"title": "Principles of Economics", "instructor": "Dr. D", "schedule": "Tue/Thu 10:00-11:30"},
        "ECON201": {"title": "Microeconomics", "instructor": "Dr. E", "schedule": "Mon/Wed 14:00-15:30"},
    }
    return course_details.get(course_id, {"error": f"Không tìm thấy chi tiết cho khóa học '{course_id}'."})

def check_course_eligibility(student_id: str, course_id: str) -> bool:
    """
    Kiểm tra sinh viên có đủ điều kiện đăng ký khóa học hay không.
    
    Args:
        student_id (str): Mã số sinh viên
        course_id (str): Mã khóa học
        
    Returns:
        bool: True nếu đủ điều kiện, False nếu không
    """
    prerequisites = get_course_prerequisites(course_id)
    student_courses = recommend_course(student_id)  # Giả lập danh sách khóa học đã hoàn thành
    return all(prereq in student_courses for prereq in prerequisites)

def generate_learning_path(student_id: str) -> list:
    """
    Sinh lộ trình học tập cá nhân hóa cho sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        list: Danh sách khóa học trong lộ trình học tập
    """
    # Giả lập dữ liệu lộ trình học tập
    learning_paths = {
        "SV001": ["CS101", "CS201", "CS301"],
        "SV002": ["ECON101", "ECON201", "ECON301"],
        "SV003": ["EE101", "EE201", "EE301"],
    }
    return learning_paths.get(student_id, [])

def find_schedule(student_id: str) -> dict:
    """
    Tìm thời khóa biểu hoặc lịch học phù hợp cho sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        dict: Thời khóa biểu của sinh viên
    """
    # Giả lập dữ liệu thời khóa biểu
    schedules = {
        "SV001": {"Mon": ["CS101 10:00-11:30"], "Wed": ["CS201 14:00-15:30"]},
        "SV002": {"Tue": ["ECON101 10:00-11:30"], "Thu": ["ECON201 14:00-15:30"]},
        "SV003": {"Mon": ["EE101 10:00-11:30"], "Wed": ["EE201 14:00-15:30"]},
    }
    return schedules.get(student_id, {"error": f"Không tìm thấy thời khóa biểu cho ID '{student_id}'."})

def register_course(student_id: str, course_id: str) -> str:
    """
    Đăng ký khóa học cho sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        course_id (str): Mã khóa học
        
    Returns:
        str: Thông báo kết quả đăng ký
    """
    if check_course_eligibility(student_id, course_id):
        return f"Đăng ký thành công khóa học '{course_id}' cho sinh viên '{student_id}'."
    else:
        return f"Không đủ điều kiện đăng ký khóa học '{course_id}' cho sinh viên '{student_id}'."
    
def count_tools_used(memory: list) -> int:
    """
    Đếm số lần các tool đã được gọi trong bộ nhớ của Agent.
    
    Args:
        memory (list): Danh sách các bước đã thực hiện và lưu trữ trong bộ nhớ
        
    Returns:
        int: Số lần tool được gọi
    """
    return sum(1 for entry in memory if "action" in entry and entry["action"].startswith("Call Tool"))
