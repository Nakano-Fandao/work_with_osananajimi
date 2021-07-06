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


class Ui_ChatPopup(object):
    def setupUi(self, ChatPopup):
        if not ChatPopup.objectName():
            ChatPopup.setObjectName(u"ChatPopup")
        ChatPopup.resize(540, 295)
        ChatPopup.setStyleSheet(u"background-color: #FF616D;")
        self.horizontalLayout = QHBoxLayout(ChatPopup)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.chatList = QListWidget(ChatPopup)
        self.chatList.setObjectName(u"chatList")
        self.chatList.setFocusPolicy(Qt.NoFocus)
        self.chatList.setStyleSheet(u"QListWidget::item {\n"
"	margin: 8px;\n"
"	padding-top: 20px;\n"
"	padding-bottom: 20px;\n"
"	margin-right: 8px;\n"
"	background-color: #FFEAC9;\n"
"	border-radius: 0px;\n"
"	color: #343A40;\n"
"	width: 520px;\n"
"	height: 40px;\n"
"	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"}\n"
"QListWidget::item:hover {\n"
"	margin: 10px;\n"
"	background-color: #FFFFC9;\n"
"	border-radius: 0px;\n"
"	color: #343A40;\n"
"	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"	word-wrap: true;\n"
"	\n"
"}")
        self.chatList.setUniformItemSizes(False)
        self.chatList.setWordWrap(True)

        self.horizontalLayout.addWidget(self.chatList)


        self.retranslateUi(ChatPopup)

        QMetaObject.connectSlotsByName(ChatPopup)
    # setupUi

    def retranslateUi(self, ChatPopup):
        ChatPopup.setWindowTitle(QCoreApplication.translate("ChatPopup", u"Dialog", None))
    # retranslateUi

