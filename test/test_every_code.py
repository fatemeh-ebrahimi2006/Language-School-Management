#
# person1 = Person("fatemeh",
#                  "ebrahimi",
#                  "09376076029",
#                  "5560937241")
# person1.introduce()
# print(person1)

#
# from main import Person
#
# person1 = Person(
#     "fatemeh",
#     "ebrahimi",
#     "09376076029",
#     "5560937241"
# )
#
# # Test 1: Invalid phone
# try:
#     person1.phone = "09376abc029"
# except ValueError as error:
#     print("Phone error:", error)
#
# # Test 2: Empty name
# try:
#     person1.name = "   "
# except ValueError as error:
#     print("Name error:", error)
#
# # Test 3: Change national ID
# try:
#     person1.national_id = "1234567890"
# except AttributeError as error:
#     print("National ID error:", error)
#
# from main import Student
#
# s1=Student("fatemeh",
#            "ebrahimi",
#            "09396076029",
#            "5560937241",
#            ["Turkish","English"],
#            ["beginner", "Intermediate"])
# s1.introduce()
# print(s1)
# print(s1.language_count)
# print(s1.languages)
#
# person1 = Person("Sara", "Ahmadi", "09123456789", "1234567890")
# person1.introduce()

#
# student1 = Student(
#     "Sara",
#     "Ahmadi",
#     "09123456789",
#     "1234567890",
#     ["English", "Turkish"],
#     ["Beginner", "Intermediate"]
# )
#
# # student1.introduce()
#
# from persian_tools import national_id, phone_number
#
# print(national_id.validate("0499370899"))
#
# print(phone_number.validate("09123456789"))

#دادم هوش مصنوعی هم تست کنه

from models.student import Student
from persian_tools import national_id


# ساخت دانش‌آموز با اطلاعات معتبر برای آزمایش
def create_student(
    name="Fatemeh",
    family="Ebrahimi",
    languages=None,
    levels=None
):
    if languages is None:
        languages = ["English"]

    if levels is None:
        levels = ["Beginner"]

    return Student(
        name,
        family,
        "09123456789",
        national_id.generate_random(),
        languages,
        levels
    )


# اجرای آزمایش‌هایی که باید موفق شوند
def test_success(title, function):

    try:
        function()
        print(f"✅ {title}: موفق")

    except Exception as error:
        print(f"❌ {title}: ناموفق - {error}")


# اجرای آزمایش‌هایی که باید خطا ایجاد کنند
def test_error(title, expected_error, function):

    try:
        function()

    except expected_error as error:
        print(f"✅ {title}: خطا به‌درستی شناسایی شد.")

    except Exception as error:
        print(f"❌ {title}: نوع خطای غیرمنتظره - {error}")

    else:
        print(f"❌ {title}: خطایی ایجاد نشد!")


# ---------------- آزمایش اطلاعات معتبر ----------------

# نام فارسی
test_success(
    "نام فارسی",
    lambda: create_student("فاطمه", "ابراهیمی")
)

# نام انگلیسی
test_success(
    "نام انگلیسی",
    lambda: create_student("Fatemeh", "Ebrahimi")
)

# نام و نام خانوادگی چندکلمه‌ای فارسی
test_success(
    "نام فارسی چندکلمه‌ای",
    lambda: create_student("فاطمه زهرا", "ابراهیمی")
)

# نام و نام خانوادگی چندکلمه‌ای انگلیسی
test_success(
    "نام انگلیسی چندکلمه‌ای",
    lambda: create_student("Fatemeh Zahra", "Ebrahimi")
)

# انتخاب چند زبان با سطح‌های متناظر
test_success(
    "انتخاب چند زبان",
    lambda: create_student(
        languages=["English", "Turkish"],
        levels=["Beginner", "Intermediate"]
    )
)


# ---------------- آزمایش نام و نام خانوادگی ----------------

# ترکیب فارسی و انگلیسی در نام
test_error(
    "ترکیب فارسی و انگلیسی در نام",
    ValueError,
    lambda: create_student("فاطمه Fatemeh", "ابراهیمی")
)

# وجود عدد در نام
test_error(
    "وجود عدد در نام",
    ValueError,
    lambda: create_student("Fatemeh123", "Ebrahimi")
)

# وجود علامت در نام
test_error(
    "وجود علامت در نام",
    ValueError,
    lambda: create_student("Fatemeh@", "Ebrahimi")
)

# نام خالی
test_error(
    "نام خالی",
    ValueError,
    lambda: create_student("", "Ebrahimi")
)

# ترکیب فارسی و انگلیسی در نام خانوادگی
test_error(
    "ترکیب فارسی و انگلیسی در نام خانوادگی",
    ValueError,
    lambda: create_student("Fatemeh", "ابراهیمی Ebrahimi")
)


# ---------------- آزمایش زبان‌ها ----------------

# زبان تکراری
test_error(
    "انتخاب زبان تکراری",
    ValueError,
    lambda: create_student(
        languages=["English", "English"],
        levels=["Beginner", "Advanced"]
    )
)

# زبان غیرمجاز
test_error(
    "انتخاب زبان غیرمجاز",
    ValueError,
    lambda: create_student(
        languages=["French"],
        levels=["Beginner"]
    )
)

# فهرست خالی زبان‌ها
test_error(
    "فهرست خالی زبان‌ها",
    ValueError,
    lambda: create_student(
        languages=[],
        levels=[]
    )
)

# ورودی نامعتبر به جای فهرست زبان‌ها
test_error(
    "نوع نامعتبر زبان‌ها",
    TypeError,
    lambda: create_student(languages="English")
)


# ---------------- آزمایش سطح‌های آموزشی ----------------

# سطح غیرمجاز
test_error(
    "سطح آموزشی غیرمجاز",
    ValueError,
    lambda: create_student(
        languages=["English"],
        levels=["Expert"]
    )
)

# فهرست خالی سطح‌ها
test_error(
    "فهرست خالی سطح‌ها",
    ValueError,
    lambda: create_student(
        languages=["English"],
        levels=[]
    )
)

# نوع نامعتبر سطح‌ها
test_error(
    "نوع نامعتبر سطح‌ها",
    TypeError,
    lambda: create_student(
        languages=["English"],
        levels="Beginner"
    )
)


# ---------------- آزمایش تطابق زبان و سطح ----------------

# تعداد زبان‌ها و سطح‌ها متفاوت است
test_error(
    "عدم تطابق تعداد زبان و سطح",
    ValueError,
    lambda: create_student(
        languages=["English", "Turkish"],
        levels=["Beginner"]
    )
)


# ---------------- آزمایش ویژگی‌های Student ----------------

def test_student_information():

    student = create_student(
        "فاطمه",
        "ابراهیمی",
        ["English", "Turkish"],
        ["beginner", "advanced"]
    )

    print("\nاطلاعات دانش‌آموز:")
    student.introduce()

    print("\nتعداد زبان‌ها:", student.language_count)
    print("خروجی repr:")
    print(repr(student))


test_success(
    "نمایش اطلاعات و تعداد زبان‌ها",
    test_student_information
)


print("\nپایان آزمایش‌های کلاس Student.")


from models.teacher import Teacher
from persian_tools import national_id


# ساخت معلم با اطلاعات معتبر برای آزمایش
def create_teacher(
    name="Sara",
    family="Ansari",
    language="English",
    levels=None
):
    if levels is None:
        levels = ["Beginner", "Intermediate"]

    return Teacher(
        name,
        family,
        "09123456789",
        national_id.generate_random(),
        language,
        levels
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

    except expected_error as error:
        print(f"✅ {title}: خطا به‌درستی شناسایی شد.")

    except Exception as error:
        print(f"❌ {title}: نوع خطای غیرمنتظره - {error}")

    else:
        print(f"❌ {title}: خطایی ایجاد نشد!")


# ---------------- آزمایش اطلاعات معتبر ----------------

test_success(
    "ساخت معلم با اطلاعات معتبر",
    lambda: create_teacher()
)

test_success(
    "ساخت معلم با نام فارسی",
    lambda: create_teacher("فاطمه", "ابراهیمی")
)

test_success(
    "ساخت معلم با چند سطح تدریس",
    lambda: create_teacher(
        levels=["Beginner", "Intermediate", "Advanced"]
    )
)

# ---------------- آزمایش زبان ----------------

test_error(
    "زبان غیرمجاز",
    ValueError,
    lambda: create_teacher(language="French")
)

test_error(
    "نوع نامعتبر زبان",
    TypeError,
    lambda: create_teacher(language=123)
)

# ---------------- آزمایش سطح‌ها ----------------

test_error(
    "سطح غیرمجاز",
    ValueError,
    lambda: create_teacher(levels=["Expert"])
)

test_error(
    "سطح تکراری",
    ValueError,
    lambda: create_teacher(
        levels=["Beginner", "Beginner"]
    )
)

test_error(
    "فهرست خالی سطح‌ها",
    ValueError,
    lambda: create_teacher(levels=[])
)

test_error(
    "نوع نامعتبر فهرست سطح‌ها",
    TypeError,
    lambda: create_teacher(levels="Beginner")
)

test_error(
    "نوع نامعتبر یک سطح",
    TypeError,
    lambda: create_teacher(levels=["Beginner", 123])
)

# ---------------- نمایش اطلاعات معلم ----------------

def test_teacher_information():

    teacher = create_teacher()

    print("\nاطلاعات معلم:")
    teacher.introduce()

    print("\nخروجی repr:")
    print(repr(teacher))


test_success(
    "نمایش اطلاعات معلم",
    test_teacher_information
)


print("\nپایان آزمایش‌های کلاس Teacher.")


from models.course import Course
from models.teacher import Teacher
from persian_tools import national_id


# ساخت معلم معتبر برای آزمایش دوره‌ها
def create_teacher(language="English", levels=None):

    if levels is None:
        levels = ["Beginner", "Intermediate", "Advanced"]

    return Teacher(
        "Sara",
        "Ansari",
        "09123456789",
        national_id.generate_random(),
        language,
        levels
    )


# ساخت دوره معتبر برای آزمایش
def create_course(
    code=101,
    language="English",
    level="Beginner",
    teacher=None,
    tuition=2000000
):

    if teacher is None:
        teacher = create_teacher(language)

    return Course(code, language, level, teacher, tuition)


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


# ---------------- آزمایش اطلاعات معتبر ----------------

test_success(
    "ساخت دوره معتبر",
    lambda: create_course()
)

test_success(
    "ساخت دوره ترکی",
    lambda: create_course(language="Turkish")
)

test_success(
    "ساخت دوره اسپانیایی",
    lambda: create_course(language="Spanish")
)

# ---------------- آزمایش کد دوره ----------------

test_error(
    "کد دوره غیرعددی",
    TypeError,
    lambda: create_course(code="101")
)

test_error(
    "کد دوره بولی",
    TypeError,
    lambda: create_course(code=True)
)

test_error(
    "کد دوره منفی",
    ValueError,
    lambda: create_course(code=-101)
)

# ---------------- آزمایش زبان ----------------

test_error(
    "زبان غیرمجاز",
    ValueError,
    lambda: create_course(language="French")
)

test_error(
    "نوع نامعتبر زبان",
    TypeError,
    lambda: create_course(language=123)
)

# ---------------- آزمایش سطح ----------------

test_error(
    "سطح غیرمجاز",
    ValueError,
    lambda: create_course(level="Expert")
)

test_error(
    "نوع نامعتبر سطح",
    TypeError,
    lambda: create_course(level=123)
)

# ---------------- آزمایش معلم ----------------

test_error(
    "ورودی نامعتبر برای معلم",
    TypeError,
    lambda: create_course(teacher="Sara")
)

test_error(
    "عدم تطابق زبان معلم و دوره",
    ValueError,
    lambda: create_course(
        language="English",
        teacher=create_teacher("Turkish")
    )
)

test_error(
    "عدم توانایی معلم در تدریس سطح دوره",
    ValueError,
    lambda: create_course(
        level="Advanced",
        teacher=create_teacher(
            "English",
            ["Beginner", "Intermediate"]
        )
    )
)

# ---------------- آزمایش شهریه ----------------

test_error(
    "شهریه غیرعددی",
    TypeError,
    lambda: create_course(tuition="2000000")
)

test_error(
    "شهریه بولی",
    TypeError,
    lambda: create_course(tuition=True)
)

test_error(
    "شهریه منفی",
    ValueError,
    lambda: create_course(tuition=-1000)
)

# ---------------- نمایش اطلاعات دوره ----------------

def test_course_information():

    course = create_course()

    print("\nاطلاعات دوره:")
    print(course)

    print("\nکد دوره:", course.code)
    print("زبان دوره:", course.language)
    print("سطح دوره:", course.level)
    print("نام معلم:", course.teacher.name)
    print("شهریه:", course.tuition)


test_success(
    "نمایش اطلاعات دوره",
    test_course_information
)


print("\nپایان آزمایش‌های کلاس Course.")
