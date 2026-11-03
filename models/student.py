from models.person import Person


class Student(Person):
    """اطلاعات زبان اموز اموزشگاه"""
    def __init__(self,name,family,phone,national_id,languages,language_levels):
        super().__init__(name,family,phone,national_id)

        self.languages = languages
        self.language_levels = language_levels

        if len(self.languages) != len(self.language_levels):
            raise ValueError("Each language must have one level.")

    #_________________language___________________

    @property
    def languages(self):
        return self.__languages

    @languages.setter
    def languages(self, new_languages):

        if not isinstance(new_languages,list):
            raise TypeError("languages must be a list!!!")

        if not new_languages :
            raise ValueError("At least one language must be selected.")
        #شرط زیر برای تکراری انتخاب نکردن زبان
        if len(new_languages) != len(set(new_languages)):
            raise ValueError("Duplicate languages are not allowed.")

        allowed_languages = ["English", "Turkish", "Spanish"]

        for language in new_languages:
            if not isinstance(language, str):
                raise TypeError("Language must be a string.")

            if language not in allowed_languages:
                raise ValueError("This language is not available.")

        self.__languages = new_languages

    #_________________language levels___________________

    @property
    def language_levels(self):
        return self.__language_levels

    @language_levels.setter
    def language_levels(self, new_levels):
        if not isinstance(new_levels,list):
            raise TypeError("language levels must be a list!!!")

        if not new_levels :
            raise ValueError("At least one language level must be selected.")

        clean_levels = []

        for level in new_levels:
            if not isinstance(level,str):
                raise TypeError("Language level must be a string.")

            level = level.strip().lower()

            if level not in ["beginner", "intermediate", "advanced"]:
                raise ValueError("This language level is not available!!!")

            clean_levels.append(level.capitalize())

        self.__language_levels = clean_levels

    #______________________language count_______________________

    @property
    def language_count(self):
        return len(self.languages)

    #_______________________introduce____________________________

    def introduce(self):
        super().introduce()
        print(f"Languages: {self.languages}")
        print(f"Language count: {self.language_count}")
        print(f"Language levels: {self.language_levels}")

    #______________repr_______________________

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"family={self.family!r}, "
            f"phone={self.phone!r}, "
            f"languages={self.languages!r}, "
            f"language_count={self.language_count!r}, "
            f"language_levels={self.language_levels!r})"
        )
