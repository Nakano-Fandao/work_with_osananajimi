from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QSound

from ui_chat_popup import Ui_Dialog

class ChatPopup(QDialog):
    def __init__(self, chats):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.chats = chats

        self.ui.pushButton.clicked.connect(self.play_voice1)
        self.ui.pushButton_2.clicked.connect(self.play_voice2)
        self.ui.pushButton_3.clicked.connect(self.play_voice3)


#         chat_length = len(self.chats)
#         height = 10 + chat_length*95
#         self.ui.resize(height, 105)
#         for i in range(chat_length-1):
#             self.create_text_browser(i)


#     def create_text_browser(self, i):
#         y_pos = 10 + 95*(i+1)
#         self.ui.textBrowser = QTextBrowser(self.ui)
#         self.ui.textBrowser.setObjectName(u"textBrowser")
#         self.ui.textBrowser.setGeometry(QRect(10, y_pos, 520, 85))
#         self.ui.textBrowser.setStyleSheet(u"QTextBrowser {\n"
# "	background-color: #FFEAC9;\n"
# "	border-radius: 15px;\n"
# "	font-color: #343A40;\n"
# "	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
# "}")
#         self.ui.pushButton = QPushButton(self.ui)
#         self.ui.pushButton.setObjectName(u"pushButton")
#         self.ui.pushButton.setGeometry(QRect(10, y_pos, 520, 85))
#         self.ui.pushButton.setStyleSheet(u"QPushButton{background: transparent;}")

    def play_voice1(self):
        self.close()
        QSound.play(":voice/sounds/voices/choicechat_good_4_a.wav")

    def play_voice2(self):
        self.close()
        QSound.play(":voice/sounds/voices/choicechat_good_4_b.wav")

    def play_voice3(self):
        self.close()
        QSound.play(":voice/sounds/voices/choicechat_good_4_c.wav")
