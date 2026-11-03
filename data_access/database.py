
import sqlite3
import os


# مسیر فایل پایگاه داده
DATABASE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "language_school.db"
)


# ساخت جدول ثبت نام
def create_table():

    connection = sqlite3.connect(DATABASE_NAME)

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                student_family TEXT NOT NULL,
                phone TEXT NOT NULL,
                national_id TEXT NOT NULL,
                language TEXT NOT NULL,
                level TEXT NOT NULL,
                course_code INTEGER NOT NULL,
                teacher_name TEXT NOT NULL,
                tuition INTEGER NOT NULL
            )
        """)

        connection.commit()

    finally:
        connection.close()


# ذخیره اطلاعات ثبت نام
def save_registration(student, course):

    connection = sqlite3.connect(DATABASE_NAME)

    try:
        cursor = connection.cursor()

        # بررسی ثبت نام تکراری
        cursor.execute("""
            SELECT id FROM registrations
            WHERE national_id = ? AND course_code = ?
        """, (
            student.national_id,
            course.code
        ))

        existing_registration = cursor.fetchone()

        if existing_registration is not None:
            raise ValueError(
                "این دانش‌آموز قبلاً در این دوره ثبت‌ نام کرده است."
            )

        # ذخیره ثبت نام جدید
        cursor.execute("""
            INSERT INTO registrations (
                student_name,
                student_family,
                phone,
                national_id,
                language,
                level,
                course_code,
                teacher_name,
                tuition
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            student.name,
            student.family,
            student.phone,
            student.national_id,
            course.language,
            course.level,
            course.code,
            f"{course.teacher.name} {course.teacher.family}",
            course.tuition
        ))

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


# دریافت تمام ثبت نام ها
def get_all_registrations():

    connection = sqlite3.connect(DATABASE_NAME)

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM registrations")

        registrations = cursor.fetchall()

        return registrations

    finally:
        connection.close()


# اجرای آزمایشی فایل
if __name__ == "__main__":
    create_table()
    print("Database and table created successfully!")

    print(get_all_registrations())
