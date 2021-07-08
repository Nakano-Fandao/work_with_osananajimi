#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow

## ==> MAIN WINDOW
from room_screen import RoomScreen

## ==> INDEX SCREEN
from ui_index_screen import Ui_IndexScreen
from play_voice import PlayVoice

from settings.mood_parameter import MoodParameter

# INDEX SCREEN
class IndexScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_IndexScreen()
        self.ui.setupUi(self)

        # 変数設定
        self.parameter = 50

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Osananajimi arrives
        self.osana = PlayVoice()
        print("うぇ、幼馴染がきた")

        # Button setting
        self.ui.startButton.clicked.connect(self.start)
        self.ui.finishButton.clicked.connect(self.finish)
        self.ui.osanaButton1.clicked.connect(self.touch)
        self.ui.osanaButton2.clicked.connect(self.touch)


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
