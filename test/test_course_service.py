
from business_logic.course_service import CourseService
from models.course import Course
from models.teacher import Teacher
from persian_tools import national_id


# ساخت معلم معتبر برای آزمایش
def create_teacher(language="English"):

    return Teacher(
        "Sara",
        "Ansari",
        "09123456789",
        national_id.generate_random(),
        language,
        ["Beginner", "Intermediate", "Advanced"]
    )


# ساخت دوره معتبر برای آزمایش
def create_course(code=101, language="English", level="Beginner", teacher=None):

    if teacher is None:
        teacher = create_teacher(language)

    return Course(
        code,
        language,
        level,
        teacher,
        2000000
    )


# آزمایش مواردی که باید موفق شوند
def test_success(title, function):

    try:
        function()
        print(f"✅ {title}: موفق")

    except Exception as error:
        print(f"❌ {title}: ناموفق - {error}")


# آزمایش مواردی که باید خطا ایجاد کنند
def test_error(title, expected_error, function):

    try:
        function()

    except expected_error:
        print(f"✅ {title}: خطا به‌درستی شناسایی شد.")

    except Exception as error:
        print(f"❌ {title}: نوع خطای غیرمنتظره - {error}")

    else:
        print(f"❌ {title}: خطایی ایجاد نشد!")


# -------------------- آزمایش اضافه کردن دوره --------------------

def test_add_course():

    service = CourseService()

    course = create_course()

    result = service.add_course(course)

    assert result is True
    assert len(service.get_all_courses()) == 1


test_success(
    "اضافه کردن دوره معتبر",
    test_add_course
)


# جلوگیری از اضافه کردن اطلاعات غیر از Course
test_error(
    "اضافه کردن شیء نامعتبر",
    TypeError,
    lambda: CourseService().add_course("English")
)


# جلوگیری از کد دوره تکراری
def test_duplicate_course():

    service = CourseService()

    course1 = create_course(code=101)
    course2 = create_course(code=101)

    service.add_course(course1)

    service.add_course(course2)


test_error(
    "جلوگیری از کد دوره تکراری",
    ValueError,
    test_duplicate_course
)


# -------------------- آزمایش دریافت تمام دوره‌ها --------------------

def test_get_all_courses():

    service = CourseService()

    service.add_course(create_course(101))
    service.add_course(create_course(102))

    courses = service.get_all_courses()

    assert len(courses) == 2


test_success(
    "دریافت تمام دوره‌ها",
    test_get_all_courses
)


# -------------------- آزمایش جست‌وجو بر اساس زبان --------------------

def test_courses_by_language():

    service = CourseService()

    service.add_course(create_course(101, "English"))
    service.add_course(create_course(102, "Turkish"))
    service.add_course(create_course(103, "English"))

    result = service.get_courses_by_language(" English ")

    assert len(result) == 2

    assert all(
        course.language == "English"
        for course in result
    )


test_success(
    "جست‌وجوی دوره‌ها بر اساس زبان",
    test_courses_by_language
)


test_error(
    "ورودی نامعتبر برای زبان",
    TypeError,
    lambda: CourseService().get_courses_by_language(123)
)


# -------------------- آزمایش جست‌وجو بر اساس سطح --------------------

def test_courses_by_level():

    service = CourseService()

    service.add_course(create_course(101, level="Beginner"))
    service.add_course(create_course(102, level="Advanced"))
    service.add_course(create_course(103, level="Beginner"))

    result = service.get_courses_by_level(" beginner ")

    assert len(result) == 2

    assert all(
        course.level == "Beginner"
        for course in result
    )


test_success(
    "جست‌وجوی دوره‌ها بر اساس سطح",
    test_courses_by_level
)


test_error(
    "ورودی نامعتبر برای سطح",
    TypeError,
    lambda: CourseService().get_courses_by_level(123)
)


# -------------------- آزمایش جست‌وجو بر اساس معلم --------------------

def test_courses_by_teacher():

    service = CourseService()

    teacher1 = create_teacher()
    teacher2 = create_teacher()

    service.add_course(
        create_course(101, teacher=teacher1)
    )

    service.add_course(
        create_course(102, teacher=teacher2)
    )

    service.add_course(
        create_course(103, teacher=teacher1)
    )

    result = service.get_courses_by_teacher(teacher1)

    assert len(result) == 2

    assert all(
        course.teacher is teacher1
        for course in result
    )


test_success(
    "جست‌وجوی دوره‌ها بر اساس معلم",
    test_courses_by_teacher
)


test_error(
    "ورودی نامعتبر برای معلم",
    TypeError,
    lambda: CourseService().get_courses_by_teacher("Sara")
)


print("\nپایان آزمایش‌های CourseService.")
