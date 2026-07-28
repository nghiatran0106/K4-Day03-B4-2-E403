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

from functools import wraps

MOCK_API = {
    "students": {
        "SV001": {"name": "Nguyễn Văn A", "major": "Công nghệ thông tin", "year": 2},
        "SV002": {"name": "Trần Thị B", "major": "Kinh tế", "year": 3},
        "SV003": {"name": "Lê Văn C", "major": "Điện tử viễn thông", "year": 1},
    },
    "skills": {
        "SV001": ["Python", "Machine Learning", "Data Analysis"],
        "SV002": ["Marketing", "Sales", "Business Strategy"],
        "SV003": ["Circuit Design", "Embedded Systems"],
    },
    "course_prerequisites": {
        "CS101": [],
        "CS201": ["CS101"],
        "CS301": ["CS201"],
        "ECON101": [],
        "ECON201": ["ECON101"],
    },
    "course_recommendations": {
        "SV001": ["CS201", "CS301"],
        "SV002": ["ECON201", "ECON301"],
        "SV003": ["EE201", "EE301"],
    },
    "course_details": {
        "CS101": {"title": "Introduction to Computer Science", "instructor": "Dr. A", "schedule": "Mon/Wed 10:00-11:30"},
        "CS201": {"title": "Data Structures and Algorithms", "instructor": "Dr. B", "schedule": "Tue/Thu 14:00-15:30"},
        "CS301": {"title": "Machine Learning", "instructor": "Dr. C", "schedule": "Mon/Wed 16:00-17:30"},
        "ECON101": {"title": "Principles of Economics", "instructor": "Dr. D", "schedule": "Tue/Thu 10:00-11:30"},
        "ECON201": {"title": "Microeconomics", "instructor": "Dr. E", "schedule": "Mon/Wed 14:00-15:30"},
    },
    "learning_paths": {
        "SV001": ["CS101", "CS201", "CS301"],
        "SV002": ["ECON101", "ECON201", "ECON301"],
        "SV003": ["EE101", "EE201", "EE301"],
    },
    "schedules": {
        "SV001": {"Mon": ["CS101 10:00-11:30"], "Wed": ["CS201 14:00-15:30"]},
        "SV002": {"Tue": ["ECON101 10:00-11:30"], "Thu": ["ECON201 14:00-15:30"]},
        "SV003": {"Mon": ["EE101 10:00-11:30"], "Wed": ["EE201 14:00-15:30"]},
    },
}

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


def _tool_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            return f"LỖI: {func.__name__} - {str(exc)}"
    return wrapper

@_tool_error_handler
def get_student_profile(student_id: str) -> dict:
    """
    Lấy hồ sơ sinh viên dựa trên ID sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        dict: Thông tin hồ sơ sinh viên
    """
    return MOCK_API["students"].get(student_id, {"error": f"Không tìm thấy hồ sơ cho ID '{student_id}'."})

@_tool_error_handler
def check_actived_skills(student_id: str) -> list:
    """
    Kiểm tra các kỹ năng đang được kích hoạt cho sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        list: Danh sách kỹ năng đang được kích hoạt
    """
    return MOCK_API["skills"].get(student_id, [])

@_tool_error_handler
def get_course_prerequisites(course_id: str) -> list:
    """
    Lấy điều kiện tiên quyết của một khóa học cụ thể.
    
    Args:
        course_id (str): Mã khóa học
        
    Returns:
        list: Danh sách các khóa học tiên quyết
    """
    return MOCK_API["course_prerequisites"].get(course_id, [])

@_tool_error_handler
def recommend_course(student_id: str) -> list:
    """
    Đề xuất khóa học phù hợp dựa trên hồ sơ và mục tiêu học tập của sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        list: Danh sách khóa học được đề xuất
    """
    return MOCK_API["course_recommendations"].get(student_id, [])

@_tool_error_handler
def search_courses(keyword: str) -> list:
    """
    Tìm kiếm khóa học theo từ khóa.
    
    Args:
        keyword (str): Từ khóa tìm kiếm
        
    Returns:
        list: Danh sách khóa học phù hợp
    """
    return [course_id for course_id, title in MOCK_API["course_details"].items() if keyword.lower() in title["title"].lower()]

@_tool_error_handler
def get_course_detail(course_id: str) -> dict:
    """
    Lấy chi tiết về một khóa học cụ thể.
    
    Args:
        course_id (str): Mã khóa học
        
    Returns:
        dict: Thông tin chi tiết về khóa học
    """
    return MOCK_API["course_details"].get(course_id, {"error": f"Không tìm thấy chi tiết cho khóa học '{course_id}'."})

def _is_error_result(result):
    return isinstance(result, str) and result.startswith("LỖI:")

@_tool_error_handler
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
    if _is_error_result(prerequisites):
        return False

    student_courses = recommend_course(student_id)  # Giả lập danh sách khóa học đã hoàn thành
    if _is_error_result(student_courses):
        return False

    if not isinstance(prerequisites, list) or not isinstance(student_courses, list):
        return False

    return all(prereq in student_courses for prereq in prerequisites)

@_tool_error_handler
def generate_learning_path(student_id: str) -> list:
    """
    Sinh lộ trình học tập cá nhân hóa cho sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        list: Danh sách khóa học trong lộ trình học tập
    """
    return MOCK_API["learning_paths"].get(student_id, [])

@_tool_error_handler
def find_schedule(student_id: str) -> dict:
    """
    Tìm thời khóa biểu hoặc lịch học phù hợp cho sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        
    Returns:
        dict: Thời khóa biểu của sinh viên
    """
    return MOCK_API["schedules"].get(student_id, {"error": f"Không tìm thấy thời khóa biểu cho ID '{student_id}'."})

@_tool_error_handler
def register_course(student_id: str, course_id: str) -> str:
    """
    Đăng ký khóa học cho sinh viên.
    
    Args:
        student_id (str): Mã số sinh viên
        course_id (str): Mã khóa học
        
    Returns:
        str: Thông báo kết quả đăng ký
    """
    eligibility = check_course_eligibility(student_id, course_id)
    if isinstance(eligibility, str) and eligibility.startswith("LỖI:"):
        return f"LỖI: register_course - Không thể kiểm tra điều kiện đăng ký do lỗi hệ thống."

    if eligibility:
        return f"Đăng ký thành công khóa học '{course_id}' cho sinh viên '{student_id}'."
    else:
        return f"Không đủ điều kiện đăng ký khóa học '{course_id}' cho sinh viên '{student_id}'."
    
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
    "get_student_profile": get_student_profile,
    "check_actived_skills": check_actived_skills,
    "get_course_prerequisites": get_course_prerequisites,
    "recommend_course": recommend_course,
    "search_courses": search_courses,
    "get_course_detail": get_course_detail,
    "check_course_eligibility": check_course_eligibility,
    "generate_learning_path": generate_learning_path,
    "find_schedule": find_schedule,
    "register_course": register_course,
    "count_tools_used": count_tools_used,
}
