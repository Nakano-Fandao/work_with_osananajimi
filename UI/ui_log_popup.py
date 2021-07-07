# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_popup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_LogPopup(object):
    def setupUi(self, LogPopup):
        if not LogPopup.objectName():
            LogPopup.setObjectName(u"LogPopup")
        LogPopup.resize(400, 600)
        LogPopup.setStyleSheet(u"")
        self.listFrame = QFrame(LogPopup)
        self.listFrame.setObjectName(u"listFrame")
        self.listFrame.setGeometry(QRect(0, 0, 400, 600))
        self.listFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(0, 0, 0, 0.4);\n"
"}")
        self.listFrame.setFrameShape(QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QFrame.Raised)
        self.backgroundLabel = QLabel(LogPopup)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(0, 0, 400, 600))
        self.backgroundLabel.setPixmap(QPixmap(u":/image/images/backgrounds/log.jpg"))
        self.logList = QListView(LogPopup)
        self.logList.setObjectName(u"logList")
        self.logList.setGeometry(QRect(5, 35, 390, 560))
        self.logList.setFocusPolicy(Qt.NoFocus)
        self.logList.setStyleSheet(u"QListView {\n"
"	border-radius: 10px;\n"
"	background: transparent;\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"QListView::item{\n"
"	background-color: rgba(0, 0, 0, 0.5);\n"
"	padding: 4px;\n"
"	border: .3px solid white;\n"
"	border-radius: 10px;\n"
"	margin-top: 10px;\n"
"	color: white;\n"
"	font-size: 1.5em;\n"
"}\n"
"QListView::item:hover{\n"
"	background-color: rgba(0, 0, 0, 0.7);\n"
"}")
        self.logList.setProperty("isWrapping", False)
        self.logList.setModelColumn(0)
        self.logList.setUniformItemSizes(False)
        self.logList.setWordWrap(True)
        self.logList.setSelectionRectVisible(False)
        self.exitButton = QPushButton(LogPopup)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(350, 0, 50, 35))
        self.exitButton.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/image/images/icons/cil-x.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/image/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon)
        self.logScreenTitleLabel = QLabel(LogPopup)
        self.logScreenTitleLabel.setObjectName(u"logScreenTitleLabel")
        self.logScreenTitleLabel.setGeometry(QRect(0, 0, 350, 35))
        self.logScreenTitleLabel.setStyleSheet(u"QLabel {\n"
"	background-color: black;\n"
"	font: 75 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"	width: 350px;\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.backgroundLabel.raise_()
        self.listFrame.raise_()
        self.logList.raise_()
        self.exitButton.raise_()
        self.logScreenTitleLabel.raise_()

        self.retranslateUi(LogPopup)

        QMetaObject.connectSlotsByName(LogPopup)
    # setupUi

    def retranslateUi(self, LogPopup):
        LogPopup.setWindowTitle(QCoreApplication.translate("LogPopup", u"Form", None))
        self.backgroundLabel.setText("")
        self.exitButton.setText("")
        self.logScreenTitleLabel.setText(QCoreApplication.translate("LogPopup", u"\u4f1a\u8a71\u30ed\u30b0", None))
    # retranslateUi

