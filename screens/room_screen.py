#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

add_list = ["../detect_modules", "../UI", "../screens"]
for dir in add_list:
    sys.path.append(os.path.join(os.path.dirname(__file__), dir))

from smapho import DetectSmaphoClass
from detect_chrome import detect_youtube
from play_voice import PlayVoice

## ==> ROOM SCREEN
from ui_room_screen import Ui_RoomScreen
## ==> CHAT POPUP
from chat_popup import ChatPopup
from log_popup import LogPopup

# ROOM SCREEN
class RoomScreen(QMainWindow):
    def __init__(self, parameter, serif):
        QMainWindow.__init__(self)
        self.ui = Ui_RoomScreen()
        self.ui.setupUi(self)
        self.parameter = parameter
        self.serif_list = []
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
        self.ui.logButton.clicked.connect(self.show_log)

        # タイマースタート！
        self.counter = -10

        # ループスタート！
        self.timer = QTimer()
        self.timer.timeout.connect(self.detect)
        self.timer.start(500)


    def detect(self):

        if self.counter in set([0, 15]):
            detected = self.detect_smapho.judge_smapho()
            if not detected:
                pass
            else:
                self.serif = self.osana.play_voice(detected, self.parameter)
                self.show_serif()
                self.parameter -= 10

        if self.counter == 30:
            self.counter = 0
            detected = detect_youtube()
            if not detected:
                pass
            else:
                self.serif = self.osana.play_voice(detected, self.parameter)
                self.show_serif()
                self.parameter -= 10

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

        self.chat_popup = ChatPopup(user_reply_list)
        if self.chat_popup.exec_() == QDialog.Accepted:
            #* 世間話popup表示
            self.chat_popup.show()

            #* 世間話popupから返ってくる
            user_reply = self.chat_popup.selected_item

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
        self.ui.osanaText.show()
        self.ui.logButton.show()
        self.ui.osanaText.setText(self.serif)
        self.serif_list.append(self.serif)
        print("Show serif")

    def show_timer(self):
        self.change_window("timer")
        self.ui.osanaText.hide()
        self.ui.logButton.hide()
        print("Show timer")

        self.do_choicechat()

    def show_break(self):
        self.ui.osanaText.hide()
        self.ui.logButton.hide()
        self.change_window("break")
        print("Show break")

    def show_finish(self):
        sys.exit(-1)

    def show_log(self):
        self.log_popup = LogPopup(self.serif_list)
        self.log_popup.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    parameter = 50
    serif = "ぷっ、なにそれ。そもそも付き合う気なかったよ。あっ、安心してる？ふふ、ぜーんぶお見通しってわけｗ"
    window = RoomScreen(parameter, serif)
    window.show()
    sys.exit(app.exec_())
