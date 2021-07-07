# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'special_splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_SpecialSplashScreen(object):
    def setupUi(self, SpecialSplashScreen):
        if not SpecialSplashScreen.objectName():
            SpecialSplashScreen.setObjectName(u"SpecialSplashScreen")
        SpecialSplashScreen.resize(600, 450)
        SpecialSplashScreen.setMaximumSize(QSize(2048, 1536))
        self.centralwidget = QWidget(SpecialSplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.loadingLabel = QLabel(self.centralwidget)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setPixmap(QPixmap(u":/image/images/backgrounds/load_.png"))
        self.loadingLabel.setScaledContents(True)

        self.verticalLayout.addWidget(self.loadingLabel)

        SpecialSplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpecialSplashScreen)

        QMetaObject.connectSlotsByName(SpecialSplashScreen)
    # setupUi

    def retranslateUi(self, SpecialSplashScreen):
        SpecialSplashScreen.setWindowTitle(QCoreApplication.translate("SpecialSplashScreen", u"SplashWindow", None))
        self.loadingLabel.setText("")
    # retranslateUi

