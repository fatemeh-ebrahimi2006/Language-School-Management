# این فایل عملکرد AppController و ارتباط آن با بخش‌های مختلف برنامه را آزمایش می‌کند.

from controller.app_controller import AppController


# ساخت کنترلر
controller = AppController()


# دریافت دوره‌های انگلیسی
english_courses = controller.get_courses_by_language("English")

print("English Courses:")

for course in english_courses:
    print(course)


# دریافت دوره‌های ترکی
turkish_courses = controller.get_courses_by_language("Turkish")

print("\nTurkish Courses:")

for course in turkish_courses:
    print(course)


# دریافت سوابق ثبت نام
registrations = controller.get_all_registrations()

print("\nRegistration History:")
for registration in registrations:
    print(registration)
