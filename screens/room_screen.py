#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, time, random
from datetime import datetime
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

        #*----- Font setting ------
        self.ui.remainingStudyTimeShadow.setText('88:88:88')
        #*-------------------------

        #*----- Variable setting ------
        #* タブ関係
        self.move_flag = True       #* False → タブがどれか出ている
        self.switching_flag = False #* True → タブ切り替え発生
        #* タイマー関係
        self.study_timer_flag = False    #* True → タイマー使用中
        self.break_timer_flag = False    #* True → タイマー使用中
        self.timeout_flag_for_study = False #* True → タイマー時間切れ中
        self.timeout_flag_for_break = False #* True → タイマー時間切れ中
        self.whole_seconds_for_study = 0 #* 残り時間（秒）
        self.whole_seconds_for_break = 0 #* 残り時間（秒）
        #* セリフ関係
        self.serif = serif
        self.serif_list = []
        self.parameter = parameter
        self.osana = PlayVoice()
        self.chat_time = 15*60 #* 15分
        #*-------------------------

        #* セリフModel作成
        self.model = QStringListModel()
        self.show_serif()
        #*-------------------------

        #* カメラオープン！
        self.detect_smapho = DetectSmaphoClass()
        #*-------------------------

        #* REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        #*-------------------------

        #* Button setting
        self.ui.timerButton.clicked.connect(self.operate_timer_tab)
        self.ui.breakButton.clicked.connect(self.operate_break_tab)
        self.ui.logButton.clicked.connect(self.operate_log_tab)
        self.ui.finishButton.clicked.connect(self.operate_finish_tab)
        self.ui.logView.clicked.connect(self.logView_clicked)
        self.ui.timerStartButton.clicked.connect(self.start_study_timer)
        self.ui.breakStartButton.clicked.connect(self.start_break_timer)
        self.ui.finishYesButton.clicked.connect(self.finish_app)
        # self.ui.finishNoButton.clicked.connect(self.operate_finish_tab)
        self.ui.finishNoButton.clicked.connect(self.do_choicechat)
        self.ui.blackFrameButton.clicked.connect(self.background_clicked)
        #*-------------------------


        #* ***************************************************
        #* *************** メイン処理スタート！ ***************
        #* ***************************************************

        #* タイマースタート！
        self.counter = 1

        #* ループスタート！
        self.timer = QTimer()
        self.timer.timeout.connect(self.act_per_second)
        self.timer.start(1000)

        self.show()

    def act_per_second(self):

        #* 5秒ごとに秒出力
        if self.counter%5 == 0: print(self.counter);

        #* 休憩タイマー使用中
        if self.break_timer_flag: self.operate_break_timer();

        else:
            #* 世間話タイム
            if self.counter%self.chat_time == 0:
                chat_functions = [self.do_chat, self.do_choicechat]
                random.choices(chat_functions)[0]()

            #* 15秒ごとにサボり検出
            elif self.counter%15 == 0: self.detect()

        #* 勉強タイマー使用中
        if self.study_timer_flag: self.operate_study_timer();

        now = datetime.now()
        if now.second == 0:
            if (now.minute == 0) & (now.hour in set([0, 3, 6, 9, 12, 15, 18, 21])):
                self.serif = self.osana.play_annoucement(str(now.hour))
                self.show_serif()

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

    def do_chat(self):

        #* 次回世間話タイムを設定
        self.chat_time += random.randint(-240, 240)
        #* -----------------------------------------------

        #* ランダムに世間話を選択肢し、声だし
        self.serif = self.osana.play_chat_voice(self.parameter)
        self.show_serif()

    def do_choicechat(self):

        #* 次回世間話タイムを設定
        self.chat_time += random.randint(-240, 240)
        #* -----------------------------------------------

        #* ランダムに世間話を選択肢し、声だし
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
        #* -----------------------------------------------

        #* ランダム選択した世間話で、popupを出す
        self.chat_popup = ChatPopup(user_reply_list)
        user_reply = ""
        if self.chat_popup.exec_() == QDialog.Accepted:
            #* 世間話popup表示
            self.chat_popup.show()

            #* 世間話popupから返ってくる
            user_reply = self.chat_popup.selected_item
        #* -----------------------------------------------

        #* popupで選択した返答に対し、幼馴染が答える
        index = user_reply_list.index(user_reply)
        self.serif = osana_reply_list[index]
        self.show_serif()
        #* -----------------------------------------------

        #* popupで選択した返答で、機嫌のパラメータが変わる
        point = point_list[index]
        self.osana.play_chat_reply(self.serif)
        self.parameter += point
        #* -----------------------------------------------

    def show_serif(self):
        #* セリフウィンドウに表示
        self.ui.osanaText.show()
        self.ui.osanaText.setText(self.serif)
        print("セリフを表示")

        #* ログに今までのセリフを登録
        self.serif_list.append(self.serif)
        self.model.setStringList(self.serif_list)
        self.ui.logView.setModel(self.model)

    def background_clicked(self):
        if self.func_flag == "Timer":
            self.operate_timer_tab()
        elif self.func_flag == "Break":
            self.operate_break_tab()
        elif self.func_flag == "Log":
            self.operate_log_tab()
        elif self.func_flag == "Finish":
            self.operate_finish_tab()

    def operate_timer_tab(self):
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

    def operate_break_tab(self):
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

    def operate_log_tab(self):
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

    def operate_finish_tab(self):
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
        self.ui.studyTimerLabel.hide()
        self.ui.remainingStudyTime.hide()
        self.ui.remainingStudyTimeShadow.hide()
        self.ui.breakTimerLabel.hide()
        self.ui.remainingBreakTime.hide()
        self.ui.remainingBreakTimeShadow.hide()
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

    def start_study_timer(self):
        self.study_timer_flag = True
        self.timeout_flag_for_study = False

        #* 幼馴染から最初の声出しを頂く
        self.serif = self.osana.play_study_timer_voice("start", self.parameter)
        self.show_serif()

        #* timeEditから時間を取得
        self.set_study_time = self.ui.timerTimeEdit.time().toString()

        #* 勉強タイマーを表示
        self.study_timer = Timer(self.set_study_time)
        self.ui.remainingStudyTime.setText(self.study_timer.add_space(self.set_study_time))
        self.ui.studyTimerLabel.show()
        self.ui.remainingStudyTime.show()
        self.ui.remainingStudyTimeShadow.show()

        #* 秒換算して、Timerウィンドウを下ろす
        self.whole_seconds_for_study = self.study_timer.get_whole_seconds(self.set_study_time)
        self.operate_timer_tab()

    def operate_study_timer(self):

        if not self.timeout_flag_for_study:
            #* 秒から表示用の時間の文字列を取得して、表示
            try:
                remaining_time = self.study_timer.get_str_time(self.whole_seconds_for_study)
            except AttributeError:
                self.study_timer_flag = False
                return
            self.ui.remainingStudyTime.setText(remaining_time)

        #* 一定のタイミングで幼馴染に声をかけてもらう
        if self.whole_seconds_for_study == 0:
            self.serif = self.osana.play_study_timer_voice("finish", self.parameter)
            self.show_serif()

            #* この場合だけpopupを出す
            if self.serif == "もう終わりか～。もうちょっとだけ一緒にしない？":
                user_reply_dict = {
                    "おっけー": "さっすがー！君わかってるぅー！じゃあ30分だけ延長ね！",
                    "無理。疲れた。": "えーノリ悪いよ～。じゃあまた今度ね。お疲れさま！"
                }
                self.chat_popup = ChatPopup(list(user_reply_dict.keys()))
                user_reply = ""
                if self.chat_popup.exec_() == QDialog.Accepted:
                    #* 世間話popup表示
                    self.chat_popup.show()

                    #* 世間話popupから返ってくる
                    user_reply = self.chat_popup.selected_item
                self.serif = user_reply_dict[user_reply]
                self.show_serif()
                self.osana.play_chat_reply(self.serif)
                #* 30分延長
                if user_reply == "おっけー":
                    self.whole_seconds_for_study = 60*30
                #* タイマー終了
                else:
                    self.timeout_flag_for_study = True

            #* 普通にタイマー終了
            else:
                self.timeout_flag_for_study = True

        #* 10分前
        elif self.whole_seconds_for_study == self.study_timer.ten:
            self.serif = self.osana.play_study_timer_voice("mid", self.parameter, "10")
            self.show_serif()
        #* 30分前
        elif self.whole_seconds_for_study == self.study_timer.thirty:
            self.serif = self.osana.play_study_timer_voice("mid", self.parameter, "30")
            self.show_serif()
        #* 半分経過
        elif self.whole_seconds_for_study == self.study_timer.half:
            self.serif = self.osana.play_study_timer_voice("mid", self.parameter, "half")
            self.show_serif()

        #* タイムアウト後の点滅表示
        elif self.whole_seconds_for_study == -1:
            self.ui.remainingStudyTime.hide()
        elif self.whole_seconds_for_study == -2:
            self.ui.remainingStudyTime.show()
        elif self.whole_seconds_for_study == -3:
            self.ui.remainingStudyTime.hide()
        elif self.whole_seconds_for_study == -4:
            self.ui.remainingStudyTime.show()
        elif self.whole_seconds_for_study == -5:
            self.ui.studyTimerLabel.hide()
            self.ui.remainingStudyTime.hide()
            self.ui.remainingStudyTimeShadow.hide()
            self.study_timer_flag = False
            self.timeout_flag_for_study = False

        self.whole_seconds_for_study -= 1

    def start_break_timer(self):
        self.break_timer_flag = True
        self.timeout_flag_for_break = False

        #* 幼馴染から最初の声出しを頂く
        self.serif = self.osana.play_break_timer_voice("start", self.parameter)
        self.show_serif()

        #* timeEditから時間を取得
        self.set_break_time = self.ui.breakTimeEdit.time().toString()

        #* 勉強タイマーを表示
        self.break_timer = Timer(self.set_break_time)
        self.ui.remainingBreakTime.setText(self.break_timer.add_space(self.set_break_time))
        self.ui.breakTimerLabel.show()
        self.ui.remainingBreakTime.show()
        self.ui.remainingBreakTimeShadow.show()

        #* 秒換算して、Timerウィンドウを下ろす
        self.whole_seconds_for_break = self.break_timer.get_whole_seconds(self.set_break_time)
        self.operate_break_tab()

    def operate_break_timer(self):

        if not self.timeout_flag_for_break:
            #* 秒から表示用の時間の文字列を取得して、表示
            try:
                remaining_time = self.break_timer.get_str_time(self.whole_seconds_for_break)
            except AttributeError:
                self.break_timer_flag = False
                return
            self.ui.remainingBreakTime.setText(remaining_time)
            self.study_timer_flag = False

        #* 一定のタイミングで幼馴染に声をかけてもらう
        if self.whole_seconds_for_break == 0:
            self.serif = self.osana.play_break_timer_voice("finish", self.parameter)
            self.show_serif()
            self.timeout_flag_for_break = True
            self.study_timer_flag = True

        #* タイムアウト後の点滅表示
        elif self.whole_seconds_for_break == -1:
            self.ui.remainingBreakTime.hide()
        elif self.whole_seconds_for_break == -2:
            self.ui.remainingBreakTime.show()
        elif self.whole_seconds_for_break == -3:
            self.ui.remainingBreakTime.hide()
        elif self.whole_seconds_for_break == -4:
            self.ui.remainingBreakTime.show()
        elif self.whole_seconds_for_break == -5:
            self.ui.breakTimerLabel.hide()
            self.ui.remainingBreakTime.hide()
            self.ui.remainingBreakTimeShadow.hide()
            self.break_timer_flag = False
            self.timeout_flag_for_break = False

        self.whole_seconds_for_break -= 1

    def finish_app(self):
        self.timer.stop()
        QTimer.singleShot(10000, lambda: sys.exit(-1))
        self.osana.play_app_voice("finish", self.parameter)
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    parameter = 80
    serif = "ぷっ、なにそれ。そもそも付き合う気なかったよ。あっ、安心してる？ふふ、ぜーんぶお見通しってわけｗ"
    window = RoomScreen(parameter, serif)
    sys.exit(app.exec_())
