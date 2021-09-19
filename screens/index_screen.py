#! /usr/bin/python
# -*- coding: utf-8 -*-
from screens.loading_screen import LoadingScreen
import sys, os

from PySide2.QtCore import Qt, QTimer, QCoreApplication, QSize
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QPixmap
from PySide2.QtMultimedia import QSound

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "../settings")))
from path_setting import PathSetting
PathSetting().__init__()

## ==> MAIN WINDOW
from loading_screen import LoadingScreen

## ==> INDEX SCREEN
from ui_index_screen import Ui_IndexScreen
from play_voice import PlayVoice
from play_bgm import PlayBgm

from mood_parameter import MoodParameter

# INDEX SCREEN
class IndexScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_IndexScreen()
        self.ui.setupUi(self)
        self.ui.moodUpLabel.hide()
        self.ui.moodDownLabel.hide()

        #* 変数設定
        self.mood_parameter = MoodParameter()
        self.up_flag = False
        self.down_flag = False

        #* REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #* Osananajimi arrives
        self.osana = PlayVoice()
        print("うぇ、幼馴染がきた")
        self.bgm = PlayBgm("Good_News_Today")

        #* Button setting
        self.ui.startButton.clicked.connect(self.start)
        self.ui.finishButton.clicked.connect(self.finish)
        self.ui.osanaButton1.clicked.connect(self.touch)
        self.ui.osanaButton2.clicked.connect(self.touch)
        self.ui.moodUpButton.clicked.connect(self.mood_up)
        self.ui.moodDownButton.clicked.connect(self.mood_down)

        self.ui.moodParameterBar.setValue(self.mood_parameter.parameter)

        self.mood_label_dict = {
            "great": ":/image/images/sentences/mood_great.png",
            "good": ":/image/images/sentences/mood_good.png",
            "normal": ":/image/images/sentences/mood_normal.png",
            "awkward": ":/image/images/sentences/mood_awkward.png",
            "bad": ":/image/images/sentences/mood_bad.png"
        }

        self.show()

    def start(self):
        self.ui.startButton.setIconSize(QSize(312, 69))
        QTimer.singleShot(100, lambda: self.ui.startButton.setIconSize(QSize(306, 63)))

        # SHOW ROOM SCREEN
        QTimer.singleShot(150, self.show_loading_screen)

    def show_loading_screen(self):
        self.loading_screen = LoadingScreen(self.mood_parameter, self.bgm)
        self.loading_screen.show()
        self.close()

    def finish(self):
        self.ui.finishButton.setIconSize(QSize(312, 69))
        QTimer.singleShot(100, lambda: self.ui.finishButton.setIconSize(QSize(306, 63)))
        #* 幼馴染をかえらせる
        self.bgm.stop()
        QTimer.singleShot(150, lambda: sys.exit(-1))

    def touch(self):
        touched = True
        self.osana.play_app_voice("start", self.mood_parameter.mood, touched)

    def mood_up(self):
        self.mood_parameter.change(10)
        if self.mood_parameter.parameter > 100:
            self.mood_parameter.set(100);
            self.ui.moodUpLabel.setText(QCoreApplication.translate("IndexScreen", u"+0", None))
        else:
            self.ui.moodUpLabel.setText(QCoreApplication.translate("IndexScreen", u"+10", None))
        self.up_flag = True
        self.ui.moodUpLabel.show()
        self.ui.moodDownLabel.hide()
        #* ボタンを一瞬大きくする
        self.ui.moodUpButton.setIconSize(QSize(32, 29))
        QTimer.singleShot(100, lambda: self.ui.moodUpButton.setIconSize(QSize(30, 27)))
        #* 値を表示
        self.start_qtimer()
        self.set_mood_label()
        self.ui.moodParameterBar.setValue(100 - self.mood_parameter.parameter)

    def mood_down(self):
        self.mood_parameter.change(-10)
        if self.mood_parameter.parameter < 0:
            self.mood_parameter.set(0);
            self.ui.moodDownLabel.setText(QCoreApplication.translate("IndexScreen", u"-0", None))
        else:
            self.ui.moodDownLabel.setText(QCoreApplication.translate("IndexScreen", u"-10", None))

        self.down_flag = True
        self.ui.moodDownLabel.show()
        self.ui.moodUpLabel.hide()
        #* ボタンを一瞬大きくする
        self.ui.moodDownButton.setIconSize(QSize(32, 29))
        QTimer.singleShot(100, lambda: self.ui.moodDownButton.setIconSize(QSize(30, 27)))
        #* 値を表示
        self.start_qtimer()
        self.set_mood_label()
        self.ui.moodParameterBar.setValue(100 - self.mood_parameter.parameter)

    def set_mood_label(self):
        self.ui.moodDisplayLabel.setPixmap(QPixmap(self.mood_label_dict[self.mood_parameter.mood]))

    def start_qtimer(self):
        #* -----------動作パラメータ--------------
        self.STAGE_NUMBER = 64
        interval = 10
        self.axis = 0.3
        #* --------------------------------------

        #* タイマースタート！
        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.fadeout)
        self.timer.start(interval)

    def fadeout(self):
        if self.up_flag:
            #* y = ax**2 + b
            opacity = -(1/(self.STAGE_NUMBER*(1-self.axis))**2)*(self.counter-self.STAGE_NUMBER*self.axis)**2 + 1
            self.ui.moodUpLabel.setStyleSheet(u"font: 75 26pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
            "color: rgba(255, 169, 0, " + str(round(opacity, 2)) + ");")

        elif self.down_flag:
            #* y = ax**2 + b
            opacity = -(1/(self.STAGE_NUMBER*(1-self.axis))**2)*(self.counter-self.STAGE_NUMBER*self.axis)**2 + 1
            self.ui.moodDownLabel.setStyleSheet(u"font: 75 26pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
            "color: rgba(18, 93, 152, " + str(round(opacity, 2)) + ");")

        if self.counter == self.STAGE_NUMBER:
            self.timer.stop()
            self.up_flag = False
            self.down_flag = False
            self.ui.moodUpLabel.hide()
            self.ui.moodDownLabel.hide()

        self.counter += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IndexScreen()
    sys.exit(app.exec_())
