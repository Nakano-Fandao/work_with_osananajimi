import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "detect_modules"))
sys.path.append(os.path.join(os.path.dirname(__file__), "UI"))
sys.path.append(os.path.join(os.path.dirname(__file__), "screens"))

from PySide2.QtWidgets import QApplication

from splash_screen import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
