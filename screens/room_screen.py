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
from json_files import JsonFiles

## ==> ROOM SCREEN
from ui_room_screen import Ui_RoomScreen
## ==> CHAT POPUP
from ui_chat_popup import Ui_ChatPopup

# ROOM SCREEN
class RoomScreen(QMainWindow):
    def __init__(self, parameter, serif):
        QMainWindow.__init__(self)
        self.ui = Ui_RoomScreen()
        self.ui.setupUi(self)
        self.parameter = parameter
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
                self.serif = self.osana.play_voice(detected, self.parameter)
                self.show_serif()

        if self.counter == 30:
            self.counter = 0
            detected = detect_youtube()
            if not detected:
                pass
            else:
                self.serif = self.osana.play_voice(detected, self.parameter)
                self.show_serif()

        print(self.counter)
        self.counter += 1

    def do_choicechat(self):

        self.serif, choicechat_detail = self.osana.play_choicechat_ask(self.parameter)
        self.show_serif()

        user_reply_list = choicechat_detail["user_reply"]
        osana_reply_list = choicechat_detail["osana_reply"]
        point_list = choicechat_detail["point"]

        if self.serif == "お腹すいたな～あたしが何か作るよ！なに食べたい？":
            osana_reply_list = (osana_reply_list[0], osana_reply_list[1])[self.parameter > 55]
            point_list = (point_list[0], point_list[1])[self.parameter > 55]

        self.popup = ChatPopup(user_reply_list)
        if self.popup.exec_()== QDialog.Accepted:
            self.popup.show()
            user_reply = self.popup.selected_item

        index = user_reply_list.index(user_reply)
        self.serif = osana_reply_list[index]
        self.show_serif()
        point = point_list[index]
        self.osana.play_choicechat_reply(self.serif)
        self.parameter += point


    def change_window(self, index):
        self.ui.windowLabel.setPixmap(QPixmap(u":/image/images/windows/textbox_{}.png".format(index)))

    def show_serif(self):
        self.change_window("serif")
        self.ui.osanaText.setText(self.serif)
        print("Show serif")

    def show_timer(self):
        self.change_window("timer")
        print("Show timer")

        self.do_choicechat()

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

        self.ui.chatList.clicked.connect(self.accept)

    def setupChats(self):
        chat_length = len(self.chats)
        height = 10 + chat_length*95
        self.setGeometry(QRect(300, 100, 540, height))
        for i in range(chat_length):
            QListWidgetItem(self.ui.chatList)
            chatItem = self.ui.chatList.item(i)
            chatItem.setText(QCoreApplication.translate("ChatPopup", self.chats[i], None));

    @property
    def selected_item(self):
        self.close()
        item = self.ui.chatList.selectedItems()[0].text()
        return ("", item)[item != ""]
