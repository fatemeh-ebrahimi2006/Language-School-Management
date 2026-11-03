from models.person import Person

class Teacher(Person):
    """اطلاعات اساتید اموزشگاه"""
    ALLOWED_LANGUAGES = ["English", "Turkish", "Spanish"]
    ALLOWED_LEVELS = ["Beginner", "Intermediate", "Advanced"]

    def __init__(self,name,family,phone,national_id,language,levels):
        super().__init__(name,family,phone,national_id)

        self.language = language
        self.levels = levels

    #_________________language_______________________

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language):
        if not isinstance(new_language,str):
            raise TypeError("language must be a string!!!")

        new_language = new_language.strip().capitalize()

        if new_language not in self.ALLOWED_LANGUAGES:
            raise ValueError("This language is not available.")

        self.__language = new_language

    #__________________levels_____________________

    @property
    def levels(self):
        return self.__levels

    @levels.setter
    def levels(self, new_levels):
        if not isinstance(new_levels,list):
            raise TypeError("levels must be a list!!!")

        if not new_levels:
            raise ValueError("At least one level must be selected.")

        clean_levels = []

        for level in new_levels:
             if not isinstance(level, str):
                raise TypeError("Each level must be a string.")

             level = level.strip().lower().capitalize()

             #بررسی می‌کنه سطح واردشده یکی از این سه مورد باشه: Beginner، Intermediate یا Advanced.
             if level not in self.ALLOWED_LEVELS:
                raise ValueError("This language level is not available.")

             #اگر سطحی قبلاً به لیست بررسی‌شده اضافه شده باشه، از تکرار اون جلوگیری می‌کنه.
             if level in clean_levels:
               raise ValueError("Duplicate levels are not allowed.")

             clean_levels.append(level)

        self.__levels = clean_levels

    # ___________________introduce_____________________

    def introduce(self):
        super().introduce()
        print(f"Language: {self.language}")
        print(f"Levels: {self.levels}")

    # ____________________repr_______________________

    def __repr__(self):
        return (
            f"Teacher(name={self.name!r}, "
            f"family={self.family!r}, "
            f"phone={self.phone!r}, "
            f"language={self.language!r}, "
            f"levels={self.levels!r})"
        )
