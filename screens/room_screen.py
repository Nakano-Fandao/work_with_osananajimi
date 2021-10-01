#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, time, random
from datetime import datetime
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from play_voice import PlayVoice
from play_se import PlaySe
from object_geometry import Geometry
from timer import Timer

## ==> ROOM SCREEN
from ui_room_screen import Ui_RoomScreen
## ==> CHAT POPUP
from chat_popup import ChatPopup
from website_selection_popup import WebsiteSelectionPopup
from miniroom_screen import miniRoomScreen
from detection_worker_thread import DetectionWorker

# ROOM SCREEN
class RoomScreen(QMainWindow):
    def __init__(self, mood_parameter, smapho_detection):
        QMainWindow.__init__(self)

        #*------ UI setting -------
        fonts = QFontDatabase()
        fonts.addApplicationFont(":/font/fonts/Let_s_go_Digital_Regular.ttf")
        self.ui = Ui_RoomScreen()
        self.ui.setupUi(self)
        self.init_objects()

        #*----- Text setting ------
        self.ui.remainingStudyTimeShadow.setText('88:88:88')
        self.ui.breakTimeEditer.setText('00 : 05 : 00')

        #*----- Variable setting ------
        #* タブ関係
        self.move_flag = True	   #* False → タブがどれか出ている
        self.switching_flag = False #* True → タブ切り替え発生
        #* タイマー関係
        self.study_timer_flag = False	#* True → タイマー使用中
        self.break_timer_flag = False	#* True → タイマー使用中
        self.timeout_flag_for_study = False #* True → タイマー時間切れ中
        self.timeout_flag_for_break = False #* True → タイマー時間切れ中
        self.whole_seconds_for_study = 0 #* 残り時間（秒）
        self.whole_seconds_for_break = 0 #* 残り時間（秒）
        #* セリフ関係
        self.serif = ""
        self.serif_list = []
        self.mood_parameter = mood_parameter
        self.osana = PlayVoice()
        self.chat_counter = 1
        self.chat_time = 10*60 #* 10分
        #* 検知機能
        self.smapho_detection = smapho_detection
        self.url_list = [
            'https://www.youtube.com/',
            'https://www.nicovideo.jp/',
            'https://video.unext.jp/'
        ]
        #* セリフModel作成
        self.model = QStringListModel()
        #* 効果音
        self.se = PlaySe()
        #* Miniroom Screenが出ているか
        self.miniroom_screen_is_shown = False
        #* 幼馴染の画像
        self.change_osananajimi_image()
        #* カーソル設定
        self.open_cur = QCursor()
        self.open_cur.setShape(Qt.OpenHandCursor)
        self.closed_cur = QCursor()
        self.closed_cur.setShape(Qt.ClosedHandCursor)
        self.pointer_cur = QCursor()
        self.pointer_cur.setShape(Qt.PointingHandCursor)
        self.ui.osanaLabel.setCursor(self.open_cur)
        self.ui.blackFrameButton.setCursor(self.open_cur)

        #* REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #* ボタン設定
        self.init_buttons()
        self.init_timer_time_edit_buttons()
        self.init_break_time_edit_buttons()

        #* ***************************************************
        #*  *************** メイン処理スタート！ ***************
        #* ***************************************************

        print("Room Screen")
        self.se.play("door_knocking")
        self.serif = self.osana.play_app_voice("start", self.mood_parameter.mood)
        self.show_serif()

        #* タイマースタート！
        self.counter = 1

        #* Worker thread作成
        self.createDetectionWorkerThread()

        #* ループスタート！
        self.timer = QTimer()
        self.timer.timeout.connect(self.act_per_second)
        self.timer.start(1000)

    def createDetectionWorkerThread(self):
        self.worker = DetectionWorker(self.smapho_detection, self.url_list)
        self.worker.smapho_detected.connect(self.detected_smapho)
        self.worker.website_detected.connect(self.detected_website)
        self.worker.setTerminationEnabled(True)
        self.worker.start()

    def act_per_second(self):

        #* 休憩タイマー使用中
        if self.break_timer_flag:
            self.operate_break_timer();
        else:
            #* 世間話タイム
            if self.chat_counter == self.chat_time:
                chat_functions = [self.do_chat, self.do_choicechat]
                random.choices(chat_functions)[0]()

        #* 勉強タイマー使用中
        if self.study_timer_flag: self.operate_study_timer();

        now = datetime.now()
        if now.second == 0:
            if (now.minute == 0) & (now.hour in set([0, 3, 6, 9, 12, 15, 18, 21])):
                self.serif = self.osana.play_announcement(str(now.hour))
                self.show_serif()

        #* 10分サボらなければ、機嫌5回復
        if self.counter >= 600:
            self.mood_parameter.change(5)
            self.change_osananajimi_image()
            self.counter = 0

        self.counter += 1
        self.chat_counter += 1

    def detected_smapho(self):
        self.serif = self.osana.play_voice("smapho", self.mood_parameter.mood)
        self.show_serif()
        self.mood_parameter.change(-10)
        self.change_osananajimi_image()
        self.counter = 0

    def detected_website(self, detected_website):
        self.serif = self.osana.play_voice(detected_website, self.mood_parameter.mood)
        self.show_serif()
        self.mood_parameter.change(-10)
        self.change_osananajimi_image()
        self.counter = 0

    def do_chat(self):
        #* 次回世間話タイムを設定
        self.chat_time += random.randint(-240, 240)
        self.chat_counter = 0

        #* ランダムに世間話を選択し、声だし
        self.serif = self.osana.play_chat_voice(self.mood_parameter.mood)
        self.show_serif()

    def do_choicechat(self):
        #* 次回世間話タイムを設定
        self.chat_time += random.randint(-240, 240)
        self.chat_counter = 0

        #* ランダムに世間話を選択し、声だし
        self.serif, choicechat_detail = self.osana.play_choicechat_ask(self.mood_parameter.mood)
        self.show_serif()

        user_reply_list = choicechat_detail["user_reply"]
        osana_reply_list = choicechat_detail["osana_reply"]
        point_list = choicechat_detail["point"]

        if self.serif == "お腹すいたな～あたしが何か作るよ！なに食べたい？":
            osana_reply_list = (osana_reply_list[0], osana_reply_list[1])[self.mood_parameter.parameter > 55]
            point_list = (point_list[0], point_list[1])[self.mood_parameter.parameter > 55]

        #* ランダム選択した世間話で、popupを出す
        self.chat_popup = ChatPopup(user_reply_list)
        user_reply = ""
        if self.chat_popup.exec_() == QDialog.Accepted:
            #* 世間話popup表示
            self.chat_popup.show()

            #* 世間話popupから返ってくる
            user_reply = self.chat_popup.selected_item

        #* popupで選択した返答に対し、幼馴染が答える
        index = user_reply_list.index(user_reply)
        self.serif = osana_reply_list[index]
        self.show_serif()

        #* popupで選択した返答で、機嫌のパラメータが変わる
        point = point_list[index]
        self.osana.play_chat_reply(self.serif)
        self.mood_parameter.change(point)
        self.change_osananajimi_image()

        #* 幼馴染が恥ずかしがっているとき
        ashamed_second = self.mood_parameter.is_ashamed(self.serif)
        if ashamed_second > 0:
            self.change_osananajimi_image("ashamed", ashamed_second)

    def change_osananajimi_image(self, action=None, second=None):
        if action == None:
            image = self.mood_parameter.get_osana_image()
            self.ui.osanaLabel.setPixmap(QPixmap(image))

            #* Miniroom Screenが出ているとき
            if self.miniroom_screen_is_shown:
                self.miniroom_screen.ui.osanaLabel.setPixmap(QPixmap(image))

        #* 幼馴染が恥ずかしがっているとき
        else:
            image = self.mood_parameter.get_osana_image(action)
            self.ui.osanaLabel.setPixmap(QPixmap(image))

            #* Miniroom Screenが出ているとき
            if self.miniroom_screen_is_shown:
                self.miniroom_screen.ui.osanaLabel.setPixmap(QPixmap(image))

            #* 元の顔に戻す
            QTimer.singleShot(second*1000, lambda: self.change_osananajimi_image())

    def show_serif(self):
        #* セリフウィンドウに表示
        self.ui.osanaText.show()
        self.ui.osanaText.setText(self.serif)

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
        self.tab = "Timer"
        self.operate_tab()

    def operate_break_tab(self):
        self.tab = "Break"
        self.operate_tab()

    def operate_log_tab(self):
        self.tab = "Log"
        self.operate_tab()

    def operate_finish_tab(self):
        self.tab = "Finish"
        self.operate_tab()

    def operate_tab(self):
        self.start = time.time()
        self.switch_buttons(False)

        if self.move_flag:
            print(f"********{self.tab} window opens*********")
            self.func_flag = self.tab
            self.ui.blackFrame.show()

            if self.tab == "Timer":
                self.ui.timerWidget.show();
            elif self.tab == "Break":
                self.ui.breakWidget.show();
            elif self.tab == "Log":
                self.ui.logView.show()
                self.ui.logBackLabel.show()
            elif self.tab == "Finish":
                self.ui.finishYesButton.show()
                self.ui.finishNoButton.show()
                self.ui.finishBackLabel.show()
            self.raise_objects(self.tab)

        else:
            #* 通常（同じボタンを押して戻るとき）
            if self.func_flag == self.tab:
                print(f"********{self.func_flag} window closes*********")

            #* 他のボタンを押して戻るとき
            else:
                self.switching_flag = self.tab
                if self.tab == "Timer":
                    self.ui.timerWidget.show();
                elif self.tab == "Break":
                    self.ui.breakWidget.show();
                elif self.tab == "Log":
                    self.ui.logView.show()
                    self.ui.logBackLabel.show()
                elif self.tab == "Finish":
                    self.ui.finishYesButton.show()
                    self.ui.finishNoButton.show()
                    self.ui.finishBackLabel.show()
                self.raise_objects(self.tab)
                print(f"*****{self.func_flag} ---> {self.switching_flag}*****")

        self.start_qtimer()

    def start_qtimer(self):
        #* 紙をめくる音
        self.se.play("paper_flipping")

        #* -----------動作パラメータ--------------
        self.STAGE_NUMBER = 64 # 分割回数（多いほど滑らか）
        interval = 1
        self.set_geometry()

        # タイマースタート！
        self.move_counter = 1
        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.move_objects)
        self.move_timer.start(interval)

    def set_geometry(self):
        #* 動かしたいオブジェクトの移動前後の座標・寸法を取得
        self.obj = Geometry(self.func_flag, self.move_flag, self.switching_flag)

        #* x, y座標のそれぞれの距離と幅・高さそれぞれを分割回数で割り、オブジェクトごとに保存
        self.x, self.y, self.w, self.h = [], [], [], []
        for (before, after) in self.obj.geometry_lists:
            self.x.append([(before[0] - after[0]) / self.STAGE_NUMBER, before[0]])
            self.y.append([(before[1] - after[1]) / self.STAGE_NUMBER, before[1]])
            self.w.append([(before[2] - after[2]) / self.STAGE_NUMBER, before[2]])
            self.h.append([(before[3] - after[3]) / self.STAGE_NUMBER, before[3]])

        #* 動かしたいオブジェクトをあらかじめセットしておく
        self.geometryObjects = [self.ui.blackFrame, self.ui.osanaLabel, self.ui.windowLabel, self.ui.osanaText, self.ui.timerButton, self.ui.breakButton, self.ui.logButton, self.ui.finishButton, self.ui.timerLabel, self.ui.breakLabel, self.ui.logLabel, self.ui.finishLabel]

        if (self.func_flag == "Timer") | (self.switching_flag == "Timer"):
            self.geometryObjects.extend([self.ui.timerWidget])
        if (self.func_flag == "Break") | (self.switching_flag == "Break"):
            self.geometryObjects.extend([self.ui.breakWidget])
        if (self.func_flag == "Log") | (self.switching_flag == "Log"):
            self.geometryObjects.extend([self.ui.logView, self.ui.logBackLabel])
        if (self.func_flag == "Finish") | (self.switching_flag == "Finish"):
            self.geometryObjects.extend([self.ui.finishYesButton, self.ui.finishNoButton, self.ui.finishBackLabel])
        if self.switching_flag:
            self.geometryObjects.pop(2)
            self.geometryObjects.pop(2)

        #* debug
        # for i in range(len(self.geometryObjects)):
        # 	name = str(self.geometryObjects[i]).split('name="')[1].split('") at')[0]
        # 	if i == 0:
        # 		print(f"{name}: \t\t{self.obj.geometry_lists[i][0]}\t\t ---> \t{self.obj.geometry_lists[i][1]}")
        # 	elif len(name) < 14:
        # 		print(f"{name}: \t\t{self.obj.geometry_lists[i][0]}\t ---> \t{self.obj.geometry_lists[i][1]}")
        # 	else:
        # 		print(f"{name}: \t{self.obj.geometry_lists[i][0]}\t ---> \t{self.obj.geometry_lists[i][1]}")

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

    def init_buttons(self):
        self.ui.timerButton.clicked.connect(self.operate_timer_tab)
        self.ui.breakButton.clicked.connect(self.operate_break_tab)
        self.ui.logButton.clicked.connect(self.operate_log_tab)
        self.ui.finishButton.clicked.connect(self.operate_finish_tab)
        self.ui.logView.clicked.connect(self.logView_clicked)
        self.ui.timerStartButton.clicked.connect(self.start_study_timer)
        self.ui.breakStartButton.clicked.connect(self.start_break_timer)
        self.ui.finishYesButton.clicked.connect(self.finish_app)
        self.ui.finishNoButton.clicked.connect(self.operate_finish_tab)
        # self.ui.finishNoButton.clicked.connect(self.do_choicechat)
        self.ui.blackFrameButton.clicked.connect(self.background_clicked)
        self.ui.smaphoButton.clicked.connect(self.switch_smapho)
        self.ui.chromeButton.clicked.connect(self.switch_chrome)
        self.ui.minimizeButton.clicked.connect(self.show_miniroom)
        self.ui.editWebsiteButton.clicked.connect(self.show_website_selection)

    def show_website_selection(self):
        self.selection_popup = WebsiteSelectionPopup(self.url_list)
        if self.selection_popup.exec_() == QDialog.Accepted:
            #* popup表示
            self.selection_popup.show()

            #* popupから返ってくる
            self.url_list = self.selection_popup.selected_items
            self.worker.set_websites(self.url_list)

    def show_miniroom(self):
        smapho_bool = self.worker.smapho_flag
        chrome_bool = self.worker.chrome_flag
        self.miniroom_screen = miniRoomScreen(self, smapho_bool, chrome_bool)
        self.handle_miniroom_flag(True)
        self.change_osananajimi_image()
        self.miniroom_screen.show()
        self.hide()

    def handle_miniroom_flag(self, flag):
        self.miniroom_screen_is_shown = flag

    def switch_smapho(self):
        if self.worker.smapho_flag:
            self.worker.smapho_flag = False
            smapho_icon = QIcon()
            smapho_icon.addFile(u":/image/images/icons/gray_smapho.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            self.worker.smapho_flag = True
            smapho_icon = QIcon()
            smapho_icon.addFile(u":/image/images/icons/pink_smapho.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.smaphoButton.setIconSize(QSize(55, 55))
        QTimer.singleShot(100, lambda: self.ui.smaphoButton.setIconSize(QSize(51, 51)))
        QTimer.singleShot(110, lambda: self.ui.smaphoButton.setIcon(smapho_icon))

    def switch_chrome(self):
        if self.worker.chrome_flag:
            self.worker.chrome_flag = False
            chrome_icon = QIcon()
            chrome_icon.addFile(u":/image/images/icons/gray_chrome.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            self.worker.chrome_flag = True
            chrome_icon = QIcon()
            chrome_icon.addFile(u":/image/images/icons/blue_chrome.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.chromeButton.setIconSize(QSize(55, 55))
        QTimer.singleShot(100, lambda: self.ui.chromeButton.setIconSize(QSize(51, 51)))
        QTimer.singleShot(110, lambda: self.ui.chromeButton.setIcon(chrome_icon))

    def init_timer_time_edit_buttons(self):

        thin_icon_size = QSize(22, 20)
        expanded_thin_icon_size = QSize(26, 24)
        thick_icon_size = QSize(38, 20)
        expanded_thick_icon_size = QSize(42, 24)

        def read_timer_time_editer():
            time_text = self.ui.timerTimeEditer.text()
            self.timer_hour, self.timer_minute, self.timer_second = \
                list(map(
                    lambda x: int("".join(x.split())),
                    time_text.split(":")
                ))

        def update_timer_time_editer():
            self.timer_hour %= 100
            self.timer_minute %= 60
            self.timer_second %= 60
            hour = str(self.timer_hour).zfill(2).replace("1", " 1")
            minute = str(self.timer_minute).zfill(2).replace("1", " 1")
            second = str(self.timer_second).zfill(2).replace("1", " 1")
            time =u"{} : {} : {}".format(hour, minute, second)
            self.ui.timerTimeEditer.setText(QCoreApplication.translate("RoomScreen", time, None))

        def timer_superup_hour():
            read_timer_time_editer()
            self.timer_hour += 5
            self.ui.timer_largeUpButton_hour.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_largeUpButton_hour.setIconSize(thin_icon_size))
            update_timer_time_editer()
            print("5 hours increased")

        def timer_superup_minute():
            read_timer_time_editer()
            self.timer_minute += 10
            self.ui.timer_largeUpButton_minute.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_largeUpButton_minute.setIconSize(thin_icon_size))
            update_timer_time_editer()
            print("10 minutes increased")

        def timer_superup_second():
            read_timer_time_editer()
            self.timer_second += 10
            self.ui.timer_largeUpButton_second.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_largeUpButton_second.setIconSize(thin_icon_size))
            update_timer_time_editer()
            print("10 seconds increased")

        def timer_up_hour():
            read_timer_time_editer()
            self.timer_hour += 1
            self.ui.timer_smallUpButton_hour.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_smallUpButton_hour.setIconSize(thick_icon_size))
            update_timer_time_editer()
            print("1 hour increased")

        def timer_up_minute():
            read_timer_time_editer()
            self.timer_minute += 1
            self.ui.timer_smallUpButton_minute.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_smallUpButton_minute.setIconSize(thick_icon_size))
            update_timer_time_editer()
            print("1 minute increased")

        def timer_up_second():
            read_timer_time_editer()
            self.timer_second += 1
            self.ui.timer_smallUpButton_second.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_smallUpButton_second.setIconSize(thick_icon_size))
            update_timer_time_editer()
            print("1 second increased")

        def timer_superdown_hour():
            read_timer_time_editer()
            self.timer_hour -= 5
            self.ui.timer_largeDownButton_hour.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_largeDownButton_hour.setIconSize(thin_icon_size))
            update_timer_time_editer()
            print("5 hours decreased")

        def timer_superdown_minute():
            read_timer_time_editer()
            self.timer_minute -= 10
            self.ui.timer_largeDownButton_minute.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_largeDownButton_minute.setIconSize(thin_icon_size))
            update_timer_time_editer()
            print("10 minutes decreased")

        def timer_superdown_second():
            read_timer_time_editer()
            self.timer_second -= 10
            self.ui.timer_largeDownButton_second.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_largeDownButton_second.setIconSize(thin_icon_size))
            update_timer_time_editer()
            print("10 seconds decreased")

        def timer_down_hour():
            read_timer_time_editer()
            self.timer_hour -= 1
            self.ui.timer_smallDownButton_hour.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_smallDownButton_hour.setIconSize(thick_icon_size))
            update_timer_time_editer()
            print("1 hour decreased")

        def timer_down_minute():
            read_timer_time_editer()
            self.timer_minute -= 1
            self.ui.timer_smallDownButton_minute.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_smallDownButton_minute.setIconSize(thick_icon_size))
            update_timer_time_editer()
            print("1 minute decreased")

        def timer_down_second():
            read_timer_time_editer()
            self.timer_second -= 1
            self.ui.timer_smallDownButton_second.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.timer_smallDownButton_second.setIconSize(thick_icon_size))
            update_timer_time_editer()
            print("1 second decreased")

        self.ui.timer_largeUpButton_hour.clicked.connect(timer_superup_hour)
        self.ui.timer_largeUpButton_minute.clicked.connect(timer_superup_minute)
        self.ui.timer_largeUpButton_second.clicked.connect(timer_superup_second)
        self.ui.timer_smallUpButton_hour.clicked.connect(timer_up_hour)
        self.ui.timer_smallUpButton_minute.clicked.connect(timer_up_minute)
        self.ui.timer_smallUpButton_second.clicked.connect(timer_up_second)
        self.ui.timer_largeDownButton_hour.clicked.connect(timer_superdown_hour)
        self.ui.timer_largeDownButton_minute.clicked.connect(timer_superdown_minute)
        self.ui.timer_largeDownButton_second.clicked.connect(timer_superdown_second)
        self.ui.timer_smallDownButton_hour.clicked.connect(timer_down_hour)
        self.ui.timer_smallDownButton_minute.clicked.connect(timer_down_minute)
        self.ui.timer_smallDownButton_second.clicked.connect(timer_down_second)

    def init_break_time_edit_buttons(self):

        thin_icon_size = QSize(22, 20)
        expanded_thin_icon_size = QSize(26, 24)
        thick_icon_size = QSize(38, 20)
        expanded_thick_icon_size = QSize(42, 24)

        def read_break_time_editer():
            time_text = self.ui.breakTimeEditer.text()
            self.break_hour, self.break_minute, self.break_second = \
                list(map(
                    lambda x: int("".join(x.split())),
                    time_text.split(":")
                ))

        def update_break_time_editer():
            self.break_hour %= 100
            self.break_minute %= 60
            self.break_second %= 60
            hour = str(self.break_hour).zfill(2).replace("1", " 1")
            minute = str(self.break_minute).zfill(2).replace("1", " 1")
            second = str(self.break_second).zfill(2).replace("1", " 1")
            time =u"{} : {} : {}".format(hour, minute, second)
            self.ui.breakTimeEditer.setText(QCoreApplication.translate("RoomScreen", time, None))

        def break_superup_hour():
            read_break_time_editer()
            self.break_hour += 5
            self.ui.break_largeUpButton_hour.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_largeUpButton_hour.setIconSize(thin_icon_size))
            update_break_time_editer()
            print("5 hours increased")

        def break_superup_minute():
            read_break_time_editer()
            self.break_minute += 10
            self.ui.break_largeUpButton_minute.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_largeUpButton_minute.setIconSize(thin_icon_size))
            update_break_time_editer()
            print("10 minutes increased")

        def break_superup_second():
            read_break_time_editer()
            self.break_second += 10
            self.ui.break_largeUpButton_second.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_largeUpButton_second.setIconSize(thin_icon_size))
            update_break_time_editer()
            print("10 seconds increased")

        def break_up_hour():
            read_break_time_editer()
            self.break_hour += 1
            self.ui.break_smallUpButton_hour.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_smallUpButton_hour.setIconSize(thick_icon_size))
            update_break_time_editer()
            print("1 hour increased")

        def break_up_minute():
            read_break_time_editer()
            self.break_minute += 1
            self.ui.break_smallUpButton_minute.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_smallUpButton_minute.setIconSize(thick_icon_size))
            update_break_time_editer()
            print("1 minute increased")

        def break_up_second():
            read_break_time_editer()
            self.break_second += 1
            self.ui.break_smallUpButton_second.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_smallUpButton_second.setIconSize(thick_icon_size))
            update_break_time_editer()
            print("1 second increased")

        def break_superdown_hour():
            read_break_time_editer()
            self.break_hour -= 5
            self.ui.break_largeDownButton_hour.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_largeDownButton_hour.setIconSize(thin_icon_size))
            update_break_time_editer()
            print("5 hours decreased")

        def break_superdown_minute():
            read_break_time_editer()
            self.break_minute -= 10
            self.ui.break_largeDownButton_minute.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_largeDownButton_minute.setIconSize(thin_icon_size))
            update_break_time_editer()
            print("10 minutes decreased")

        def break_superdown_second():
            read_break_time_editer()
            self.break_second -= 10
            self.ui.break_largeDownButton_second.setIconSize(expanded_thin_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_largeDownButton_second.setIconSize(thin_icon_size))
            update_break_time_editer()
            print("10 seconds decreased")

        def break_down_hour():
            read_break_time_editer()
            self.break_hour -= 1
            self.ui.break_smallDownButton_hour.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_smallDownButton_hour.setIconSize(thick_icon_size))
            update_break_time_editer()
            print("1 hour decreased")

        def break_down_minute():
            read_break_time_editer()
            self.break_minute -= 1
            self.ui.break_smallDownButton_minute.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_smallDownButton_minute.setIconSize(thick_icon_size))
            update_break_time_editer()
            print("1 minute decreased")

        def break_down_second():
            read_break_time_editer()
            self.break_second -= 1
            self.ui.break_smallDownButton_second.setIconSize(expanded_thick_icon_size)
            QTimer.singleShot(100, lambda: self.ui.break_smallDownButton_second.setIconSize(thick_icon_size))
            update_break_time_editer()
            print("1 second decreased")

        self.ui.break_largeUpButton_hour.clicked.connect(break_superup_hour)
        self.ui.break_largeUpButton_minute.clicked.connect(break_superup_minute)
        self.ui.break_largeUpButton_second.clicked.connect(break_superup_second)
        self.ui.break_smallUpButton_hour.clicked.connect(break_up_hour)
        self.ui.break_smallUpButton_minute.clicked.connect(break_up_minute)
        self.ui.break_smallUpButton_second.clicked.connect(break_up_second)
        self.ui.break_largeDownButton_hour.clicked.connect(break_superdown_hour)
        self.ui.break_largeDownButton_minute.clicked.connect(break_superdown_minute)
        self.ui.break_largeDownButton_second.clicked.connect(break_superdown_second)
        self.ui.break_smallDownButton_hour.clicked.connect(break_down_hour)
        self.ui.break_smallDownButton_minute.clicked.connect(break_down_minute)
        self.ui.break_smallDownButton_second.clicked.connect(break_down_second)

    def init_objects(self):
        self.ui.blackFrame.hide()
        self.ui.timerWidget.hide()
        self.ui.breakWidget.hide()
        self.ui.logView.hide()
        self.ui.logBackLabel.hide()
        self.ui.finishYesButton.hide()
        self.ui.finishNoButton.hide()
        self.ui.finishBackLabel.hide()
        self.ui.studyTimerLabel.hide()
        self.ui.breakTimerLabel.hide()
        self.ui.remainingStudyTime.hide()
        self.ui.remainingStudyTimeShadow.hide()
        self.ui.remainingBreakTime.hide()
        self.ui.remainingBreakTimeShadow.hide()

        #* オブジェクトのレイヤー順
        self.ui.insideRoomLabel.raise_()
        self.ui.blackFrame.raise_()
        self.ui.osanaLabel.raise_()
        self.ui.remainingStudyTimeShadow.raise_()
        self.ui.remainingBreakTimeShadow.raise_()
        self.ui.remainingStudyTime.raise_()
        self.ui.remainingBreakTime.raise_()
        self.ui.studyTimerLabel.raise_()
        self.ui.breakTimerLabel.raise_()
        self.raise_objects("")

    def raise_objects(self, func):
        if func == "Timer":
            self.ui.timerWidget.raise_()
        elif func == "Break":
            self.ui.breakWidget.raise_()
        elif func == "Log":
            self.ui.logBackLabel.raise_()
            self.ui.logView.raise_()
        elif func == "Finish":
            self.ui.finishBackLabel.raise_()
            self.ui.finishYesButton.raise_()
            self.ui.finishNoButton.raise_()

        self.ui.timerLabel.raise_()
        self.ui.breakLabel.raise_()
        self.ui.logLabel.raise_()
        self.ui.finishLabel.raise_()
        self.ui.windowLabel.raise_()
        self.ui.osanaText.raise_()
        self.ui.timerButton.raise_()
        self.ui.breakButton.raise_()
        self.ui.logButton.raise_()
        self.ui.finishButton.raise_()
        self.ui.smaphoButton.raise_()
        self.ui.chromeButton.raise_()
        self.ui.minimizeButton.raise_()
        self.ui.editWebsiteButton.raise_()

    def move_objects(self):

        #* 黒背景の透明度の値代入
        t_val = round(self.h[0][1] - self.h[0][0]*self.move_counter, 2)
        self.geometryObjects[0].setStyleSheet("QFrame {background-color: rgba(0, 0, 0, " + str(t_val) + ");}")

        #* オブジェクトの座標・寸法代入（移動前後の内分点を座標・寸法とする）
        for i, object in enumerate(self.geometryObjects):
            if i == 0: continue;
            object.setGeometry(QRect(
                int(self.x[i][1] - self.x[i][0]*self.move_counter),
                int(self.y[i][1] - self.y[i][0]*self.move_counter),
                int(self.w[i][1] - self.w[i][0]*self.move_counter),
                int(self.h[i][1] - self.h[i][0]*self.move_counter)
            ))

        #* オブジェクトの移動終了後の処理
        if self.move_counter == self.STAGE_NUMBER:
            self.move_timer.stop()
            if self.move_flag:
                self.move_flag = False
                self.ui.blackFrameButton.show()
            else:
                if self.func_flag == "Timer":
                    self.ui.timerWidget.hide()
                elif self.func_flag == "Break":
                    self.ui.breakWidget.hide()
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
            # print(f"takes {time.time() - self.start} s.\n")

        self.move_counter += 1

    def logView_clicked(self, index):
        # 選択した声を再生する
        self.osana.find_and_play(index.data())

    def start_study_timer(self):
        self.study_timer_flag = True
        self.timeout_flag_for_study = False

        #* 幼馴染から最初の声出しを頂く
        self.serif = self.osana.play_study_timer_voice("start", self.mood_parameter.mood)
        self.show_serif()

        #* timeEditから時間を取得
        self.set_study_time = self.ui.timerTimeEditer.text()

        #* 勉強タイマーを表示
        self.study_timer = Timer(self.set_study_time)
        self.ui.remainingStudyTime.setText(self.study_timer.str_initial_time)
        self.ui.studyTimerLabel.show()
        self.ui.remainingStudyTime.show()
        # self.ui.remainingStudyTimeShadow.show()

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
            self.serif = self.osana.play_study_timer_voice("finish", self.mood_parameter.mood)
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
            self.serif = self.osana.play_study_timer_voice("mid", self.mood_parameter.mood, "10")
            self.show_serif()
        #* 30分前
        elif self.whole_seconds_for_study == self.study_timer.thirty:
            self.serif = self.osana.play_study_timer_voice("mid", self.mood_parameter.mood, "30")
            self.show_serif()
        #* 半分経過
        elif self.whole_seconds_for_study == self.study_timer.half:
            self.serif = self.osana.play_study_timer_voice("mid", self.mood_parameter.mood, "half")
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
        self.serif = self.osana.play_break_timer_voice("start", self.mood_parameter.mood)
        self.show_serif()
        self.worker.stop()

        #* breakTimeEditerから時間を取得
        self.set_break_time = self.ui.breakTimeEditer.text()

        #* 勉強タイマーを表示
        self.break_timer = Timer(self.set_break_time)
        self.ui.remainingBreakTime.setText(self.break_timer.str_initial_time)
        self.ui.breakTimerLabel.show()
        self.ui.remainingBreakTime.show()
        # self.ui.remainingBreakTimeShadow.show()

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
            self.serif = self.osana.play_break_timer_voice("finish", self.mood_parameter.mood)
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
            self.worker.restart(self.url_list)

        self.whole_seconds_for_break -= 1

    def finish_app(self):
        self.timer.stop()
        self.worker.end()

        QTimer.singleShot(10000, lambda: sys.exit(-1))
        self.osana.play_app_voice("finish", self.mood_parameter.mood)
        self.hide()

    def mousePressEvent(self, event):
        self.__isDrag = True
        self.__startPos = event.pos()
        self.ui.osanaLabel.setCursor(self.closed_cur)
        self.ui.blackFrameButton.setCursor(self.closed_cur)

    def mouseReleaseEvent(self, event):
        self.__isDrag = False
        self.ui.osanaLabel.setCursor(self.open_cur)
        self.ui.blackFrameButton.setCursor(self.open_cur)

    def mouseMoveEvent(self, event):
        if self.__isDrag:
            self.move(self.mapToParent(event.pos() - self.__startPos))
            self.ui.osanaLabel.setCursor(self.closed_cur)
            self.ui.blackFrameButton.setCursor(self.closed_cur)