#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

## ==> MAIN WINDOW
# from index_screen import IndexScreen

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

    #     ## REMOVE TITLE BAR
    #     self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    #     self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    #     self.loading_list = [
    #         "load_",
    #         "load_0",
    #         "load_0_1",
    #         "load_1",
    #         "load_2",
    #         "load_3",
    #         "load_4",
    #         "load_5",
    #         "load_6",
    #         "load_7",
    #         "load_8",
    #         "load_9"
    #     ]

    #     self.counter = 0
    #     self.timer = QTimer()
    #     self.timer.timeout.connect(self.load)
    #     self.timer.start(300)

    #     self.show()


    # def load(self):

    #     load_png = self.loading_list[self.counter]
    #     path = u":image/images/backgrounds/{}.png".format(load_png)
    #     print(path)

    #     self.ui.loadingLabel.setPixmap(QPixmap(path))

    #     print(self.counter)
    #     self.counter += 1

    #     if self.counter == 12:
    #         self.timer.stop()
    #         self.main = IndexScreen()
    #         self.main.show()
    #         self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.show()
    sys.exit(app.exec_())
