
import customtkinter as ctk
import sqlite3
from tkinter import messagebox

from controller.app_controller import AppController


class MainWindow:
    """رابط گرافیکی آموزشگاه زبان"""

    # نکات تکمیلی طراحی رابط کاربری:
    # 1. فارسی‌سازی متن‌های نمایش دوره‌ها و جزئیات آن‌ها.
    # 2. هماهنگ‌کردن گزینه‌های کادر انتخاب دوره با زبان فارسی و انگلیسی.
    # 3. فارسی‌سازی و راست‌چین‌کردن فرم ثبت‌نام و پنجره سوابق.
    # 4. حفظ منطق Controller، اعتبارسنجی و SQLite بدون تغییر.

    def __init__(self, controller):

        # دریافت کنترلر و آماده‌سازی دوره انتخاب‌شده
        self.controller = controller
        self.selected_course = None

        # تنظیم ظاهر کلی برنامه
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # ساخت پنجره اصلی آموزشگاه
        self.window = ctk.CTk()
        self.window.title("آموزشگاه زبان")


        # تعیین اندازه اولیه پنجره
        self.window.geometry("950x600")
        # تعیین حداقل اندازه مجاز پنجره
        self.window.minsize(850, 540)
        self.window.resizable(True, True)

        # تعیین رنگ پس‌زمینه پنجره
        self.window.configure(fg_color="#F1F5F9")

        # ---------------- سربرگ اصلی ----------------

        # ساخت سربرگ بالای صفحه
        header = ctk.CTkFrame(
            self.window,
            height=95,
            corner_radius=0,
            fg_color="#16324F"
        )
        header.pack(fill="x")

        # جلوگیری از تغییر ارتفاع سربرگ بر اساس محتوای آن
        header.pack_propagate(False)

        # نمایش نام آموزشگاه
        title_label = ctk.CTkLabel(
            header,
            text="آموزشگاه زبان",
            font=("Arial", 30, "bold"),
            text_color="#FFFFFF"
        )
        title_label.pack(pady=(22, 5))

        # نمایش توضیح کوتاه آموزشگاه
        subtitle_label = ctk.CTkLabel(
            header,
            text="سامانه مدیریت دوره‌ها و ثبت‌نام دانش‌آموزان",
            font=("Arial", 14),
            text_color="#D6E5F5"
        )
        subtitle_label.pack()

        # ---------------- بخش اصلی صفحه ----------------

        # ساخت کادر اصلی برای قرارگیری منو و اطلاعات دوره
        main_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )
        main_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        # ---------------- منوی سمت چپ ----------------

        # ساخت پنل انتخاب زبان‌ها و دسترسی به سوابق
        left_panel = ctk.CTkFrame(
            main_frame,
            width=260,
            corner_radius=18,
            fg_color="#FFFFFF"
        )
        left_panel.pack(
            side="left",
            fill="y",
            padx=(0, 20)
        )

        # ثابت نگه‌داشتن عرض پنل منو
        left_panel.pack_propagate(False)

        # عنوان منوی سمت چپ
        language_title = ctk.CTkLabel(
            left_panel,
            text="انتخاب زبان",
            font=("Arial", 20, "bold"),
            text_color="#16324F"
        )
        language_title.pack(pady=(30, 25))

        # دکمه زبان انگلیسی
        self.english_button = ctk.CTkButton(
            left_panel,
            text="انگلیسی (English)",
            width=210,
            height=52,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.select_english
        )
        self.english_button.pack(pady=10)

        # دکمه زبان ترکی
        self.turkish_button = ctk.CTkButton(
            left_panel,
            text="ترکی استانبولی (Turkish)",
            width=210,
            height=52,
            corner_radius=12,
            font=("Arial", 14, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.select_turkish
        )
        self.turkish_button.pack(pady=10)

        # دکمه زبان اسپانیایی
        self.spanish_button = ctk.CTkButton(
            left_panel,
            text="اسپانیایی (Spanish)",
            width=210,
            height=52,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.select_spanish
        )
        self.spanish_button.pack(pady=10)

        # دکمه مشاهده سوابق ثبت‌نام
        self.history_button = ctk.CTkButton(
            left_panel,
            text="سوابق ثبت‌نام",
            width=210,
            height=45,
            corner_radius=12,
            fg_color="#0F766E",
            hover_color="#115E59",
            font=("Arial", 15, "bold"),
            command=self.show_registrations
        )
        self.history_button.pack(
            side="bottom",
            pady=25
        )

        # ---------------- بخش اطلاعات دوره‌ها ----------------

        # ساخت پنل سمت راست برای نمایش دوره‌ها
        right_panel = ctk.CTkFrame(
            main_frame,
            corner_radius=18,
            fg_color="#FFFFFF"
        )
        right_panel.pack(
            side="right",
            fill="both",
            expand=True
        )

        # عنوان بخش دوره‌ها
        course_title = ctk.CTkLabel(
            right_panel,
            text="دوره‌های آموزشی",
            font=("Arial", 22, "bold"),
            text_color="#16324F"
        )
        course_title.pack(pady=(25, 10))

        # کادر نمایش اطلاعات دوره و معلم
        self.result_label = ctk.CTkLabel(
            right_panel,
            text="برای مشاهده دوره‌ها، ابتدا یک زبان را انتخاب کنید.",
            width=490,
            height=160,
            corner_radius=12,
            fg_color="#F1F5F9",
            text_color="#1F2937",
            font=("Arial", 15),
            justify="right",
            anchor="e",
            wraplength=550
        )

        # تنظیم اندازه و محل کادر اطلاعات دوره
        self.result_label.pack(
            padx=20,
            pady=8,
            fill="x"
        )

        # عنوان کادر انتخاب دوره
        course_label = ctk.CTkLabel(
            right_panel,
            text="دوره موردنظر خود را انتخاب کنید:",
            font=("Arial", 15, "bold"),
            text_color="#16324F"
        )
        course_label.pack(pady=(12, 5))

        # ساخت کادر انتخاب دوره
        self.course_combo = ctk.CTkComboBox(
            right_panel,
            values=["انتخاب دوره"],
            width=300,
            state="readonly",
            command=self.show_course_details,
            justify="center"
        )
        self.course_combo.pack(pady=5)
        self.course_combo.set("انتخاب دوره")

        # دکمه ثبت‌نام در دوره
        self.register_button = ctk.CTkButton(
            right_panel,
            text="ثبت‌نام در دوره",
            width=220,
            height=45,
            corner_radius=12,
            fg_color="#0F766E",
            hover_color="#115E59",
            font=("Arial", 16, "bold"),
            command=self.open_registration_form,
            state="disabled"
        )
        self.register_button.pack(pady=12)

    # انتخاب زبان انگلیسی
    def select_english(self):
        self.show_courses("English")

    # انتخاب زبان ترکی
    def select_turkish(self):
        self.show_courses("Turkish")

    # انتخاب زبان اسپانیایی
    def select_spanish(self):
        self.show_courses("Spanish")


    # نمایش دوره‌های زبان انتخاب‌شده
    def show_courses(self, language):

        # پاک کردن دوره انتخاب‌شده قبلی
        self.selected_course = None

        # غیرفعال کردن دکمه ثبت‌نام تا انتخاب دوره جدید
        self.register_button.configure(state="disabled")

        # دریافت دوره‌های زبان انتخاب‌شده از کنترلر
        courses = self.controller.get_courses_by_language(language)

        # ترجمه نام زبان‌ها برای نمایش به کاربر
        language_names = {
            "English": "انگلیسی (English)",
            "Turkish": "ترکی استانبولی (Turkish)",
            "Spanish": "اسپانیایی (Spanish)"
        }

        # ترجمه سطح‌های آموزشی برای نمایش به کاربر
        level_names = {
            "Beginner": "مبتدی (Beginner)",
            "Intermediate": "متوسط (Intermediate)",
            "Advanced": "پیشرفته (Advanced)"
        }

        # آماده کردن عنوان فهرست دوره‌ها
        details = f"دوره‌های زبان {language_names.get(language, language)}:\n\n"

        # ساخت فهرست گزینه‌های کادر انتخاب دوره
        course_options = []

        # بررسی دوره‌های پیدا شده
        for course in courses:

            # تبدیل نام انگلیسی سطح به عنوان فارسی و انگلیسی
            level_title = level_names.get(course.level, course.level)

            # اضافه کردن کد و سطح دوره به گزینه‌های انتخاب
            course_options.append(
                f"{course.code} - {level_title}"
            )

            # اضافه کردن اطلاعات دوره به متن نمایش
            details += (
                f"کد دوره: {course.code}\n"
                f"سطح: {level_title}\n\n"
            )

        # اگر هیچ دوره‌ای برای زبان وجود نداشت
        if not courses:
            details = "در حال حاضر دوره‌ای برای این زبان موجود نیست."

        # به‌روزرسانی گزینه‌های کادر انتخاب دوره
        self.course_combo.configure(values=course_options)

        # تنظیم متن اولیه کادر انتخاب
        self.course_combo.set("انتخاب دوره")

        # نمایش اطلاعات دوره‌ها در پنجره
        self.result_label.configure(text=details)


    # نمایش جزئیات دوره انتخاب‌شده
    def show_course_details(self, selected_value):

        # جلوگیری از اجرای تابع قبل از انتخاب واقعی دوره
        if selected_value == "انتخاب دوره":
            return

        # استخراج کد دوره از گزینه انتخاب‌شده
        course_code = int(selected_value.split(" - ")[0])

        # پیدا کردن دوره از طریق کنترلر
        course = self.controller.get_course_by_code(course_code)

        # بررسی موجود بودن دوره
        if course is None:
            messagebox.showerror(
                "خطای انتخاب دوره",
                "دوره موردنظر پیدا نشد."
            )
            return

        # ذخیره دوره انتخاب‌شده
        self.selected_course = course

        # ترجمه نام زبان‌ها
        language_names = {
            "English": "انگلیسی (English)",
            "Turkish": "ترکی استانبولی (Turkish)",
            "Spanish": "اسپانیایی (Spanish)"
        }

        # ترجمه سطح‌های آموزشی
        level_names = {
            "Beginner": "مبتدی (Beginner)",
            "Intermediate": "متوسط (Intermediate)",
            "Advanced": "پیشرفته (Advanced)"
        }

        # آماده کردن اطلاعات دوره انتخاب‌شده
        details = (
            f"جزئیات دوره انتخاب‌شده\n\n"
            f"کد دوره: {course.code}\n"
            f"زبان: {language_names.get(course.language, course.language)}\n"
            f"سطح: {level_names.get(course.level, course.level)}\n"
            f"مدرس: {course.teacher.name} {course.teacher.family}\n"
            f"شهریه: {course.tuition:,} تومان"
        )

        # نمایش جزئیات دوره در پنجره
        self.result_label.configure(text=details)

        # فعال کردن دکمه ثبت‌نام پس از انتخاب دوره
        self.register_button.configure(state="normal")


    # ساخت فرم ثبت‌نام دانش‌آموز
    def open_registration_form(self):

        # بررسی انتخاب‌شدن دوره
        if self.selected_course is None:
            messagebox.showwarning(
                "انتخاب دوره",
                "لطفاً ابتدا یک دوره آموزشی انتخاب کنید."
            )
            return

        # ساخت پنجره ثبت‌نام
        form_window = ctk.CTkToplevel(self.window)
        form_window.title("ثبت‌نام دانش‌آموز")
        form_window.geometry("520x570")
        # تعیین حداقل اندازه پنجره ثبت‌نام
        form_window.minsize(520, 570)
        # اجازه بزرگ و کوچک کردن پنجره ثبت‌نام
        form_window.resizable(True, True)
        form_window.configure(fg_color="#F1F5F9")

        # ساخت سربرگ فرم
        header = ctk.CTkFrame(
            form_window,
            height=90,
            corner_radius=0,
            fg_color="#16324F"
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        # نمایش عنوان فرم
        title = ctk.CTkLabel(
            header,
            text="فرم ثبت‌نام دانش‌آموز",
            font=("Arial", 24, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(pady=25)

        # ساخت بخش داخلی فرم
        form_frame = ctk.CTkFrame(
            form_window,
            corner_radius=18,
            fg_color="#FFFFFF"
        )
        form_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # نمایش دوره انتخاب‌شده
        course_info = ctk.CTkLabel(
            form_frame,
            text=(
                f"دوره انتخاب‌شده: "
                f"{self.selected_course.language} - "
                f"{self.selected_course.level}"
            ),
            font=("Arial", 14, "bold"),
            text_color="#16324F"
        )
        course_info.pack(pady=(15, 10))

        # ایجاد کادر ورود نام
        name_label = ctk.CTkLabel(
            form_frame,
            text=": نام",
            font=("Arial", 14, "bold"),
            anchor="e"
        )
        name_label.pack(anchor="e", padx=25, pady=(8, 2))

        name_entry = ctk.CTkEntry(
            form_frame,
            width=410,
            height=38,
            justify="right",
        )
        name_entry.pack(padx=25)

        # ایجاد کادر ورود نام خانوادگی
        family_label = ctk.CTkLabel(
            form_frame,
            text=": نام خانوادگی",
            font=("Arial", 14, "bold"),
            anchor="e",
            justify="right",
        )
        family_label.pack(anchor="e", padx=25, pady=(10, 2))

        family_entry = ctk.CTkEntry(
            form_frame,
            width=410,
            height=38,
            justify="right",
        )
        family_entry.pack(padx=25)

        # ایجاد کادر ورود شماره موبایل
        phone_label = ctk.CTkLabel(
            form_frame,
            text=": شماره موبایل",
            font=("Arial", 14, "bold"),
            anchor="e",
            justify="right",
        )
        phone_label.pack(anchor="e", padx=25, pady=(10, 2))

        phone_entry = ctk.CTkEntry(
            form_frame,
            width=410,
            height=38,
            justify="right",
            placeholder_text="مثال: 09123456789"
        )
        phone_entry.pack(padx=25)

        # نمایش راهنمای شماره موبایل
        phone_hint = ctk.CTkLabel(
            form_frame,
            text="شماره باید ۱۱ رقم انگلیسی و با 09 شروع شود.",
            font=("Arial", 11),
            text_color="#64748B"
        )
        phone_hint.pack(anchor="e", padx=25)

        # ایجاد کادر ورود کد ملی
        national_id_label = ctk.CTkLabel(
            form_frame,
            text=": کد ملی",
            font=("Arial", 14, "bold"),
            anchor="e",
            justify="right",
        )
        national_id_label.pack(anchor="e", padx=25, pady=(8, 2))

        national_id_entry = ctk.CTkEntry(
            form_frame,
            width=410,
            height=38,
            justify="right",
            placeholder_text=" رقم 10"
        )
        national_id_entry.pack(padx=25)

        # نمایش راهنمای کد ملی
        national_id_hint = ctk.CTkLabel(
            form_frame,
            text="کد ملی باید ۱۰ رقم انگلیسی و معتبر باشد.",
            font=("Arial", 11),
            text_color="#64748B"
        )
        national_id_hint.pack(anchor="e", padx=25)

        # ثبت اطلاعات دانش‌آموز
        def register_student():

            try:
                # دریافت اطلاعات و ثبت‌نام دانش‌آموز از طریق کنترلر
                student, registration_id = self.controller.register_student(
                    name_entry.get(),
                    family_entry.get(),
                    phone_entry.get(),
                    national_id_entry.get(),
                    self.selected_course
                )

                # ترجمه نام زبان برای نمایش در رسید
                language_names = {
                    "English": "انگلیسی",
                    "Turkish": "ترکی استانبولی",
                    "Spanish": "اسپانیایی"
                }

                # ترجمه سطح دوره برای نمایش در رسید
                level_names = {
                    "Beginner": "مبتدی",
                    "Intermediate": "متوسط",
                    "Advanced": "پیشرفته"
                }

                # نمایش رسید فارسی ثبت‌نام
                messagebox.showinfo(
                    "ثبت‌نام موفق",
                    f"شماره ثبت‌نام: {registration_id}\n"
                    f"نام دانش‌آموز: {student.name} {student.family}\n"
                    f"زبان: {language_names.get(self.selected_course.language)}\n"
                    f"سطح: {level_names.get(self.selected_course.level)}\n"
                    f"مدرس: {self.selected_course.teacher.name} "
                    f"{self.selected_course.teacher.family}\n"
                    f"شهریه: {self.selected_course.tuition:,} تومان",
                    parent=form_window
                )

                # بستن فرم پس از ثبت‌نام موفق
                form_window.destroy()

            except (TypeError, ValueError, sqlite3.Error) as error:

                # نمایش پیام خطا در صورت نامعتبر بودن اطلاعات
                messagebox.showerror(
                    "خطا در ثبت‌نام",
                    str(error),
                    parent=form_window
                )

        # ساخت دکمه تایید ثبت‌نام
        register_button_form = ctk.CTkButton(
            form_frame,
            text="ثبت‌نام",
            width=180,
            height=42,
            corner_radius=12,
            font=("Arial", 15, "bold"),
            fg_color="#0F766E",
            hover_color="#115E59",
            command=register_student
        )
        register_button_form.pack(pady=18)

        # قرار دادن فرم در حالت فعال
        form_window.grab_set()


    # نمایش سوابق ثبت‌نام دانش‌آموزان
    def show_registrations(self):

        # دریافت تمام ثبت‌نام‌های ذخیره‌شده از پایگاه داده
        records = self.controller.get_all_registrations()

        # ساخت پنجره جدید سوابق ثبت‌نام
        history_window = ctk.CTkToplevel(self.window)
        history_window.title("سوابق ثبت‌نام")
        history_window.geometry("1100x620")
        history_window.minsize(900, 500)
        history_window.resizable(True, True)
        history_window.configure(fg_color="#F1F5F9")

        # ساخت سربرگ پنجره سوابق
        header = ctk.CTkFrame(
            history_window,
            height=90,
            corner_radius=0,
            fg_color="#16324F"
        )
        header.pack(fill="x")

        # ثابت نگه‌داشتن ارتفاع سربرگ
        header.pack_propagate(False)

        # نمایش عنوان پنجره سوابق
        title = ctk.CTkLabel(
            header,
            text="سوابق ثبت‌نام",
            font=("Arial", 24, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(pady=(15, 5))

        # نمایش تعداد ثبت‌نام‌های موجود
        count_label = ctk.CTkLabel(
            header,
            text=f"تعداد ثبت‌نام‌ها: {len(records)}",
            font=("Arial", 13),
            text_color="#D6E5F5"
        )
        count_label.pack()

        # ساخت بخش اصلی جدول
        table_frame = ctk.CTkScrollableFrame(
            history_window,
            fg_color="#F1F5F9",
            corner_radius=12
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # تنظیم حداقل عرض ستون‌های جدول
        for column in range(8):
            table_frame.grid_columnconfigure(
                column,
                weight=1,
                minsize=110
            )

        # عنوان ستون‌ها از چپ به راست
        headers = [
            "شهریه",
            "مدرس",
            "کد دوره",
            "سطح",
            "زبان",
            "شماره موبایل",
            "نام دانش‌آموز",
            "شماره ثبت‌نام"
        ]

        # ایجاد عنوان‌های جدول
        for column, heading in enumerate(headers):

            header_cell = ctk.CTkLabel(
                table_frame,
                text=heading,
                height=45,
                corner_radius=8,
                fg_color="#16324F",
                text_color="#FFFFFF",
                font=("Arial", 13, "bold")
            )

            header_cell.grid(
                row=0,
                column=column,
                padx=3,
                pady=5,
                sticky="nsew"
            )

        # ترجمه نام زبان‌ها برای نمایش به کاربر
        language_names = {
            "English": "انگلیسی",
            "Turkish": "ترکی استانبولی",
            "Spanish": "اسپانیایی"
        }

        # ترجمه سطوح دوره‌ها برای نمایش به کاربر
        level_names = {
            "Beginner": "مبتدی",
            "Intermediate": "متوسط",
            "Advanced": "پیشرفته"
        }

        # بررسی خالی بودن سوابق ثبت‌نام
        if not records:

            empty_label = ctk.CTkLabel(
                table_frame,
                text="هنوز هیچ ثبت‌نامی انجام نشده است.",
                font=("Arial", 16),
                text_color="#64748B"
            )

            empty_label.grid(
                row=1,
                column=0,
                columnspan=8,
                pady=40
            )

        else:

            # بررسی و نمایش تک‌تک ثبت‌نام‌ها
            for row, record in enumerate(records, start=1):

                # جداکردن اطلاعات هر ثبت‌نام
                (
                    registration_id,
                    student_name,
                    student_family,
                    phone,
                    national_id,
                    language,
                    level,
                    course_code,
                    teacher_name,
                    tuition
                ) = record

                # آماده‌کردن اطلاعات برای نمایش در جدول
                row_data = [
                    f"{tuition:,} تومان",
                    teacher_name,
                    str(course_code),
                    level_names.get(level, level),
                    language_names.get(language, language),
                    phone,
                    f"{student_name} {student_family}",
                    str(registration_id)
                ]

                # تغییر رنگ ردیف‌ها برای خوانایی بهتر
                row_color = (
                    "#FFFFFF" if row % 2 == 1 else "#E8EFF7"
                )

                # نمایش اطلاعات هر ستون در ردیف فعلی
                for column, value in enumerate(row_data):

                    cell = ctk.CTkLabel(
                        table_frame,
                        text=value,
                        height=48,
                        corner_radius=6,
                        fg_color=row_color,
                        text_color="#1F2937",
                        font=("Arial", 12),
                        justify="center"
                    )

                    cell.grid(
                        row=row,
                        column=column,
                        padx=3,
                        pady=3,
                        sticky="nsew"
                    )

    # اجرای پنجره
    def run(self):
        self.window.mainloop()
