# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'room_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_RoomScreen(object):
    def setupUi(self, RoomScreen):
        if not RoomScreen.objectName():
            RoomScreen.setObjectName(u"RoomScreen")
        RoomScreen.resize(800, 600)
        self.centralwidget = QWidget(RoomScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.insideRoomLabel = QLabel(self.centralwidget)
        self.insideRoomLabel.setObjectName(u"insideRoomLabel")
        self.insideRoomLabel.setGeometry(QRect(0, 0, 800, 600))
        self.insideRoomLabel.setPixmap(QPixmap(u":/image/images/backgrounds/inside.jpg"))
        self.osanaText = QTextBrowser(self.centralwidget)
        self.osanaText.setObjectName(u"osanaText")
        self.osanaText.setGeometry(QRect(30, 470, 740, 105))
        self.osanaText.setStyleSheet(u"QTextBrowser {\n"
"	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"}")
        self.osanaLabel = QLabel(self.centralwidget)
        self.osanaLabel.setObjectName(u"osanaLabel")
        self.osanaLabel.setGeometry(QRect(220, 40, 370, 470))
        self.osanaLabel.setPixmap(QPixmap(u":/image/images/character/figure1.png"))
        self.osanaLabel.setScaledContents(True)
        self.serifButton = QPushButton(self.centralwidget)
        self.serifButton.setObjectName(u"serifButton")
        self.serifButton.setGeometry(QRect(20, 410, 140, 45))
        self.serifButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.finishButton = QPushButton(self.centralwidget)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(677, 414, 101, 40))
        self.finishButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.finishButton.setIconSize(QSize(108, 79))
        self.windowLabel = QLabel(self.centralwidget)
        self.windowLabel.setObjectName(u"windowLabel")
        self.windowLabel.setGeometry(QRect(20, 405, 760, 182))
        self.windowLabel.setStyleSheet(u"")
        self.windowLabel.setPixmap(QPixmap(u":/image/images/windows/textbox_serif.png"))
        self.windowLabel.setScaledContents(True)
        self.blackFrame = QFrame(self.centralwidget)
        self.blackFrame.setObjectName(u"blackFrame")
        self.blackFrame.setEnabled(True)
        self.blackFrame.setGeometry(QRect(0, 0, 800, 600))
        self.blackFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(0, 0, 0, 0.4);\n"
"}")
        self.blackFrame.setFrameShape(QFrame.StyledPanel)
        self.blackFrame.setFrameShadow(QFrame.Raised)
        self.logView = QListView(self.centralwidget)
        self.logView.setObjectName(u"logView")
        self.logView.setGeometry(QRect(370, 470, 400, 100))
        self.logView.setFocusPolicy(Qt.NoFocus)
        self.logView.setStyleSheet(u"QListView {\n"
"	background: transparent;\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"QListView::item{\n"
"	padding: 4px;\n"
"	border: .3px solid white;\n"
"	border-radius: 10px;\n"
"	margin-top: 10px;\n"
"	color: black;\n"
"	font-size: 1.5em;\n"
"}\n"
"QListView::item:hover{\n"
"	background-color: rgba(0, 0, 0, 0.7);\n"
"}")
        self.logView.setWordWrap(True)
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setEnabled(True)
        self.timeEdit.setGeometry(QRect(300, 510, 180, 50))
        font = QFont()
        font.setFamily(u"Gill Sans MT")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.timeEdit.setFont(font)
        self.timeEdit.setCursor(QCursor(Qt.UpArrowCursor))
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 5, 0)))
        self.logButton = QPushButton(self.centralwidget)
        self.logButton.setObjectName(u"logButton")
        self.logButton.setGeometry(QRect(577, 414, 101, 40))
        self.logButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.logButton.setIconSize(QSize(108, 79))
        self.breakButton = QPushButton(self.centralwidget)
        self.breakButton.setObjectName(u"breakButton")
        self.breakButton.setGeometry(QRect(477, 414, 101, 40))
        self.breakButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.breakButton.setIconSize(QSize(108, 79))
        self.timerButton = QPushButton(self.centralwidget)
        self.timerButton.setObjectName(u"timerButton")
        self.timerButton.setGeometry(QRect(377, 414, 101, 40))
        self.timerButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.timerButton.setIconSize(QSize(108, 79))
        self.logBackLabel = QLabel(self.centralwidget)
        self.logBackLabel.setObjectName(u"logBackLabel")
        self.logBackLabel.setGeometry(QRect(370, 470, 400, 100))
        self.logBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_log.png"))
        self.logBackLabel.setScaledContents(True)
        self.finishLabel = QLabel(self.centralwidget)
        self.finishLabel.setObjectName(u"finishLabel")
        self.finishLabel.setGeometry(QRect(670, 410, 108, 79))
        self.finishLabel.setPixmap(QPixmap(u":/image/images/windows/button_finish.png"))
        self.logLabel = QLabel(self.centralwidget)
        self.logLabel.setObjectName(u"logLabel")
        self.logLabel.setGeometry(QRect(570, 410, 108, 79))
        self.logLabel.setPixmap(QPixmap(u":/image/images/windows/button_log.png"))
        self.breakLabel = QLabel(self.centralwidget)
        self.breakLabel.setObjectName(u"breakLabel")
        self.breakLabel.setGeometry(QRect(470, 410, 108, 79))
        self.breakLabel.setPixmap(QPixmap(u":/image/images/windows/button_break.png"))
        self.timerLabel = QLabel(self.centralwidget)
        self.timerLabel.setObjectName(u"timerLabel")
        self.timerLabel.setGeometry(QRect(370, 410, 108, 79))
        self.timerLabel.setPixmap(QPixmap(u":/image/images/windows/button_timer.png"))
        self.timerBackLabel = QLabel(self.centralwidget)
        self.timerBackLabel.setObjectName(u"timerBackLabel")
        self.timerBackLabel.setGeometry(QRect(110, 470, 400, 100))
        self.timerBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_log.png"))
        self.timerBackLabel.setScaledContents(True)
        self.breakBackLabel = QLabel(self.centralwidget)
        self.breakBackLabel.setObjectName(u"breakBackLabel")
        self.breakBackLabel.setGeometry(QRect(210, 470, 400, 100))
        self.breakBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_break.png"))
        self.breakBackLabel.setScaledContents(True)
        self.finishBackLabel = QLabel(self.centralwidget)
        self.finishBackLabel.setObjectName(u"finishBackLabel")
        self.finishBackLabel.setGeometry(QRect(380, 470, 400, 100))
        self.finishBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_finish.png"))
        self.finishBackLabel.setScaledContents(True)
        self.breakSentence = QLabel(self.centralwidget)
        self.breakSentence.setObjectName(u"breakSentence")
        self.breakSentence.setGeometry(QRect(130, 510, 180, 50))
        self.breakSentence.setPixmap(QPixmap(u":/image/images/sentences/breakSentence.png"))
        self.breakSentence.setScaledContents(True)
        RoomScreen.setCentralWidget(self.centralwidget)
        self.insideRoomLabel.raise_()
        self.blackFrame.raise_()
        self.osanaLabel.raise_()
        self.timerBackLabel.raise_()
        self.timeEdit.raise_()
        self.breakSentence.raise_()
        self.finishBackLabel.raise_()
        self.breakBackLabel.raise_()
        self.logBackLabel.raise_()
        self.logView.raise_()
        self.finishLabel.raise_()
        self.logLabel.raise_()
        self.breakLabel.raise_()
        self.timerLabel.raise_()
        self.windowLabel.raise_()
        self.osanaText.raise_()
        self.serifButton.raise_()
        self.breakButton.raise_()
        self.finishButton.raise_()
        self.logButton.raise_()
        self.timerButton.raise_()

        self.retranslateUi(RoomScreen)

        QMetaObject.connectSlotsByName(RoomScreen)
    # setupUi

    def retranslateUi(self, RoomScreen):
        RoomScreen.setWindowTitle(QCoreApplication.translate("RoomScreen", u"MainWindow", None))
        self.insideRoomLabel.setText("")
        self.osanaText.setMarkdown(QCoreApplication.translate("RoomScreen", u"\u3077\u3063\u3001\u306a\u306b\u305d\u308c\u3002\u305d\u3082\u305d\u3082\u4ed8\u304d\u5408\u3046\u6c17\u306a\u304b\u3063\u305f\u3088\u3002\u3042\u3063\u3001\u5b89\u5fc3\u3057\u3066\u308b\uff1f\u3075\u3075\u3001\u305c\u30fc\u3093\u3076\u304a\u898b\u901a\u3057\u3063\u3066\u308f\u3051\uff57\n"
"\n"
"", None))
        self.osanaText.setHtml(QCoreApplication.translate("RoomScreen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u30e1\u30a4\u30ea\u30aa'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u3077\u3063\u3001\u306a\u306b\u305d\u308c\u3002\u305d\u3082\u305d\u3082\u4ed8\u304d\u5408\u3046\u6c17\u306a\u304b\u3063\u305f\u3088\u3002\u3042\u3063\u3001\u5b89\u5fc3\u3057\u3066\u308b\uff1f\u3075\u3075\u3001\u305c\u30fc\u3093\u3076\u304a\u898b\u901a\u3057\u3063\u3066\u308f\u3051\uff57</p></body></html>", None))
        self.osanaLabel.setText("")
        self.serifButton.setText("")
        self.finishButton.setText("")
        self.windowLabel.setText("")
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("RoomScreen", u"mm:ss", None))
        self.logButton.setText("")
        self.breakButton.setText("")
        self.timerButton.setText("")
        self.logBackLabel.setText("")
        self.finishLabel.setText("")
        self.logLabel.setText("")
        self.breakLabel.setText("")
        self.timerLabel.setText("")
        self.timerBackLabel.setText("")
        self.breakBackLabel.setText("")
        self.finishBackLabel.setText("")
        self.breakSentence.setText("")
    # retranslateUi

