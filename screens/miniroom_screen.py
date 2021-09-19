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
        self.ui.chromeButton.hide()
        self.ui.maximizeButton.hide()
        self.ui.smaphoButton.hide()
        self.open_cur = QCursor()
        self.open_cur.setShape(Qt.OpenHandCursor)
        self.closed_cur = QCursor()
        self.closed_cur.setShape(Qt.ClosedHandCursor)
        self.pointer_cur = QCursor()
        self.pointer_cur.setShape(Qt.PointingHandCursor)
        self.ui.hoverFrame.setCursor(self.open_cur)
        #* REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        #*-------------------------

        self.room_screen = RoomScreen
        self.smapho_flag = smapho_flag
        self.chrome_flag = chrome_flag

        self.init_buttons()
        self.init_layers()

        #slot,signal
        self.ui.smaphoButton.clicked.connect(self.switch_smapho)
        self.ui.chromeButton.clicked.connect(self.switch_chrome)
        self.ui.maximizeButton.clicked.connect(self.show_room)

    def show_room(self):
        #* Roomを開く
        self.room_screen.show()
        self.room_screen.handle_miniroom_flag(False)
        self.close()

    def mousePressEvent(self, event):
        self.__isDrag = True
        self.__startPos = event.pos()
        self.ui.hoverFrame.setCursor(self.closed_cur)

    def mouseReleaseEvent(self, event):
        self.__isDrag = False
        self.ui.hoverFrame.setCursor(self.open_cur)

    def mouseMoveEvent(self, event):
        if self.__isDrag:
            self.move(self.mapToParent(event.pos() - self.__startPos))
            self.ui.hoverFrame.setCursor(self.closed_cur)

    def enterEvent(self, event):
        self.ui.chromeButton.show()
        self.ui.maximizeButton.show()
        self.ui.smaphoButton.show()
        self.ui.hoverFrame.setStyleSheet(u"QFrame { background-color: rgba(0, 0, 0, 0.5); }")

    def leaveEvent(self, event):
        self.ui.chromeButton.hide()
        self.ui.maximizeButton.hide()
        self.ui.smaphoButton.hide()
        self.ui.hoverFrame.setStyleSheet(u"QFrame { background-color: rgba(0, 0, 0, 0); }")

    def init_layers(self):
        #* オブジェクトのレイヤー順
        # self.ui.hoverFrame.raise_()
        pass

    def init_buttons(self):
        if not self.smapho_flag:
            smapho_icon = QIcon()
            smapho_icon.addFile(u":/image/images/icons/gray_smapho.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.smaphoButton.setIcon(smapho_icon)

        if not self.chrome_flag:
            chrome_icon = QIcon()
            chrome_icon.addFile(u":/image/images/icons/gray_chrome.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.chromeButton.setIcon(chrome_icon)

        self.ui.smaphoButton.setCursor(self.pointer_cur)
        self.ui.chromeButton.setCursor(self.pointer_cur)
        self.ui.maximizeButton.setCursor(self.pointer_cur)

    def switch_smapho(self):
        #* メイン側のボタンを変える
        self.room_screen.switch_smapho()

        #* ミニ側のボタンを変える
        if self.smapho_flag:
            print("Deactivate Smapho detection")
            self.smapho_flag = False
            smapho_icon = QIcon()
            smapho_icon.addFile(u":/image/images/icons/gray_smapho.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            print("Activate Smapho detection")
            self.smapho_flag = True
            smapho_icon = QIcon()
            smapho_icon.addFile(u":/image/images/icons/pink_smapho.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.smaphoButton.setIconSize(QSize(55, 55))
        QTimer.singleShot(100, lambda: self.ui.smaphoButton.setIconSize(QSize(51, 51)))
        QTimer.singleShot(110, lambda: self.ui.smaphoButton.setIcon(smapho_icon))

    def switch_chrome(self):
        #* メイン側のボタンを変える
        self.room_screen.switch_chrome()

        #* ミニ側のボタンを変える
        if self.chrome_flag:
            print("Deactivate Chrome detection")
            self.chrome_flag = False
            chrome_icon = QIcon()
            chrome_icon.addFile(u":/image/images/icons/gray_chrome.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            print("Activate Chrome detection")
            self.chrome_flag = True
            chrome_icon = QIcon()
            chrome_icon.addFile(u":/image/images/icons/blue_chrome.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.chromeButton.setIconSize(QSize(55, 55))
        QTimer.singleShot(100, lambda: self.ui.chromeButton.setIconSize(QSize(51, 51)))
        QTimer.singleShot(110, lambda: self.ui.chromeButton.setIcon(chrome_icon))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    miniroom_screen = miniRoomScreen(None, True, True)
    miniroom_screen.show()
    sys.exit(app.exec_())
