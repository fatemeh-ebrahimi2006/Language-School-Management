# این فایل مسئول مدیریت دوره‌های آموزشی، افزودن دوره و جست‌وجوی آن‌ها است.

from models.course import Course
from models.teacher import Teacher

class CourseService :
    """مدیریت دوره های اموزشی اموزشگاه زبان"""

    def __init__(self):
    #لیست دوره هایی که در اموزشگاه تعریف میشود
        self.courses = []
    def add_course(self,course):
       """یک دورهٔ معتبر را به فهرست دوره‌ها اضافه می‌کند."""

       if not isinstance(course,Course):
           raise TypeError("Only Course objects can be added.")

       for existing_course in self.courses:
           if existing_course.code == course.code :
               raise ValueError("Course code already exists.")

       self.courses.append(course)
       return True

    def get_all_courses(self):
        """فهرست دوره‌های آموزشگاه را برمی‌گرداند."""
        return self.courses

    def get_courses_by_language(self,language):
        """دریافت دوره ها بر اساس زبان"""

        if not isinstance(language,str):
            raise TypeError("Language must be string!!!")

        result = []

        for course in self.courses :
            if course.language.lower() == language.strip().lower():
                result.append(course)

        return result

    def get_courses_by_level(self, level):
        """دریافت دوره‌ها بر اساس سطح"""

        if not isinstance(level, str):
            raise TypeError("Level must be a string.")

        result = []

        for course in self.courses:
            if course.level.lower() == level.strip().lower():
                result.append(course)

        return result

    def get_courses_by_teacher(self, teacher):
        """دریافت دوره‌ها بر اساس معلم"""

        if not isinstance(teacher, Teacher):
            raise TypeError("Teacher must be a Teacher object.")

        result = []

        for course in self.courses:
            if course.teacher is teacher:
                result.append(course)

        return result
