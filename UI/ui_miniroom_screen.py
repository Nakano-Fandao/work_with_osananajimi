# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'miniroom_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_miniRoomScreen(object):
    def setupUi(self, miniRoomScreen):
        if not miniRoomScreen.objectName():
            miniRoomScreen.setObjectName(u"miniRoomScreen")
        miniRoomScreen.resize(240, 180)
        miniRoomScreen.setMinimumSize(QSize(0, 0))
        miniRoomScreen.setMaximumSize(QSize(400, 300))
        self.centralwidget = QWidget(miniRoomScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(400, 300))
        self.insideRoomLabel = QLabel(self.centralwidget)
        self.insideRoomLabel.setObjectName(u"insideRoomLabel")
        self.insideRoomLabel.setGeometry(QRect(0, 0, 240, 180))
        self.insideRoomLabel.setPixmap(QPixmap(u":/image/images/backgrounds/room_day.jpg"))
        self.insideRoomLabel.setScaledContents(True)
        self.hoverFrame = QFrame(self.centralwidget)
        self.hoverFrame.setObjectName(u"hoverFrame")
        self.hoverFrame.setGeometry(QRect(0, 0, 240, 180))
        self.hoverFrame.setStyleSheet(u"")
        self.hoverFrame.setFrameShape(QFrame.StyledPanel)
        self.hoverFrame.setFrameShadow(QFrame.Raised)
        self.smaphoButton = QPushButton(self.hoverFrame)
        self.smaphoButton.setObjectName(u"smaphoButton")
        self.smaphoButton.setGeometry(QRect(19, 120, 55, 55))
        self.smaphoButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.smaphoButton.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/image/images/icons/pink_smapho.png", QSize(), QIcon.Normal, QIcon.Off)
        self.smaphoButton.setIcon(icon)
        self.smaphoButton.setIconSize(QSize(51, 51))
        self.chromeButton = QPushButton(self.hoverFrame)
        self.chromeButton.setObjectName(u"chromeButton")
        self.chromeButton.setGeometry(QRect(93, 120, 55, 55))
        self.chromeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.chromeButton.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/image/images/icons/blue_chrome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chromeButton.setIcon(icon1)
        self.chromeButton.setIconSize(QSize(51, 51))
        self.maximizeButton = QPushButton(self.hoverFrame)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setGeometry(QRect(166, 120, 55, 55))
        self.maximizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeButton.setStyleSheet(u"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/image/images/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon2)
        self.maximizeButton.setIconSize(QSize(51, 51))
        self.chromeButton.raise_()
        self.smaphoButton.raise_()
        self.maximizeButton.raise_()
        self.osanaLabel = QLabel(self.centralwidget)
        self.osanaLabel.setObjectName(u"osanaLabel")
        self.osanaLabel.setGeometry(QRect(-130, -7, 600, 800))
        self.osanaLabel.setPixmap(QPixmap(u":/image/images/character/figure_good.png"))
        self.osanaLabel.setScaledContents(True)
        miniRoomScreen.setCentralWidget(self.centralwidget)
        self.insideRoomLabel.raise_()
        self.osanaLabel.raise_()
        self.hoverFrame.raise_()
        QWidget.setTabOrder(self.smaphoButton, self.chromeButton)
        QWidget.setTabOrder(self.chromeButton, self.maximizeButton)

        self.retranslateUi(miniRoomScreen)

        QMetaObject.connectSlotsByName(miniRoomScreen)
    # setupUi

    def retranslateUi(self, miniRoomScreen):
        miniRoomScreen.setWindowTitle(QCoreApplication.translate("miniRoomScreen", u"\u30df\u30cb\u753b\u9762", None))
        self.insideRoomLabel.setText("")
        self.smaphoButton.setText("")
        self.chromeButton.setText("")
        self.maximizeButton.setText("")
        self.osanaLabel.setText("")
    # retranslateUi

