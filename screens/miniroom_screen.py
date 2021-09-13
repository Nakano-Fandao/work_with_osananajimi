#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "../settings")))
from path_setting import PathSetting
PathSetting().__init__()

## ==> ROOM SCREEN
from ui_miniroom_screen import Ui_miniRoomScreen

class miniRoomScreen(QMainWindow):
    def __init__(self, RoomScreen, smapho_flag, chrome_flag):
        QMainWindow.__init__(self)

        #*------ UI setting -------
        self.ui = Ui_miniRoomScreen()
        self.ui.setupUi(self)
        #*-------------------------

        self.RoomScreen = RoomScreen
        self.smapho_flag = smapho_flag
        self.chrome_flag = chrome_flag

        self.init_buttons()
        self.init_objects()

        #slot,signal
        self.ui.smaphoButton.clicked.connect(self.switch_smapho)
        self.ui.chromeButton.clicked.connect(self.switch_chrome)
        self.ui.maximizeButton.clicked.connect(self.show_room)

    def show_room(self):
        #Room開く
        self.RoomScreen.show()
        self.hide()

    def mousePressEvent(self, event):
        self.__isDrag = True
        self.__startPos = event.pos()

    def mouseReleaseEvent(self, event):
        self.__isDrag = False

    def mouseMoveEvent(self, event):
        if self.__isDrag:
            self.move(self.mapToParent(event.pos() - self.__startPos))

    def init_objects(self):
        self.ui.blackFrame.hide()
        #* オブジェクトのレイヤー順
        self.ui.blackFrame.raise_()

    def init_buttons(self):
        if not self.smapho_flag:
            smapho_icon = QIcon()
            smapho_icon.addFile(u":/image/images/icons/gray_smapho.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.smaphoButton.setIcon(smapho_icon)

        if not self.chrome_flag:
            chrome_icon = QIcon()
            chrome_icon.addFile(u":/image/images/icons/gray_chrome.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.chromeButton.setIcon(chrome_icon)

    def switch_smapho(self):
        #* メイン側のボタンを変える
        self.RoomScreen.switch_smapho()

        #* ミニ側のボタンを変える
        if self.smapho_flag:
            print("Smapho detection deactivate")
            self.smapho_flag = False
            smapho_icon = QIcon()
            smapho_icon.addFile(u":/image/images/icons/gray_smapho.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            print("Smapho detection activate")
            self.smapho_flag = True
            smapho_icon = QIcon()
            smapho_icon.addFile(u":/image/images/icons/pink_smapho.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.smaphoButton.setIconSize(QSize(55, 55))
        QTimer.singleShot(100, lambda: self.ui.smaphoButton.setIconSize(QSize(51, 51)))
        QTimer.singleShot(110, lambda: self.ui.smaphoButton.setIcon(smapho_icon))

    def switch_chrome(self):
        #* メイン側のボタンを変える
        self.RoomScreen.switch_chrome()

        #* ミニ側のボタンを変える
        if self.chrome_flag:
            print("Chrome detection deactivate")
            self.chrome_flag = False
            chrome_icon = QIcon()
            chrome_icon.addFile(u":/image/images/icons/gray_chrome.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            print("Chrome detection activate")
            self.chrome_flag = True
            chrome_icon = QIcon()
            chrome_icon.addFile(u":/image/images/icons/blue_chrome.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.chromeButton.setIconSize(QSize(55, 55))
        QTimer.singleShot(100, lambda: self.ui.chromeButton.setIconSize(QSize(51, 51)))
        QTimer.singleShot(110, lambda: self.ui.chromeButton.setIcon(chrome_icon))