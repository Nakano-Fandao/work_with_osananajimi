#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys, json, os, random

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow
from PySide2.QtMultimedia import QSound

## ==> MAIN WINDOW
from room_screen import RoomScreen

## ==> INDEX SCREEN
from UI.ui_index_screen import Ui_IndexScreen

from play_voice import PlayVoice

## ==> Sound Effects
# import files_rc

# GUI FILE
# from app_modules import *

# YOUR APPLICATION
class IndexScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_IndexScreen()
        self.ui.setupUi(self)

        # 変数設定
        self.mood = "normal"

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Osananajimi arrives
        # door_knocking = correspondence_json["door_knocking"]
        # QSound.play(door_knocking)
        self.osana = PlayVoice()
        print("うぇ、幼馴染がきた")

        # Button setting
        self.ui.startButton.clicked.connect(self.start)
        self.ui.finishButton.clicked.connect(self.finish)
        self.ui.osanaButton1.clicked.connect(self.touch)
        self.ui.osanaButton2.clicked.connect(self.touch)


    def start(self):

        serif = self.osana.play_app_voice("start", self.mood)

        # SHOW ROOM SCREEN
        self.main = RoomScreen(self.mood, serif)
        self.main.show()

        # CLOSE INDEX SCREEN
        self.close()

    def finish(self):
        # 幼馴染が帰った
        sys.exit(-1)

    def touch(self):
        self.osana.play_app_voice("start", self.mood, True)
