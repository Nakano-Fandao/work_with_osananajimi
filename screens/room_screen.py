#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QSound

from smapho import DetectSmaphoClass
from detect_chrome import detect_youtube
from play_voice import PlayVoice

## ==> ROOM SCREEN
from ui_room_screen import Ui_RoomScreen
## ==> CHAT POPUP
from ui_chat_popup import Ui_ChatPopup

# ROOM SCREEN
class RoomScreen(QMainWindow):
    def __init__(self, mood, serif):
        QMainWindow.__init__(self)
        self.ui = Ui_RoomScreen()
        self.ui.setupUi(self)
        self.mood = mood
        self.serif = serif
        self.show_serif()

        # カメラオープン！
        self.detect_smapho = DetectSmaphoClass()

        self.osana = PlayVoice()

        ## REMOVE TITLE BAR
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Button setting
        self.ui.serifButton.clicked.connect(self.show_serif)
        self.ui.timerButton.clicked.connect(self.show_timer)
        self.ui.breakButton.clicked.connect(self.show_break)
        self.ui.finishButton.clicked.connect(self.show_finish)

        # タイマースタート！
        self.counter = -10

        # ループスタート！
        self.timer = QTimer()
        self.timer.timeout.connect(self.detect)
        self.timer.start(1500)


    def detect(self):

        if self.counter in set([0, 15]):
            detected = self.detect_smapho.judge_smapho()
            if not detected:
                pass
            else:
                self.serif = self.osana.play_voice(detected, self.mood)
                self.show_serif()

        if self.counter == 30:
            self.counter = 0
            detected = detect_youtube()
            if not detected:
                pass
            else:
                self.serif = self.osana.play_voice(detected, self.mood)
                self.show_serif()

        print(self.counter)
        self.counter += 1


    def change_window(self, index):
        self.ui.windowLabel.setPixmap(QPixmap(u":/image/images/windows/textbox_{}.png".format(index)))

    def show_serif(self):
        self.change_window("serif")
        self.ui.osanaText.setText(self.serif)
        print("Show serif")

    def show_timer(self):
        self.change_window("timer")
        print("Show timer")
        self.chats = [
            "えっ、よかったじゃん…お似合いだよ",
            "嫌だ嫌だ嫌だ",
            "付き合うのか、俺以外の奴と。"
        ]
        QSound.play(":voice/sounds/voices/choicechat_good_4_ask.wav")

        self.popup = ChatPopup(self.chats)
        self.popup.show()

    def show_break(self):
        self.change_window("break")
        print("Show break")

    def show_finish(self):
        sys.exit(-1)


class ChatPopup(QDialog):
    def __init__(self, chats):
        super().__init__()
        self.ui = Ui_ChatPopup()
        self.ui.setupUi(self)
        self.chats = chats
        self.setupChats()

    def setupChats(self):
        chat_length = len(self.chats)
        height = 10 + chat_length*95
        self.setGeometry(QRect(300, 100, 540, height))

        # 1つ目のみ
        self.ui.textBrowser_1.setMarkdown(QCoreApplication.translate("Dialog", self.chats[0], None))
        self.ui.pushButton_1.clicked.connect(self.play_voice1)

        for i in range(chat_length-1):
            self.create_text_browser(i)
            self.create_button(i)

    def create_text_browser(self, i):
        y_pos = 10 + 95*(i+1)
        self.ui.textBrowser = QTextBrowser(self)
        self.ui.textBrowser.setObjectName(u"textBrowser_{}".format(i+2))
        self.ui.textBrowser.setGeometry(QRect(10, y_pos, 520, 85))
        self.ui.textBrowser.setStyleSheet(u"QTextBrowser {\n"
            "	background-color: #FFEAC9;\n"
            "	border-radius: 15px;\n"
            "	color: #343A40;\n"
            "	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
            "}")
        self.ui.textBrowser.setMarkdown(QCoreApplication.translate("Dialog", self.chats[i+1], None))
        print(locals())
        # self.ui.pushButton.clicked.connect(self.play_voice2)

    def create_button(self, i):
        y_pos = 10 + 95*(i+1)
        self.ui.pushButton = QPushButton(self)
        self.ui.pushButton.setObjectName(u"pushButton_{}".format(i+2))
        self.ui.pushButton.setGeometry(QRect(10, y_pos, 520, 85))
        self.ui.pushButton.setStyleSheet(u"QPushButton{background: transparent;}")



    def play_voice1(self):
        print(locals())
        print(globals())
        self.close()
        QSound.play(":voice/sounds/voices/choicechat_good_4_a.wav")

    def play_voice2(self):
        self.close()
        QSound.play(":voice/sounds/voices/choicechat_good_4_b.wav")

    def play_voice3(self):
        self.close()
        QSound.play(":voice/sounds/voices/choicechat_good_4_c.wav")
