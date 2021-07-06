import sys, os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

sys.path.append(os.path.join(os.path.dirname(__file__), "../UI"))
from ui_chat_popup import Ui_ChatPopup

class ChatPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ChatPopup()
        self.ui.setupUi(self)
        self.chats = [
            "おはよう",
            "ばいばい",
            "やっほー"
        ]

        self.ui.pushButton_1.clicked.connect(self.play_voice1)

        chat_length = len(self.chats)
        height = 10 + chat_length*95
        self.setGeometry(QRect(300, 100, 540, height))
        for i in range(chat_length-1):
            self.create_text_browser(i)
            self.create_button(i)

    def create_text_browser(self, i):
        y_pos = 10 + 95*(i+1)
        self.ui.textBrowser = QTextBrowser(self)
        self.ui.textBrowser.setObjectName(u"textBrowser")
        self.ui.textBrowser.setGeometry(QRect(10, y_pos, 520, 85))
        self.ui.textBrowser.setStyleSheet(u"QTextBrowser {\n"
            "	background-color: #FFEAC9;\n"
            "	border-radius: 15px;\n"
            "	font-color: #343A40;\n"
            "	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
            "}")

    def create_button(self):
        self.ui.pushButton = QPushButton(self)
        self.ui.pushButton.setObjectName(u"pushButton")
        self.ui.pushButton.setGeometry(QRect(10, y_pos, 520, 85))
        self.ui.pushButton.setStyleSheet(u"QPushButton{background: transparent;}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatPopup()
    window.show()
    sys.exit(app.exec_())
