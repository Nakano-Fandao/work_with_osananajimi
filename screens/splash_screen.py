#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsDropShadowEffect
from PySide2.QtMultimedia import QSound

## ==> MAIN WINDOW
from index_screen import IndexScreen

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> GLOBALS
counter = 0

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER of 25 ms * 100
        self.timer.start(25)

        # CHANGE DESCRIPTION
        # Initial Text
        self.ui.label_description.setText("<strong>幼馴染</strong> に電話しています。")
        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>幼馴染</strong>があなたの部屋に来ることを了承しました。"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>幼馴染が</strong>あなたの部屋に向かっています。"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = IndexScreen()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        if counter == 80:
            QSound.play(":effect/sounds/effects/door_knocking.wav")

        # INCREASE COUNTER
        counter += 1
