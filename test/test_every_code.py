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