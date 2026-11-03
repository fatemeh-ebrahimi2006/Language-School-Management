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
           raise TypeError("فقط اشیاء کلاس Course قابل اضافه شدن هستند.")

       for existing_course in self.courses:
           if existing_course.code == course.code :
               raise ValueError("این کد دوره قبلاً ثبت شده است.")

       self.courses.append(course)
       return True

    def get_all_courses(self):
        """فهرست دوره‌های آموزشگاه را برمی‌گرداند."""
        return self.courses

    def get_courses_by_language(self,language):
        """دریافت دوره ها بر اساس زبان"""

        if not isinstance(language,str):
            raise TypeError("زبان باید متنی باشد")

        result = []

        for course in self.courses :
            if course.language.lower() == language.strip().lower():
                result.append(course)

        return result

    def get_courses_by_level(self, level):
        """دریافت دوره‌ها بر اساس سطح"""

        if not isinstance(level, str):
            raise TypeError("سطح باید متنی باشد")

        result = []

        for course in self.courses:
            if course.level.lower() == level.strip().lower():
                result.append(course)

        return result

    def get_courses_by_teacher(self, teacher):
        """دریافت دوره‌ها بر اساس معلم"""

        if not isinstance(teacher, Teacher):
            raise TypeError("معلم باید یک شیء از کلاس Teacher باشد.")

        result = []

        for course in self.courses:
            if course.teacher is teacher:
                result.append(course)

        return result
