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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(540, 308)
        Dialog.setStyleSheet(u"background-color: #FF616D;")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 10, 520, 85))
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"	background-color: #FFEAC9;\n"
"	border-radius: 15px;\n"
"	color: #343A40;\n"
"	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"}")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 520, 85))
        self.pushButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.textBrowser_2 = QTextBrowser(Dialog)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(10, 110, 520, 85))
        self.textBrowser_2.setStyleSheet(u"QTextBrowser {\n"
"	background-color: #FFEAC9;\n"
"	border-radius: 15px;\n"
"	color: #343A40;\n"
"	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"}")
        self.textBrowser_3 = QTextBrowser(Dialog)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(10, 210, 520, 85))
        self.textBrowser_3.setStyleSheet(u"QTextBrowser {\n"
"	background-color: #FFEAC9;\n"
"	border-radius: 15px;\n"
"	color: #343A40;\n"
"	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"}")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 110, 520, 85))
        self.pushButton_2.setStyleSheet(u"QPushButton{background: transparent;}")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 210, 520, 85))
        self.pushButton_3.setStyleSheet(u"QPushButton{background: transparent;}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setMarkdown(QCoreApplication.translate("Dialog", u"\u3048\u3063\u3001\u3088\u304b\u3063\u305f\u3058\u3083\u3093\u2026\u304a\u4f3c\u5408\u3044\u3060\u3088\n"
"\n"
"", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u30e1\u30a4\u30ea\u30aa'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u3048\u3063\u3001\u3088\u304b\u3063\u305f\u3058\u3083\u3093\u2026\u304a\u4f3c\u5408\u3044\u3060\u3088</p></body></html>", None))
        self.pushButton.setText("")
        self.textBrowser_2.setMarkdown(QCoreApplication.translate("Dialog", u"\u5acc\u3060\u5acc\u3060\u5acc\u3060\n"
"\n"
"", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u30e1\u30a4\u30ea\u30aa'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5acc\u3060\u5acc\u3060\u5acc\u3060</p></body></html>", None))
        self.textBrowser_3.setMarkdown(QCoreApplication.translate("Dialog", u"\u4ed8\u304d\u5408\u3046\u306e\u304b\u3001\u4ffa\u4ee5\u5916\u306e\u5974\u3068\u3002\n"
"\n"
"", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u30e1\u30a4\u30ea\u30aa'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4ed8\u304d\u5408\u3046\u306e\u304b\u3001\u4ffa\u4ee5\u5916\u306e\u5974\u3068\u3002</p></body></html>", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

