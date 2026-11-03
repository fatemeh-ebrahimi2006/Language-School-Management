# این فایل کلاس پایه Person را برای نگهداری و اعتبارسنجی اطلاعات مشترک افراد تعریف می‌کند.

from persian_tools import national_id as national_id_tools
from persian_tools import phone_number as phone_number_tools

class Person :
    """اطلاعات مشترک افراد اموزشگاه"""
    def __init__(self,name,family,phone,national_id):

        self.name = name
        self.family = family
        self.phone = phone
        self.__validate_national_id(national_id)
        self.__national_id = national_id

    #________________name___________________

    @property
    def name(self):
        return self.__name

    # اعتبارسنجی و تنظیم نام
    @name.setter
    def name(self, new_name):

        # بررسی متنی بودن نام
        if not isinstance(new_name, str):
            raise TypeError("نام باید متن باشد.")

        # حذف فاصله‌های ابتدا و انتهای نام
        new_name = new_name.strip()

        # جلوگیری از خالی بودن نام
        if not new_name:
            raise ValueError("وارد کردن نام الزامی است.")

        # بررسی وجود حروف فارسی
        has_persian = any(
            '\u0600' <= char <= '\u06FF' and char.isalpha()
            for char in new_name
        )

        # بررسی وجود حروف انگلیسی
        has_english = any(
            char.isascii() and char.isalpha()
            for char in new_name
        )

        # جلوگیری از ترکیب فارسی و انگلیسی
        if has_persian and has_english:
            raise ValueError(
                "نام را فقط فارسی یا فقط انگلیسی وارد کنید."
            )

        # اجازه استفاده از حروف و فاصله
        if not all(
            char == " " or
            (char.isascii() and char.isalpha()) or
            ('\u0600' <= char <= '\u06FF' and char.isalpha())
            for char in new_name
        ):
            raise ValueError(
                "نام نباید شامل عدد یا علامت باشد."
            )

        # ذخیره نام معتبر
        self.__name = new_name

    #________________family___________________

    @property
    def family(self):
        return self.__family

    # اعتبارسنجی و تنظیم نام خانوادگی
    @family.setter
    def family(self, new_family):

        # بررسی متنی بودن نام خانوادگی
        if not isinstance(new_family, str):
            raise TypeError("نام خانوادگی باید متن باشد.")

        # حذف فاصله‌های ابتدا و انتهای نام خانوادگی
        new_family = new_family.strip()

        # جلوگیری از خالی بودن نام خانوادگی
        if not new_family:
            raise ValueError("وارد کردن نام خانوادگی الزامی است.")

        # بررسی وجود حروف فارسی
        has_persian = any(
            '\u0600' <= char <= '\u06FF' and char.isalpha()
            for char in new_family
        )

        # بررسی وجود حروف انگلیسی
        has_english = any(
            char.isascii() and char.isalpha()
            for char in new_family
        )

        # جلوگیری از ترکیب فارسی و انگلیسی
        if has_persian and has_english:
            raise ValueError(
                "نام خانوادگی را فقط فارسی یا فقط انگلیسی وارد کنید."
            )

        # اجازه استفاده از حروف و فاصله
        if not all(
            char == " " or
            (char.isascii() and char.isalpha()) or
            ('\u0600' <= char <= '\u06FF' and char.isalpha())
            for char in new_family
        ):
            raise ValueError(
                "نام خانوادگی نباید شامل عدد یا علامت باشد."
            )

        # ذخیره نام خانوادگی معتبر
        self.__family = new_family

    #________________phone___________________

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):

        if not isinstance(new_phone, str):
            raise TypeError("شماره موبایل باید متن باشد")

        if (
                len(new_phone) != 11
                or not new_phone.isascii()
                or not new_phone.isdigit()
                or not new_phone.startswith("09")
        ):
            raise ValueError(
                "شماره موبایل باید ۱۱ رقم انگلیسی و با ۰۹ شروع شود."
            )

        if not phone_number_tools.validate(new_phone):
            raise ValueError("شماره موبایل وارد شده معتبر نیست")

        self.__phone = new_phone

    #________________national_id___________________

    @staticmethod
    def __validate_national_id(national_id):

        if not isinstance(national_id, str):
            raise TypeError("کد ملی باید متن باشدgit diff --check")

        if (
                len(national_id) != 10
                or not national_id.isascii()
                or not national_id.isdigit()
        ):
            raise ValueError(
                "کد ملی باید 10 رقم باشد"
            )

        if not national_id_tools.validate(national_id):
            raise ValueError("کد ملی واردشده معتبر نیست.")

        return national_id
    @property
    def national_id(self):
        return self.__national_id

    #______________introduce__________________

    def introduce(self):
        print(f"Name: {self.name} {self.family}")
        print(f"Phone: {self.phone}")

    #______________repr_______________________

    def __repr__(self):
        return (
            f"Person(name={self.name!r}, "
            f"family={self.family!r}, "
            f"phone={self.phone!r})"
        )
