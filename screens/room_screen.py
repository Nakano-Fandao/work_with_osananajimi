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
from timer import Timer

## ==> ROOM SCREEN
from ui_room_screen import Ui_RoomScreen
## ==> CHAT POPUP
from chat_popup import ChatPopup

# ROOM SCREEN
class RoomScreen(QMainWindow):
    def __init__(self, parameter, serif):
        QMainWindow.__init__(self)

        #*------ UI setting -------
        fonts = QFontDatabase()
        fonts.addApplicationFont(":/font/fonts/Let_s_go_Digital_Regular.ttf")
        self.ui = Ui_RoomScreen()
        self.ui.setupUi(self)
        self.init_objects()
        #*-------------------------

        #*----- font setting ------
        self.ui.remainingTimeShadow.setText('88:88:88')
        #*-------------------------

        self.move_flag = True
        self.timer_flag = False
        self.break_flag = False
        self.switching_flag = False
        self.whole_seconds = 0
        self.serif = serif
        self.parameter = parameter
        self.serif_list = []

        # Model作成
        self.model = QStringListModel()
        self.show_serif()

        # カメラオープン！
        # self.detect_smapho = DetectSmaphoClass()

        self.osana = PlayVoice()

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Button setting
        self.ui.timerButton.clicked.connect(self.operate_timer)
        self.ui.breakButton.clicked.connect(self.operate_break)
        self.ui.logButton.clicked.connect(self.operate_log)
        self.ui.finishButton.clicked.connect(self.operate_finish)
        self.ui.logView.clicked.connect(self.logView_clicked)
        self.ui.timerStartButton.clicked.connect(self.start_timer)
        self.ui.breakStartButton.clicked.connect(self.start_break)
        self.ui.finishYesButton.clicked.connect(lambda x: sys.exit(-1))
        # self.ui.finishNoButton.clicked.connect(self.operate_finish)
        self.ui.finishNoButton.clicked.connect(self.do_choicechat)
        self.ui.blackFrameButton.clicked.connect(self.back_clicked)

        # # タイマースタート！
        # self.counter = -10

        # # ループスタート！
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.act_per_second)
        # self.timer.start(1000)

        self.show()

    def act_per_second(self):

        if self.counter%15 == 0: self.detect()

        if self.counter%5 == 0: print(self.counter);

        #* 勉強タイマー使用中
        if self.timer_flag:
            #* 秒から表示用の時間の文字列を取得して、表示
            remaining_time = self.study_timer.get_str_time(self.whole_seconds)
            self.ui.remainingTime.setText(remaining_time)

            #* 一定のタイミングで幼馴染に声をかけてもらう
            if self.whole_seconds == 0:
                self.serif = self.osana.play_timer_voice("finish", self.parameter)
                self.show_serif()
                self.ui.remainingTime.hide()
                self.ui.remainingTimeShadow.hide()
                self.timer_flag = False

            elif self.whole_seconds == self.study_timer.ten:
                self.serif = self.osana.play_timer_voice("mid", self.parameter, "10")
                self.show_serif()
            elif self.whole_seconds == self.study_timer.thirty:
                self.serif = self.osana.play_timer_voice("mid", self.parameter, "30")
                self.show_serif()
            elif self.whole_seconds == self.study_timer.half:
                self.serif = self.osana.play_timer_voice("mid", self.parameter, "half")
                self.show_serif()


            self.whole_seconds -= 1


        self.counter += 1

    def detect(self):

        if self.counter%15 == 0:
            detected = self.detect_smapho.judge_smapho()
            if not detected:
                pass
            else:
                self.serif = self.osana.play_voice(detected, self.parameter)
                self.show_serif()
                self.parameter -= 10

        if self.counter%30 == 0:
            self.counter = 0
            detected = detect_youtube()
            if not detected:
                pass
            else:
                self.serif = self.osana.play_voice(detected, self.parameter)
                self.show_serif()
                self.parameter -= 10

    def do_choicechat(self):

        self.serif, choicechat_detail = self.osana.play_choicechat_ask(self.parameter)
        self.show_serif()

        user_reply_list = choicechat_detail["user_reply"]
        osana_reply_list = choicechat_detail["osana_reply"]
        point_list = choicechat_detail["point"]

        if self.serif == "お腹すいたな～あたしが何か作るよ！なに食べたい？":
            osana_reply_list = (osana_reply_list[0], osana_reply_list[1])[self.parameter > 55]
            point_list = (point_list[0], point_list[1])[self.parameter > 55]


        print(osana_reply_list)
        print(user_reply_list)
        self.chat_popup = ChatPopup(user_reply_list)
        user_reply = ""
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
        #* セリフウィンドウに表示
        self.ui.osanaText.show()
        self.ui.osanaText.setText(self.serif)
        print("Show serif")

        #* ログに今までのセリフを登録
        self.serif_list.append(self.serif)
        self.model.setStringList(self.serif_list)
        self.ui.logView.setModel(self.model)

    def back_clicked(self):
        if self.func_flag == "Timer":
            self.operate_timer()
        elif self.func_flag == "Break":
            self.operate_break()
        elif self.func_flag == "Log":
            self.operate_log()
        elif self.func_flag == "Finish":
            self.operate_finish()

    def operate_timer(self):
        self.start = time.time()
        self.switch_buttons(False)

        if self.move_flag:
            print("********Timer window opens*********")
            self.func_flag = "Timer"
            self.ui.blackFrame.show()
            self.ui.timerSentence.show()
            self.ui.timerTimeEdit.show()
            self.ui.timerStartButton.show()
            self.ui.timerBackLabel.show()
        else:
            #* 通常（同じボタンを押して戻るとき）
            if self.func_flag == "Timer":
                print("********Timer window closes*********")

            #* 他のボタンを押して戻るとき
            else:
                self.switching_flag = "Timer"
                self.ui.timerSentence.show()
                self.ui.timerTimeEdit.show()
                self.ui.timerStartButton.show()
                self.ui.timerBackLabel.show()
                print(f"*****{self.func_flag} ---> {self.switching_flag}*****")
                self.start_qtimer()
                return

        self.start_qtimer()

    def operate_break(self):
        self.start = time.time()
        self.switch_buttons(False)

        if self.move_flag:
            print("********Break window opens*********")
            self.func_flag = "Break"
            self.ui.blackFrame.show()
            self.ui.breakSentence.show()
            self.ui.breakTimeEdit.show()
            self.ui.breakBackLabel.show()
            self.ui.breakStartButton.show()
        else:
            #* 通常（同じボタンを押して戻るとき）
            if self.func_flag == "Break":
                print("********Break window closes*********")

            #* 他のボタンを押して戻るとき
            else:
                self.switching_flag = "Break"
                self.ui.breakSentence.show()
                self.ui.breakTimeEdit.show()
                self.ui.breakBackLabel.show()
                self.ui.breakStartButton.show()
                print(f"*****{self.func_flag} ---> {self.switching_flag}*****")
                self.start_qtimer()
                return

        self.start_qtimer()

    def operate_log(self):
        self.start = time.time()
        self.switch_buttons(False)

        if self.move_flag:
            print("************Log opens**************")

            self.ui.blackFrame.show()
            self.ui.logView.show()
            self.ui.logBackLabel.show()
            self.switching_flag = False
        else:
            #* 通常（同じボタンを押して戻るとき）
            if self.func_flag == "Log":
                print("************Log closes**************")

            #* 他のボタンを押して戻るとき
            else:
                self.switching_flag = "Log"
                self.ui.logView.show()
                self.ui.logBackLabel.show()
                print(f"*****{self.func_flag} ---> {self.switching_flag}*****")
                self.start_qtimer()
                return

        self.func_flag = "Log"
        self.start_qtimer()

    def operate_finish(self):
        self.start = time.time()
        self.switch_buttons(False)

        if self.move_flag:
            print("********Finish window opens********")
            self.ui.blackFrame.show()
            self.ui.finishYesButton.show()
            self.ui.finishNoButton.show()
            self.ui.finishBackLabel.show()
        else:
            #* 通常（同じボタンを押して戻るとき）
            if self.func_flag == "Finish":
                print("********Finish window closes*********")

            #* 他のボタンを押して戻るとき
            else:
                self.switching_flag = "Finish"
                self.ui.finishYesButton.show()
                self.ui.finishNoButton.show()
                self.ui.finishBackLabel.show()
                print(f"*****{self.func_flag} ---> {self.switching_flag}*****")
                self.start_qtimer()
                return

        self.func_flag = "Finish"
        self.start_qtimer()

    def start_qtimer(self):
        #* 紙をめくる音
        QSound.play(":effect/sounds/effects/paper_flipping.wav")

        #* -----------動作パラメータ--------------
        self.STAGE_NUMBER = 64 # 分割回数（多いほど滑らか）
        interval = 1
        self.set_geometry()
        #* --------------------------------------

        # タイマースタート！
        self.move_counter = 1
        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.move_objects)
        self.move_timer.start(interval)

    def set_geometry(self):
        #* 動かしたいオブジェクトの移動前後の座標・寸法を取得
        self.obj = Geometry(self.func_flag, self.move_flag, self.switching_flag)
        #* -----------------------------------------------

        #* x, y座標のそれぞれの距離と幅・高さそれぞれを分割回数で割り、オブジェクトごとに保存
        self.x, self.y, self.w, self.h = [], [], [], []
        for (before, after) in self.obj.geometry_lists:
            self.x.append([(before[0] - after[0]) / self.STAGE_NUMBER, before[0]])
            self.y.append([(before[1] - after[1]) / self.STAGE_NUMBER, before[1]])
            self.w.append([(before[2] - after[2]) / self.STAGE_NUMBER, before[2]])
            self.h.append([(before[3] - after[3]) / self.STAGE_NUMBER, before[3]])
        #* ------------------------------------------------------

        #* 動かしたいオブジェクトをあらかじめセットしておく
        self.geometryObjects = [self.ui.blackFrame, self.ui.osanaLabel, self.ui.windowLabel, self.ui.osanaText, self.ui.timerButton, self.ui.breakButton, self.ui.logButton, self.ui.finishButton, self.ui.timerLabel, self.ui.breakLabel, self.ui.logLabel, self.ui.finishLabel]

        if (self.func_flag == "Timer") | (self.switching_flag == "Timer"):
            self.geometryObjects.extend([self.ui.timerSentence, self.ui.timerTimeEdit, self.ui.timerStartButton, self.ui.timerBackLabel])

        if (self.func_flag == "Break") | (self.switching_flag == "Break"):
            self.geometryObjects.extend([self.ui.breakSentence, self.ui.breakTimeEdit, self.ui.breakStartButton, self.ui.breakBackLabel])

        if (self.func_flag == "Log") | (self.switching_flag == "Log"):
            self.geometryObjects.extend([self.ui.logView, self.ui.logBackLabel])

        if (self.func_flag == "Finish") | (self.switching_flag == "Finish"):
            self.geometryObjects.extend([self.ui.finishYesButton, self.ui.finishNoButton, self.ui.finishBackLabel])

        if self.switching_flag:
            self.geometryObjects.pop(2)
            self.geometryObjects.pop(2)

        for i in range(len(self.geometryObjects)):
            name = str(self.geometryObjects[i]).split('name="')[1].split('") at')[0]
            if i == 0:
                print(f"{name}: \t\t{self.obj.geometry_lists[i][0]}\t\t ---> \t{self.obj.geometry_lists[i][1]}")
            elif len(name) < 14:
                print(f"{name}: \t\t{self.obj.geometry_lists[i][0]}\t ---> \t{self.obj.geometry_lists[i][1]}")
            else:
                print(f"{name}: \t{self.obj.geometry_lists[i][0]}\t ---> \t{self.obj.geometry_lists[i][1]}")
        #* ------------------------------------------------------

    def switch_buttons(self, flag):
        if flag:
            self.ui.timerButton.show()
            self.ui.breakButton.show()
            self.ui.logButton.show()
            self.ui.finishButton.show()
        else:
            self.ui.timerButton.hide()
            self.ui.breakButton.hide()
            self.ui.logButton.hide()
            self.ui.finishButton.hide()

    def init_objects(self):
        self.ui.logView.hide()
        self.ui.timerBackLabel.hide()
        self.ui.breakBackLabel.hide()
        self.ui.logBackLabel.hide()
        self.ui.finishBackLabel.hide()
        self.ui.blackFrame.hide()
        self.ui.timerSentence.hide()
        self.ui.timerTimeEdit.hide()
        self.ui.timerStartButton.hide()
        self.ui.breakSentence.hide()
        self.ui.breakTimeEdit.hide()
        self.ui.breakStartButton.hide()
        self.ui.remainingTime.hide()
        self.ui.remainingTimeShadow.hide()
        self.ui.finishYesButton.hide()
        self.ui.finishNoButton.hide()

    def move_objects(self):

        #* 黒背景の透明度の値代入
        t_val = round(self.h[0][1] - self.h[0][0]*self.move_counter, 2)
        self.geometryObjects[0].setStyleSheet("QFrame {background-color: rgba(0, 0, 0, " + str(t_val) + ");}")
        #* ------------------------------------------------------

        #* オブジェクトの座標・寸法代入（移動前後の内分点を座標・寸法とする）
        for i, object in enumerate(self.geometryObjects):
            if i == 0: continue;
            object.setGeometry(QRect(
                int(self.x[i][1] - self.x[i][0]*self.move_counter),
                int(self.y[i][1] - self.y[i][0]*self.move_counter),
                int(self.w[i][1] - self.w[i][0]*self.move_counter),
                int(self.h[i][1] - self.h[i][0]*self.move_counter)
            ))
        #* ------------------------------------------------------

        #* オブジェクトの移動終了後の処理
        if self.move_counter == self.STAGE_NUMBER:
            self.move_timer.stop()
            if self.move_flag:
                self.move_flag = False
                self.ui.blackFrameButton.show()
            else:
                if self.func_flag == "Timer":
                    self.ui.timerSentence.hide()
                    self.ui.timerTimeEdit.hide()
                    self.ui.timerBackLabel.hide()
                    self.ui.timerStartButton.hide()
                elif self.func_flag == "Break":
                    self.ui.breakSentence.hide()
                    self.ui.breakTimeEdit.hide()
                    self.ui.breakBackLabel.hide()
                    self.ui.breakStartButton.hide()
                elif self.func_flag == "Log":
                    self.ui.logView.hide()
                    self.ui.logBackLabel.hide()
                elif self.func_flag == "Finish":
                    self.ui.finishYesButton.hide()
                    self.ui.finishNoButton.hide()
                    self.ui.finishBackLabel.hide()

                if self.switching_flag:
                    self.func_flag = self.switching_flag
                    self.switching_flag = False
                else:
                    self.move_flag = True
                    self.ui.blackFrameButton.hide()

            self.switch_buttons(True)
            print(f"takes {time.time() - self.start} s.\n")
        #* ------------------------------------------------------

        self.move_counter += 1

    def logView_clicked(self, index):
        # 選択した声を再生する
        self.osana.find_and_play(index.data())

    def start_timer(self):
        self.timer_flag = True

        #* 幼馴染から最初の声出しを頂く
        self.serif = self.osana.play_timer_voice("start", self.parameter)
        self.show_serif()

        #* timeEditから時間を取得
        self.set_time = self.ui.timerTimeEdit.time().toString()

        #* 勉強タイマーを表示
        self.study_timer = Timer(self.set_time)
        self.ui.remainingTime.setText(self.study_timer.add_space(self.set_time))
        self.ui.remainingTime.show()
        self.ui.remainingTimeShadow.show()

        #* 秒換算して、Timerウィンドウを下ろす
        self.whole_seconds = self.study_timer.get_whole_seconds(self.set_time)
        self.operate_timer()

    def start_break(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    parameter = 50
    serif = "ぷっ、なにそれ。そもそも付き合う気なかったよ。あっ、安心してる？ふふ、ぜーんぶお見通しってわけｗ"
    window = RoomScreen(parameter, serif)
    sys.exit(app.exec_())
