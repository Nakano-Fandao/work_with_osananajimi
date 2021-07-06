import sys, os

add_list = ["detect_modules", "UI", "screens"]
for dir in add_list:
    sys.path.append(os.path.join(os.path.dirname(__file__), dir))

from PySide2.QtWidgets import QApplication

from splash_screen import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
