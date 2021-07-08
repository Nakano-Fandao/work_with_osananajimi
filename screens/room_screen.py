#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QSound

add_list = ["../detect_modules", "../UI", "../settings", "../screens"]
for dir in add_list:
    sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), dir)))

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

        self.ui.logView.hide()
        self.ui.blackFrame.hide()
        self.ui.returnButton.hide()

        # Model作成
        self.model = QStringListModel()
        self.model.setStringList(self.serif_list)
        self.ui.logView.setModel(self.model)

        # Signal-Slot作成
        self.ui.logView.clicked.connect(self.logView_clicked)

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
        self.ui.returnButton.clicked.connect(self.return_log)

        # タイマースタート！
        self.counter = -10

        # ループスタート！
        self.timer = QTimer()
        self.timer.timeout.connect(self.detect)
        self.timer.start(500)

        self.show()

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
        self.ui.finishLabel.hide()
        self.ui.finishButton.hide()
        self.ui.logButton.hide()

        self.model.setStringList(self.serif_list)
        self.ui.logView.setModel(self.model)

        # 紙をめくる音
        QSound.play(":effect/sounds/effects/paper_flipping.wav")

        self.log_flag = True
        self.get_geometry()

        # タイマースタート！
        self.ui.logView.show()
        self.ui.blackFrame.show()
        self.STAGE_NUMBER = 64 # 分割回数（多いほど滑らか）
        self.interval = 1
        self.move_counter = 1
        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.move_log)
        self.move_timer.start(1)

    def return_log(self):

        # 紙をめくる音
        QSound.play(":effect/sounds/effects/paper_flipping.wav")

        self.log_flag = False
        self.get_geometry()

        # タイマースタート！
        self.ui.returnButton.hide()
        self.STAGE_NUMBER = 64 # 分割回数（多いほど滑らか）
        self.interval = 1
        self.move_counter = 1
        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.move_log)
        self.move_timer.start(1)

    def get_geometry(self):
        #* --------------------before-----------------after--------
        blackFrame   = [[  0,   0,   0,   0], [  0,   0,   0, 0.4]]
        osanaLabel   = [[220,  40, 370, 470], [ 20,  60, 370, 470]]
        logView      = [[610, 390, 160, 170], [370,  90, 400, 430]]
        windowLabel  = [[ 20, 405, 760, 182], [ 20, 525, 760, 182]]
        osanaText    = [[ 30, 470, 740, 105], [ 30, 590, 740, 105]]
        serifButton  = [[ 20, 410, 140,  45], [ 20, 530, 140,  45]]
        timerButton  = [[160, 410, 140,  45], [ 20, 530, 140,  45]]
        breakButton  = [[300, 410, 140,  45], [ 20, 530, 140,  45]]
        finishButton = [[630, 410, 140,  45], [ 20, 670, 140,  45]]
        #* --------------------------------------------------------
        if not self.log_flag:
            blackFrame.reverse()
            osanaLabel.reverse()
            logView.reverse()
            windowLabel.reverse()
            osanaText.reverse()
            serifButton.reverse()
            timerButton.reverse()
            breakButton.reverse()
            finishButton.reverse()

        self.geometry_lists = [blackFrame]+[osanaLabel]+[logView]+[windowLabel]+[osanaText]+[serifButton]+[timerButton]+[breakButton]+[finishButton]

    def move_log(self):

        current_geometry = []
        for i, (before, after) in enumerate(self.geometry_lists):
            x = (before[0] - after[0]) / self.STAGE_NUMBER
            y = (before[1] - after[1]) / self.STAGE_NUMBER
            w = (before[2] - after[2]) / self.STAGE_NUMBER
            h = (before[3] - after[3]) / self.STAGE_NUMBER
            if i != 0:
                current_geometry.append(QRect(
                    int(before[0] - x*self.move_counter),
                    int(before[1] - y*self.move_counter),
                    int(before[2] - w*self.move_counter),
                    int(before[3] - h*self.move_counter)
                ))
            else:
                t_val = round(before[3] - h*self.move_counter, 2)
                current_geometry.append("QFrame {background-color: rgba(0, 0, 0, " + str(t_val) + ");}")

        self.ui.blackFrame.setStyleSheet(current_geometry[0])
        self.ui.osanaLabel.setGeometry(current_geometry[1])
        self.ui.logView.setGeometry(current_geometry[2])
        self.ui.windowLabel.setGeometry(current_geometry[3])
        self.ui.osanaText.setGeometry(current_geometry[4])
        self.ui.serifButton.setGeometry(current_geometry[5])
        self.ui.timerButton.setGeometry(current_geometry[6])
        self.ui.breakButton.setGeometry(current_geometry[7])
        self.ui.finishButton.setGeometry(current_geometry[8])

        if self.move_counter == self.STAGE_NUMBER:
            self.move_timer.stop()
            if self.log_flag:
                self.ui.returnButton.show()
            else:
                self.ui.logView.hide()
                self.ui.finishLabel.show()
                self.ui.finishButton.show()
                self.ui.logButton.show()
                self.ui.blackFrame.hide()

        self.move_counter += 1

    def logView_clicked(self, index):
        # 選択した声を再生する
        self.osana.find_and_play(index.data())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    parameter = 50
    serif = "ぷっ、なにそれ。そもそも付き合う気なかったよ。あっ、安心してる？ふふ、ぜーんぶお見通しってわけｗ"
    window = RoomScreen(parameter, serif)
    sys.exit(app.exec_())
