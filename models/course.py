# این فایل کلاس Course را برای نگهداری اطلاعات دوره، معلم، سطح و شهریه تعریف می‌کند.

from models.teacher import Teacher


class Course:
    """اطلاعات دوره آموزشی آموزشگاه"""

    # زبان‌های مجاز آموزشگاه
    ALLOWED_LANGUAGES = ["English", "Turkish", "Spanish"]

    # سطح‌های مجاز آموزشی
    ALLOWED_LEVELS = ["Beginner", "Intermediate", "Advanced"]

    def __init__(self, code, language, level, teacher, tuition):

        # تنظیم اطلاعات اولیه دوره از طریق ویژگی‌ها
        self.code = code
        self.language = language
        self.level = level
        self.teacher = teacher
        self.tuition = tuition

    # -------------------- code --------------------

    @property
    def code(self):
        """دریافت کد دوره"""
        return self.__code

    @code.setter
    def code(self, new_code):

        # بررسی عدد صحیح بودن کد دوره
        if not isinstance(new_code, int) or isinstance(new_code, bool):
            raise TypeError("کد دوره باید عدد صحیح باشد.")

        # جلوگیری از کدهای صفر و منفی
        if new_code <= 0:
            raise ValueError("کد دوره باید عددی مثبت باشد.")

        # ذخیره کد معتبر
        self.__code = new_code

    # -------------------- language --------------------

    @property
    def language(self):
        """دریافت زبان دوره"""
        return self.__language

    @language.setter
    def language(self, new_language):

        # بررسی متنی بودن نام زبان
        if not isinstance(new_language, str):
            raise TypeError("نام زبان باید متنی باشد.")

        # حذف فاصله‌های اضافی و یکسان‌سازی حروف
        new_language = new_language.strip().lower().capitalize()

        # بررسی ارائه شدن زبان در آموزشگاه
        if new_language not in self.ALLOWED_LANGUAGES:
            raise ValueError("این زبان در آموزشگاه ارائه نمی‌شود.")

        # ذخیره زبان معتبر
        self.__language = new_language

    # -------------------- level --------------------

    @property
    def level(self):
        """دریافت سطح دوره"""
        return self.__level

    @level.setter
    def level(self, new_level):

        # بررسی متنی بودن سطح دوره
        if not isinstance(new_level, str):
            raise TypeError("سطح دوره باید متنی باشد.")

        # حذف فاصله‌های اضافی و یکسان‌سازی حروف
        new_level = new_level.strip().lower().capitalize()

        # بررسی معتبر بودن سطح آموزشی
        if new_level not in self.ALLOWED_LEVELS:
            raise ValueError("این سطح آموزشی در دسترس نیست.")

        # ذخیره سطح معتبر
        self.__level = new_level

    # -------------------- teacher --------------------

    @property
    def teacher(self):
        """دریافت معلم دوره"""
        return self.__teacher

    @teacher.setter
    def teacher(self, new_teacher):

        # بررسی اینکه ورودی یک شیء از کلاس Teacher باشد
        if not isinstance(new_teacher, Teacher):
            raise TypeError("معلم باید یک شیء از کلاس Teacher باشد.")

        # بررسی تطابق زبان معلم با زبان دوره
        if new_teacher.language != self.language:
            raise ValueError(
                "زبان تدریس معلم باید با زبان دوره یکسان باشد."
            )

        # بررسی توانایی معلم برای تدریس سطح انتخاب‌شده
        if self.level not in new_teacher.levels:
            raise ValueError(
                "این معلم توانایی تدریس سطح انتخاب‌شده را ندارد."
            )

        # ذخیره معلم معتبر
        self.__teacher = new_teacher

    # -------------------- tuition --------------------

    @property
    def tuition(self):
        """دریافت شهریه دوره"""
        return self.__tuition

    @tuition.setter
    def tuition(self, new_tuition):

        # بررسی عددی بودن شهریه و جلوگیری از پذیرش مقدار بولی
        if (
            not isinstance(new_tuition, (int, float))
            or isinstance(new_tuition, bool)
        ):
            raise TypeError("شهریه باید یک عدد باشد.")

        # جلوگیری از شهریه منفی
        if new_tuition < 0:
            raise ValueError("شهریه نمی‌تواند منفی باشد.")

        # ذخیره شهریه معتبر
        self.__tuition = new_tuition

    # -------------------- repr --------------------

    def __repr__(self):

        # نمایش اطلاعات دوره برای بررسی و اشکال‌زدایی
        return (
            f"Course(code={self.code!r}, "
            f"language={self.language!r}, "
            f"level={self.level!r}, "
            f"teacher={self.teacher!r}, "
            f"tuition={self.tuition!r})"
        )
