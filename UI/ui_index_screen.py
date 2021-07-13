# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc
import files_rc

class Ui_IndexScreen(object):
    def setupUi(self, IndexScreen):
        if not IndexScreen.objectName():
            IndexScreen.setObjectName(u"IndexScreen")
        IndexScreen.resize(800, 600)
        self.centralwidget = QWidget(IndexScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setStyleSheet(u"")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.osanaLabel = QLabel(self.mainFrame)
        self.osanaLabel.setObjectName(u"osanaLabel")
        self.osanaLabel.setGeometry(QRect(440, 50, 421, 551))
        self.osanaLabel.setAutoFillBackground(False)
        self.osanaLabel.setPixmap(QPixmap(u":/image/images/character/figure1.png"))
        self.osanaLabel.setScaledContents(True)
        self.backgroundLabel = QLabel(self.mainFrame)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(0, 0, 800, 600))
        self.backgroundLabel.setPixmap(QPixmap(u":/image/images/backgrounds/index.png"))
        self.backgroundLabel.setScaledContents(True)
        self.startButton = QPushButton(self.mainFrame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(70, 390, 306, 63))
        self.startButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/image/images/sentences/startButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QSize(306, 63))
        self.finishButton = QPushButton(self.mainFrame)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(150, 500, 306, 63))
        icon1 = QIcon()
        icon1.addFile(u":/image/images/sentences/finishButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.finishButton.setIcon(icon1)
        self.finishButton.setIconSize(QSize(306, 63))
        self.osanaButton1 = QPushButton(self.mainFrame)
        self.osanaButton1.setObjectName(u"osanaButton1")
        self.osanaButton1.setGeometry(QRect(570, 70, 191, 351))
        self.osanaButton1.setStyleSheet(u"QPushButton{background: transparent;}")
        self.osanaButton2 = QPushButton(self.mainFrame)
        self.osanaButton2.setObjectName(u"osanaButton2")
        self.osanaButton2.setGeometry(QRect(500, 390, 191, 211))
        self.osanaButton2.setStyleSheet(u"QPushButton{background: transparent;}")
        self.moodDisplayLabel = QLabel(self.mainFrame)
        self.moodDisplayLabel.setObjectName(u"moodDisplayLabel")
        self.moodDisplayLabel.setGeometry(QRect(30, 280, 400, 60))
        self.moodDisplayLabel.setPixmap(QPixmap(u":/image/images/sentences/mood_normal.png"))
        self.moodDisplayLabel.setScaledContents(True)
        self.moodUpButton = QPushButton(self.mainFrame)
        self.moodUpButton.setObjectName(u"moodUpButton")
        self.moodUpButton.setGeometry(QRect(440, 275, 35, 35))
        font = QFont()
        font.setFamily(u"MS UI Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.moodUpButton.setFont(font)
        self.moodUpButton.setStyleSheet(u"font: 28pt \"MS UI Gothic\";\n"
"color: red;\n"
"background-color: transparent;")
        self.moodDownButton = QPushButton(self.mainFrame)
        self.moodDownButton.setObjectName(u"moodDownButton")
        self.moodDownButton.setGeometry(QRect(440, 305, 35, 35))
        self.moodDownButton.setFont(font)
        self.moodDownButton.setStyleSheet(u"font: 28pt \"MS UI Gothic\";\n"
"color: blue;\n"
"background-color: transparent;")
        self.moodUpLabel = QLabel(self.mainFrame)
        self.moodUpLabel.setObjectName(u"moodUpLabel")
        self.moodUpLabel.setGeometry(QRect(460, 240, 70, 50))
        self.moodUpLabel.setStyleSheet(u"font: 75 26pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"color: rgba(255, 169, 0, 1);")
        self.moodDownLabel = QLabel(self.mainFrame)
        self.moodDownLabel.setObjectName(u"moodDownLabel")
        self.moodDownLabel.setGeometry(QRect(460, 330, 70, 50))
        self.moodDownLabel.setStyleSheet(u"font: 75 26pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"color: rgba(18, 93, 152, 1);")
        self.backgroundLabel.raise_()
        self.osanaLabel.raise_()
        self.startButton.raise_()
        self.finishButton.raise_()
        self.osanaButton1.raise_()
        self.osanaButton2.raise_()
        self.moodDisplayLabel.raise_()
        self.moodUpButton.raise_()
        self.moodDownButton.raise_()
        self.moodUpLabel.raise_()
        self.moodDownLabel.raise_()

        self.verticalLayout.addWidget(self.mainFrame)

        IndexScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(IndexScreen)

        QMetaObject.connectSlotsByName(IndexScreen)
    # setupUi

    def retranslateUi(self, IndexScreen):
        IndexScreen.setWindowTitle(QCoreApplication.translate("IndexScreen", u"IndexScreen", None))
        self.osanaLabel.setText("")
        self.backgroundLabel.setText("")
        self.startButton.setText("")
        self.finishButton.setText("")
        self.osanaButton1.setText("")
        self.osanaButton2.setText("")
        self.moodDisplayLabel.setText("")
        self.moodUpButton.setText(QCoreApplication.translate("IndexScreen", u"\u25b2", None))
        self.moodDownButton.setText(QCoreApplication.translate("IndexScreen", u"\u25bc", None))
        self.moodUpLabel.setText(QCoreApplication.translate("IndexScreen", u"+10", None))
        self.moodDownLabel.setText(QCoreApplication.translate("IndexScreen", u"-10", None))
    # retranslateUi

