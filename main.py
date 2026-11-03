# این فایل نقطه شروع برنامه است و اجرای کنترلر و رابط گرافیکی آموزشگاه را بر عهده دارد.

from controller.app_controller import AppController
from view.main_window import MainWindow


def main():
    # ساخت کنترلر
    controller = AppController()

    # ساخت رابط گرافیکی
    app = MainWindow(controller)

    # اجرای برنامه
    app.run()


if __name__ == "__main__":
    main()
