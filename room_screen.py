#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, json, os, time, random

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QSound

from detect_modules.smapho import DetectSmaphoClass
from detect_modules.detect_chrome import detect_youtube

from play_voice import PlayVoice

## ==> MAIN WINDOW
from chat_popup import ChatPopup

## ==> INDEX SCREEN
from UI.ui_room_screen import Ui_RoomScreen

## ==> Sound Effects
import files_rc

# GUI FILE
# from app_modules import *

# YOUR APPLICATION
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
        chats = [
            "えっ、よかったじゃん…お似合いだよ",
            "嫌だ嫌だ嫌だ",
            "付き合うのか、俺以外の奴と。"
        ]
        QSound.play(":voice/sounds/voices/choicechat_good_4_ask.wav")

        self.popup = ChatPopup(chats)
        self.popup.show()


    def show_break(self):
        self.change_window("break")
        print("Show break")


    def show_finish(self):
        sys.exit(-1)
