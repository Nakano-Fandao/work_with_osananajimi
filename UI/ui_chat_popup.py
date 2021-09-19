# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_popup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_ChatPopup(object):
    def setupUi(self, ChatPopup):
        if not ChatPopup.objectName():
            ChatPopup.setObjectName(u"ChatPopup")
        ChatPopup.resize(540, 300)
        ChatPopup.setStyleSheet(u"")
        self.chatList = QListWidget(ChatPopup)
        self.chatList.setObjectName(u"chatList")
        self.chatList.setGeometry(QRect(0, 0, 540, 300))
        self.chatList.setFocusPolicy(Qt.NoFocus)
        self.chatList.setStyleSheet(u"QListWidget {\n"
"	border-radius: 10px;\n"
"	background: transparent;\n"
"	color: rgb(220, 220, 220);\n"
"	font: 75 20px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"}\n"
"QListWidget::item{\n"
"	width: 520px;\n"
"	height: 80px;\n"
"	background-color: rgba(0, 0, 0, 0.5);\n"
"	border: .3px solid white;\n"
"	border-radius: 10px;\n"
"	margin: 10px;\n"
"	color: white;\n"
"}\n"
"QListWidget::item:hover{\n"
"	background-color: rgba(0, 0, 0, 0.7);\n"
"}")
        self.chatList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chatList.setProperty("isWrapping", False)
        self.chatList.setUniformItemSizes(False)
        self.chatList.setWordWrap(True)
        self.backgroundLabel = QLabel(ChatPopup)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(0, 0, 540, 300))
        self.backgroundLabel.setPixmap(QPixmap(u":/image/images/backgrounds/room_day.jpg"))
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.raise_()
        self.chatList.raise_()

        self.retranslateUi(ChatPopup)

        QMetaObject.connectSlotsByName(ChatPopup)
    # setupUi

    def retranslateUi(self, ChatPopup):
        ChatPopup.setWindowTitle(QCoreApplication.translate("ChatPopup", u"Dialog", None))
        self.backgroundLabel.setText("")
    # retranslateUi

