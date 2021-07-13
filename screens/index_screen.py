#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys, os

from PySide2.QtCore import Qt, QTimer, QCoreApplication
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QPixmap

add_list = ["../detect_modules", "../UI", "../settings", "../screens"]
for dir in add_list:
    sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), dir)))

## ==> MAIN WINDOW
from room_screen import RoomScreen

## ==> INDEX SCREEN
from ui_index_screen import Ui_IndexScreen
from play_voice import PlayVoice

from mood_parameter import MoodParameter

# INDEX SCREEN
class IndexScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_IndexScreen()
        self.ui.setupUi(self)
        self.ui.moodUpLabel.hide()
        self.ui.moodDownLabel.hide()

        # 変数設定
        self.parameter = 50
        self.up_flag = False
        self.down_flag = False

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Osananajimi arrives
        self.osana = PlayVoice()
        print("うぇ、幼馴染がきた")

        # Button setting
        self.ui.startButton.clicked.connect(self.start)
        self.ui.finishButton.clicked.connect(self.finish)
        self.ui.osanaButton1.clicked.connect(self.touch)
        self.ui.osanaButton2.clicked.connect(self.touch)
        self.ui.moodUpButton.clicked.connect(self.mood_up)
        self.ui.moodDownButton.clicked.connect(self.mood_down)

        self.mood_label_dict = {
            "great": ":/image/images/sentences/mood_great.png",
            "good": ":/image/images/sentences/mood_good.png",
            "normal": ":/image/images/sentences/mood_normal.png",
            "awkward": ":/image/images/sentences/mood_awkward.png",
            "bad": ":/image/images/sentences/mood_bad.png"
        }

        self.show()

    def start(self):

        serif = self.osana.play_app_voice("start", self.parameter)

        # SHOW ROOM SCREEN
        self.main = RoomScreen(self.parameter, serif)

        # CLOSE INDEX SCREEN
        self.close()

    def finish(self):
        # 幼馴染をかえらせる
        sys.exit(-1)

    def touch(self):
        touched = True
        self.osana.play_app_voice("start", self.parameter, touched)

    def mood_up(self):

        self.parameter += 10
        if self.parameter > 100:
            self.parameter = 100;
            self.ui.moodUpLabel.setText(QCoreApplication.translate("IndexScreen", u"+0", None))
        else:
            self.ui.moodUpLabel.setText(QCoreApplication.translate("IndexScreen", u"+10", None))
        self.up_flag = True
        self.ui.moodUpLabel.show()
        self.ui.moodDownLabel.hide()
        self.start_qtimer()
        self.set_mood_label()

    def mood_down(self):

        self.parameter -= 10
        if self.parameter < 0:
            self.parameter = 0;
            self.ui.moodDownLabel.setText(QCoreApplication.translate("IndexScreen", u"-0", None))
        else:
            self.ui.moodDownLabel.setText(QCoreApplication.translate("IndexScreen", u"-10", None))

        self.down_flag = True
        self.ui.moodDownLabel.show()
        self.ui.moodUpLabel.hide()
        self.start_qtimer()
        self.set_mood_label()

    def set_mood_label(self):
        mood = MoodParameter(self.parameter).mood
        self.ui.moodDisplayLabel.setPixmap(QPixmap(self.mood_label_dict[mood]))

    def start_qtimer(self):
        #* -----------動作パラメータ--------------
        self.STAGE_NUMBER = 64
        interval = 10
        self.axis = 0.3
        #* --------------------------------------

        # タイマースタート！
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
