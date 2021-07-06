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
        ChatPopup.resize(540, 105)
        ChatPopup.setStyleSheet(u"background-color: #FF616D;")
        self.textBrowser_1 = QTextBrowser(ChatPopup)
        self.textBrowser_1.setObjectName(u"textBrowser_1")
        self.textBrowser_1.setGeometry(QRect(10, 10, 520, 85))
        self.textBrowser_1.setStyleSheet(u"QTextBrowser {\n"
"	background-color: #FFEAC9;\n"
"	border-radius: 15px;\n"
"	color: #343A40;\n"
"	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"}")
        self.pushButton_1 = QPushButton(ChatPopup)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(10, 10, 520, 85))
        self.pushButton_1.setStyleSheet(u"QPushButton{background: transparent;}")

        self.retranslateUi(ChatPopup)

        QMetaObject.connectSlotsByName(ChatPopup)
    # setupUi

    def retranslateUi(self, ChatPopup):
        ChatPopup.setWindowTitle(QCoreApplication.translate("ChatPopup", u"Dialog", None))
        self.textBrowser_1.setMarkdown("")
        self.textBrowser_1.setHtml(QCoreApplication.translate("ChatPopup", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u30e1\u30a4\u30ea\u30aa'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_1.setText("")
    # retranslateUi

