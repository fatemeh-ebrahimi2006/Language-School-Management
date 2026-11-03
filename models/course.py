from models.teacher import Teacher
#این کلاس اطلاعات یه دوره را نگه میدارد
class Course :
    """اطلاعات دوره اموزشی"""

    ALLOWED_LANGUAGES = ["English", "Turkish", "Spanish"]
    ALLOWED_LEVELS = ["Beginner", "Intermediate", "Advanced"]

    def __init__(self,code, language, level, teacher, tuition):
        self.code = code
        self.language = language
        self.level = level
        self.teacher = teacher
        self.tuition = tuition

    #________________code____________________

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, new_code):
        if not isinstance(new_code,int) or isinstance(new_code,bool):
            raise TypeError("Course code must be integer!!!")

        if new_code <= 0 :
            raise ValueError("Course code must be positive!!!")

        self.__code = new_code

    #______________________language___________________

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self,new_language):
        if not isinstance(new_language,str):
            raise TypeError("Language must be string!!!")

        new_language = new_language.strip().lower().capitalize()

        if new_language not in self.ALLOWED_LANGUAGES :
            raise ValueError("This language is not available.")

        self.__language = new_language

    #______________________level_________________________

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self,new_level):
        if not isinstance(new_level,str):
            raise TypeError("Level must be string!!!")

        new_level = new_level.strip().lower().capitalize()

        if new_level not in self.ALLOWED_LEVELS :
            raise ValueError("This level is not available.")

        self.__level = new_level

    #______________________teacher______________________

    @property
    def teacher(self):
        return self.__teacher


    @teacher.setter
    def teacher(self, new_teacher):
        if not isinstance(new_teacher, Teacher):
            raise TypeError("Teacher must be a Teacher object.")

        if new_teacher.language != self.language:
            raise ValueError(
                "Teacher's language must match the course language."
            )

        if self.level not in new_teacher.levels:
            raise ValueError(
                "Teacher cannot teach this course level."
            )

        self.__teacher = new_teacher

    #______________________tuition_____________________

    @property
    def tuition(self):
        return self.__tuition

    @tuition.setter
    def tuition(self,new_tuition):
        if not isinstance(new_tuition,(int,float)) or isinstance(new_tuition,bool):
            raise TypeError("Tuition must be a number!!!")

        if new_tuition < 0 :
            raise ValueError("Tuition cannot be negative!!!")

        self.__tuition = new_tuition

    #_______________repr____________________

    def __repr__(self):
        return (
            f"Course(code={self.code!r}, "
            f"language={self.language!r}, "
            f"level={self.level!r}, "
            f"teacher={self.teacher!r}, "
            f"tuition={self.tuition!r})"
        )
