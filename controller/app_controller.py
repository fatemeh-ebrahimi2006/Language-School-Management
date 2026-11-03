#وظیفه Controller اینه که بین رابط گرافیکی، کلاس‌ها و پایگاه داده ارتباط برقرار کنه.

from persian_tools import national_id
from models.teacher import Teacher
from models.course import Course
from models.student import Student

from business_logic.course_service import CourseService

from data_access.database import (
    create_table,
    save_registration,
    get_all_registrations as fetch_all_registrations
)


class AppController:
    """مدیریت ارتباط بین بخش‌های مختلف برنامه"""

    def __init__(self):

        # ساخت جدول پایگاه داده
        create_table()

        # ساخت سرویس مدیریت دوره‌ها
        self.course_service = CourseService()

        # ایجاد دوره‌های نمونه
        self.create_sample_courses()

    def create_sample_courses(self):
        """ساخت معلم‌ها و دوره‌های نمونه آموزشگاه"""

        # ساخت معلم‌ها
        teacher1 = Teacher(
            "Sara", "Ansari", "09398766029",
             national_id.generate_random(),
            "English", ["Beginner", "Intermediate", "Advanced"]
        )

        teacher2 = Teacher(
            "Ahmad", "Ebadi", "09918835420",
             national_id.generate_random(),
            "Turkish", ["Beginner", "Intermediate", "Advanced"]
        )

        teacher3 = Teacher(
            "Maria", "Ahmadi", "09123456789",
             national_id.generate_random(),
            "Spanish", ["Beginner", "Intermediate", "Advanced"]
        )

        # ساخت دوره‌ها
        courses = [
            Course(101, "English", "Beginner", teacher1, 2_000_000),
            Course(102, "English", "Intermediate", teacher1, 2_500_000),
            Course(103, "English", "Advanced", teacher1, 3_000_000),

            Course(104, "Turkish", "Beginner", teacher2, 2_000_000),
            Course(105, "Turkish", "Intermediate", teacher2, 2_500_000),
            Course(106, "Turkish", "Advanced", teacher2, 3_000_000),

            Course(107, "Spanish", "Beginner", teacher3, 2_000_000),
            Course(108, "Spanish", "Intermediate", teacher3, 2_500_000),
            Course(109, "Spanish", "Advanced", teacher3, 3_000_000)
        ]

        for course in courses:
            self.course_service.add_course(course)

    def get_courses_by_language(self, language):
        """دریافت دوره‌های یک زبان"""

        return self.course_service.get_courses_by_language(language)

    def get_course_by_code(self, course_code):
        """پیدا کردن یک دوره با کد آن"""

        for course in self.course_service.get_all_courses():

            if course.code == course_code:
                return course

        return None

    def register_student(self, name, family, phone, national_id, course):
        """ثبت‌نام دانش‌آموز در یک دوره"""

        # بررسی معتبر بودن دوره انتخاب‌شده
        if not isinstance(course, Course):
            raise TypeError("دوره انتخاب‌ شده معتبر نیست.")

        student = Student(
            name,
            family,
            phone,
            national_id,
            [course.language],
            [course.level]
        )

        registration_id = save_registration(student, course)

        return student, registration_id

    def get_all_registrations(self):
        """دریافت تمام ثبت‌نام‌های ذخیره‌شده"""

        return fetch_all_registrations()
