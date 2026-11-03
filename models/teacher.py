
from models.person import Person


class Teacher(Person):
    """اطلاعات معلمان آموزشگاه"""

    # زبان‌های مجاز برای تدریس
    ALLOWED_LANGUAGES = ["English", "Turkish", "Spanish"]

    # سطح‌های مجاز برای تدریس
    ALLOWED_LEVELS = ["Beginner", "Intermediate", "Advanced"]

    def __init__(self, name, family, phone, national_id, language, levels):

        # دریافت اطلاعات اولیه از کلاس پدر
        super().__init__(name, family, phone, national_id)

        # تنظیم زبان و سطح‌های تدریس معلم
        self.language = language
        self.levels = levels

    # -------------------- language --------------------

    @property
    def language(self):
        """دریافت زبان تدریس معلم"""
        return self.__language

    @language.setter
    def language(self, new_language):

        # بررسی متنی بودن زبان
        if not isinstance(new_language, str):
            raise TypeError("نام زبان باید متنی باشد.")

        # حذف فاصله‌های اضافی و یکسان‌سازی حروف
        new_language = new_language.strip().capitalize()

        # بررسی ارائه شدن زبان در آموزشگاه
        if new_language not in self.ALLOWED_LANGUAGES:
            raise ValueError("این زبان در آموزشگاه ارائه نمی‌شود.")

        # ذخیره زبان معتبر
        self.__language = new_language

    # -------------------- levels --------------------

    @property
    def levels(self):
        """دریافت سطح‌های قابل تدریس معلم"""
        return self.__levels

    @levels.setter
    def levels(self, new_levels):

        # بررسی فهرست بودن سطح‌های تدریس
        if not isinstance(new_levels, list):
            raise TypeError("سطح‌های تدریس باید به‌صورت فهرست باشند.")

        # جلوگیری از خالی بودن فهرست سطح‌ها
        if not new_levels:
            raise ValueError("حداقل یک سطح تدریس باید انتخاب شود.")

        # فهرست نگهداری سطح‌های معتبر
        clean_levels = []

        # بررسی تک‌تک سطح‌های واردشده
        for level in new_levels:

            # بررسی متنی بودن سطح
            if not isinstance(level, str):
                raise TypeError("هر سطح تدریس باید متنی باشد.")

            # حذف فاصله‌های اضافی و یکسان‌سازی حروف
            level = level.strip().capitalize()

            # بررسی مجاز بودن سطح تدریس
            if level not in self.ALLOWED_LEVELS:
                raise ValueError("این سطح آموزشی مجاز نیست.")

            # جلوگیری از ثبت سطح تکراری
            if level in clean_levels:
                raise ValueError("انتخاب سطح تکراری مجاز نیست.")

            # اضافه کردن سطح معتبر به فهرست
            clean_levels.append(level)

        # ذخیره فهرست سطح‌های معتبر
        self.__levels = clean_levels

    # -------------------- introduce --------------------

    def introduce(self):

        # نمایش اطلاعات پایه معلم از طریق کلاس پدر
        super().introduce()

        # نمایش زبان و سطح‌های تدریس معلم
        print(f"زبان تدریس: {self.language}")
        print(f"سطح‌های قابل تدریس: {self.levels}")

    # -------------------- repr --------------------

    def __repr__(self):

        # نمایش اطلاعات معلم برای بررسی و اشکال‌زدایی
        return (
            f"Teacher(name={self.name!r}, "
            f"family={self.family!r}, "
            f"phone={self.phone!r}, "
            f"language={self.language!r}, "
            f"levels={self.levels!r})"
        )
