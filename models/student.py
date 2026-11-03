
from models.person import Person


class Student(Person):
    """اطلاعات زبان‌آموز آموزشگاه"""

    def __init__(self, name, family, phone, national_id, languages, language_levels):

        # دریافت اطلاعات اولیه از کلاس پدر
        super().__init__(name, family, phone, national_id)

        # تنظیم زبان‌ها و سطح‌های آموزشی
        self.languages = languages
        self.language_levels = language_levels

        # بررسی تطابق تعداد زبان‌ها و سطح‌های آن‌ها
        if len(self.languages) != len(self.language_levels):
            raise ValueError("هر زبان باید یک سطح داشته باشد.")

    # -------------------- languages --------------------

    @property
    def languages(self):
        """دریافت زبان‌های دانش‌آموز"""
        return self.__languages

    @languages.setter
    def languages(self, new_languages):

        # بررسی فهرست بودن زبان‌های انتخاب‌شده
        if not isinstance(new_languages, list):
            raise TypeError("زبان‌ها باید به‌صورت فهرست باشند.")

        # جلوگیری از خالی بودن فهرست زبان‌ها
        if not new_languages:
            raise ValueError("حداقل یک زبان باید انتخاب شود.")

        # جلوگیری از انتخاب زبان تکراری
        if len(new_languages) != len(set(new_languages)):
            raise ValueError("انتخاب زبان تکراری مجاز نیست.")

        # زبان‌های مجاز آموزشگاه
        allowed_languages = ["English", "Turkish", "Spanish"]

        # بررسی معتبر بودن هر زبان
        for language in new_languages:

            # بررسی متنی بودن نام زبان
            if not isinstance(language, str):
                raise TypeError("نام زبان باید متنی باشد.")

            # بررسی ارائه شدن زبان در آموزشگاه
            if language not in allowed_languages:
                raise ValueError("این زبان در آموزشگاه ارائه نمی‌شود.")

        # ذخیره زبان‌های معتبر
        self.__languages = new_languages

    # -------------------- language levels --------------------

    @property
    def language_levels(self):
        """دریافت سطح‌های آموزشی دانش‌آموز"""
        return self.__language_levels

    @language_levels.setter
    def language_levels(self, new_levels):

        # بررسی فهرست بودن سطح‌های آموزشی
        if not isinstance(new_levels, list):
            raise TypeError("سطح‌های زبان باید به‌صورت فهرست باشند.")

        # جلوگیری از خالی بودن فهرست سطح‌ها
        if not new_levels:
            raise ValueError("حداقل یک سطح زبان باید انتخاب شود.")

        # فهرست نگهداری سطح‌های معتبر
        clean_levels = []

        # بررسی تک‌تک سطح‌های آموزشی
        for level in new_levels:

            # بررسی متنی بودن سطح
            if not isinstance(level, str):
                raise TypeError("سطح زبان باید متنی باشد.")

            # حذف فاصله‌های اضافی و یکسان‌سازی حروف
            level = level.strip().lower()

            # سطح‌های مجاز آموزشگاه
            if level not in ["beginner", "intermediate", "advanced"]:
                raise ValueError("این سطح آموزشی در دسترس نیست.")

            # ذخیره سطح با حرف اول بزرگ
            clean_levels.append(level.capitalize())

        # ذخیره فهرست سطح‌های معتبر
        self.__language_levels = clean_levels

    # -------------------- language count --------------------

    @property
    def language_count(self):
        """تعداد زبان‌های دانش‌آموز"""
        return len(self.languages)

    # -------------------- introduce --------------------

    def introduce(self):

        # نمایش اطلاعات پایه از طریق کلاس پدر
        super().introduce()

        # نمایش زبان‌ها و سطح‌های آموزشی
        print(f"زبان‌ها: {self.languages}")
        print(f"تعداد زبان‌ها: {self.language_count}")
        print(f"سطح‌های زبان: {self.language_levels}")

    # -------------------- repr --------------------

    def __repr__(self):

        # نمایش اطلاعات دانش‌آموز به شکل قابل شناسایی
        return (
            f"Student(name={self.name!r}, "
            f"family={self.family!r}, "
            f"phone={self.phone!r}, "
            f"languages={self.languages!r}, "
            f"language_count={self.language_count!r}, "
            f"language_levels={self.language_levels!r})"
        )
