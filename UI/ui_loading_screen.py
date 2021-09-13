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
        LoadingScreen.resize(800, 600)
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
        self.loadingLabel.setPixmap(QPixmap(u":/image/images/sentences/loading2.png"))
        self.loadingLabel.setScaledContents(True)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(190, 250, 430, 80))
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"	background-color: transparent;\n"
"	border: 0;	\n"
"}")
        LoadingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingScreen)

        QMetaObject.connectSlotsByName(LoadingScreen)
    # setupUi

    def retranslateUi(self, LoadingScreen):
        LoadingScreen.setWindowTitle(QCoreApplication.translate("LoadingScreen", u"MainWindow", None))
        self.backgroundLabel.setText("")
        self.loadingLabel.setText("")
    # retranslateUi

