#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "../settings")))
from path_setting import PathSetting
PathSetting().__init__()

## ==> MAIN WINDOW
# from index_screen import IndexScreen

## ==> LOADING SCREEN
from ui_loading_screen import Ui_LoadingScreen

# LOADING SCREEN
class LoadingScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.load)
        self.timer.start(800)

        self.show()


    def load(self):

        path = u":image/images/sentences/loading{}.png".format(self.counter%2+1)

        self.ui.loadingLabel.setPixmap(QPixmap(path))

        self.counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingScreen()
    window.show()
    sys.exit(app.exec_())
