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
        miniRoomScreen.resize(800, 600)
        miniRoomScreen.setMinimumSize(QSize(800, 600))
        miniRoomScreen.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(miniRoomScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.insideRoomLabel = QLabel(self.centralwidget)
        self.insideRoomLabel.setObjectName(u"insideRoomLabel")
        self.insideRoomLabel.setGeometry(QRect(0, 0, 800, 600))
        self.insideRoomLabel.setPixmap(QPixmap(u":/image/images/backgrounds/inside.jpg"))
        self.blackFrame = QFrame(self.centralwidget)
        self.blackFrame.setObjectName(u"blackFrame")
        self.blackFrame.setEnabled(True)
        self.blackFrame.setGeometry(QRect(0, 0, 800, 600))
        self.blackFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.blackFrame.setFrameShape(QFrame.StyledPanel)
        self.blackFrame.setFrameShadow(QFrame.Raised)
        self.osanaLabel = QLabel(self.blackFrame)
        self.osanaLabel.setObjectName(u"osanaLabel")
        self.osanaLabel.setGeometry(QRect(90, 40, 600, 800))
        self.osanaLabel.setPixmap(QPixmap(u":/image/images/character/figure1.png"))
        self.osanaLabel.setScaledContents(True)
        self.bigButton = QPushButton(self.blackFrame)
        self.bigButton.setObjectName(u"bigButton")
        self.bigButton.setGeometry(QRect(630, 20, 151, 161))
        miniRoomScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(miniRoomScreen)

        QMetaObject.connectSlotsByName(miniRoomScreen)
    # setupUi

    def retranslateUi(self, miniRoomScreen):
        miniRoomScreen.setWindowTitle(QCoreApplication.translate("miniRoomScreen", u"MainWindow", None))
        self.insideRoomLabel.setText("")
        self.osanaLabel.setText("")
        self.bigButton.setText(QCoreApplication.translate("miniRoomScreen", u"\u5927", None))
    # retranslateUi

