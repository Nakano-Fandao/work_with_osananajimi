# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        if not LoadingScreen.objectName():
            LoadingScreen.setObjectName(u"LoadingScreen")
        LoadingScreen.resize(796, 591)
        LoadingScreen.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/image/images/icons/pink_smapho.png", QSize(), QIcon.Normal, QIcon.Off)
        LoadingScreen.setWindowIcon(icon)
        self.centralwidget = QWidget(LoadingScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backgroundLabel = QLabel(self.centralwidget)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(0, 0, 800, 600))
        self.backgroundLabel.setPixmap(QPixmap(u":/image/images/backgrounds/loading_screen.png"))
        self.backgroundLabel.setScaledContents(True)
        self.loadingLabel = QLabel(self.centralwidget)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setGeometry(QRect(530, 530, 219, 50))
        self.loadingLabel.setScaledContents(True)
        self.tipsBrowser = QTextBrowser(self.centralwidget)
        self.tipsBrowser.setObjectName(u"tipsBrowser")
        self.tipsBrowser.setGeometry(QRect(170, 260, 470, 60))
        font = QFont()
        font.setFamily(u"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tipsBrowser.setFont(font)
        self.tipsBrowser.setContextMenuPolicy(Qt.NoContextMenu)
        self.tipsBrowser.setStyleSheet(u"QTextBrowser {\n"
"	background-color: transparent;\n"
"	border: 0;	\n"
"	font: 75 24px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"}")
        self.tipsBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tipsBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tipsBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tipsBrowser.setTabChangesFocus(True)
        LoadingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingScreen)

        QMetaObject.connectSlotsByName(LoadingScreen)
    # setupUi

    def retranslateUi(self, LoadingScreen):
        LoadingScreen.setWindowTitle(QCoreApplication.translate("LoadingScreen", u"Loading", None))
        self.backgroundLabel.setText("")
        self.loadingLabel.setText("")
        self.tipsBrowser.setHtml(QCoreApplication.translate("LoadingScreen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B'; font-size:24px; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u30bf\u30a4\u30c8\u30eb\u753b\u9762\u306e\u5e7c\u99b4\u67d3\u306b\u89e6\u308c\u3066\u307f\u308b\u3068\u306a\u306b\u304b\u304c\u6012\u308b\u30fb\u30fb\u30fb\uff1f</span></p></body></html>", None))
    # retranslateUi

