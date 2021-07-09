#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, time
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
from object_geometry import Geometry

## ==> ROOM SCREEN
from ui_room_screen import Ui_RoomScreen
## ==> CHAT POPUP
from chat_popup import ChatPopup

# ROOM SCREEN
class RoomScreen(QMainWindow):
    def __init__(self, parameter, serif):
        QMainWindow.__init__(self)

        #*------ UI setting -------
        self.ui = Ui_RoomScreen()
        self.ui.setupUi(self)
        self.ui.logView.hide()
        self.ui.timerBackLabel.hide()
        self.ui.breakBackLabel.hide()
        self.ui.logBackLabel.hide()
        self.ui.finishBackLabel.hide()
        self.ui.blackFrame.hide()
        self.ui.breakSentence.hide()
        self.ui.timeEdit.hide()
        #*-------------------------

        self.move_flag = True

        self.parameter = parameter
        self.serif_list = []
        self.serif = serif
        self.show_serif()

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
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Button setting
        self.ui.serifButton.clicked.connect(self.show_serif)
        self.ui.timerButton.clicked.connect(self.operate_timer)
        self.ui.breakButton.clicked.connect(self.operate_break)
        self.ui.logButton.clicked.connect(self.operate_log)
        self.ui.finishButton.clicked.connect(self.operate_finish)

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

        if self.counter%5 == 0: print(self.counter);
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

    def show_serif(self):
        self.ui.osanaText.show()
        self.ui.osanaText.setText(self.serif)
        self.serif_list.append(self.serif)
        print("Show serif")

    def operate_timer(self):
        self.start = time.time()

        if self.move_flag:
            print("********Timer window opens*********")
            self.ui.blackFrame.show()
            self.ui.breakSentence.show()
            self.ui.timeEdit.show()
            self.ui.timerBackLabel.show()
            self.ui.breakButton.hide()
            self.ui.logButton.hide()
            self.ui.finishButton.hide()
        else:
            print("********Timer window closes*********")
            self.start = time.time()

        self.func_flag = "Timer"
        self.start_qtimer()

    def operate_break(self):
        self.start = time.time()

        if self.move_flag:
            print("********Break window opens*********")
            self.ui.blackFrame.show()
            self.ui.breakBackLabel.show()
            self.ui.timerButton.hide()
            self.ui.logButton.hide()
            self.ui.finishButton.hide()
        else:
            print("********Break window closes*********")
            self.start = time.time()

        self.func_flag = "Break"
        self.start_qtimer()

    def operate_log(self):
        self.start = time.time()

        if self.move_flag:
            print("************Log opens**************")

            self.ui.logView.show()
            self.ui.logBackLabel.show()
            self.ui.blackFrame.show()
            self.ui.timerButton.hide()
            self.ui.breakButton.hide()
            self.ui.finishButton.hide()

            self.model.setStringList(self.serif_list)
            self.ui.logView.setModel(self.model)
        else:
            print("************Log closes**************")

        self.func_flag = "Log"
        self.start_qtimer()

    def operate_finish(self):
        sys.exit(-1)

    def start_qtimer(self):
        # 紙をめくる音
        QSound.play(":effect/sounds/effects/paper_flipping.wav")

        self.STAGE_NUMBER = 64 # 分割回数（多いほど滑らか）
        self.interval = 1
        self.set_geometry()

        # タイマースタート！
        self.move_counter = 1
        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.move_log)
        self.move_timer.start(1)

    def set_geometry(self):
        self.obj = Geometry(self.func_flag, self.move_flag)

        self.geometryObjects = [self.ui.blackFrame, self.ui.osanaLabel, self.ui.windowLabel, self.ui.osanaText, self.ui.serifButton, self.ui.timerButton, self.ui.breakButton, self.ui.logButton, self.ui.finishButton, self.ui.timerLabel, self.ui.breakLabel, self.ui.logLabel, self.ui.finishLabel]

        if self.func_flag == "Timer":
            self.geometryObjects.extend([self.ui.breakSentence, self.ui.timeEdit, self.ui.timerBackLabel])

        elif self.func_flag == "Break":
            self.geometryObjects.extend([self.ui.breakBackLabel])

        elif self.func_flag == "Log":
            self.geometryObjects.extend([self.ui.logView, self.ui.logBackLabel])

        self.x, self.y, self.w, self.h = [], [], [], []
        for (before, after) in self.obj.geometry_lists:
            self.x.append([(before[0] - after[0]) / self.STAGE_NUMBER, before[0]])
            self.y.append([(before[1] - after[1]) / self.STAGE_NUMBER, before[1]])
            self.w.append([(before[2] - after[2]) / self.STAGE_NUMBER, before[2]])
            self.h.append([(before[3] - after[3]) / self.STAGE_NUMBER, before[3]])

    def move_log(self):

        t_val = round(self.h[0][1] - self.h[0][0]*self.move_counter, 2)
        self.geometryObjects[0].setStyleSheet("QFrame {background-color: rgba(0, 0, 0, " + str(t_val) + ");}")

        for i, object in enumerate(self.geometryObjects):
            if i == 0: continue;
            object.setGeometry(QRect(
                int(self.x[i][1] - self.x[i][0]*self.move_counter),
                int(self.y[i][1] - self.y[i][0]*self.move_counter),
                int(self.w[i][1] - self.w[i][0]*self.move_counter),
                int(self.h[i][1] - self.h[i][0]*self.move_counter)
            ))

        if self.move_counter == self.STAGE_NUMBER:
            self.move_timer.stop()
            if self.move_flag:
                if self.func_flag == "Log":
                    pass
                elif self.func_flag == "Timer":
                    pass
                self.move_flag = False

            else:
                if self.func_flag == "Timer":
                    self.ui.breakSentence.hide()
                    self.ui.timeEdit.hide()
                    self.ui.timerBackLabel.hide()
                elif self.func_flag == "Break":
                    self.ui.breakBackLabel.hide()
                elif self.func_flag == "Log":
                    self.ui.logView.hide()
                    self.ui.logBackLabel.hide()
                self.ui.blackFrame.hide()
                self.ui.timerButton.show()
                self.ui.breakButton.show()
                self.ui.logButton.show()
                self.ui.finishButton.show()
                self.move_flag = True
            print(f"takes {time.time() - self.start} s.")

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
