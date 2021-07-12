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
        RoomScreen.resize(796, 591)
        self.centralwidget = QWidget(RoomScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.insideRoomLabel = QLabel(self.centralwidget)
        self.insideRoomLabel.setObjectName(u"insideRoomLabel")
        self.insideRoomLabel.setGeometry(QRect(0, 0, 800, 600))
        self.insideRoomLabel.setPixmap(QPixmap(u":/image/images/backgrounds/inside.jpg"))
        self.osanaText = QTextBrowser(self.centralwidget)
        self.osanaText.setObjectName(u"osanaText")
        self.osanaText.setGeometry(QRect(30, 470, 740, 105))
        self.osanaText.setStyleSheet(u"font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"")
        self.osanaLabel = QLabel(self.centralwidget)
        self.osanaLabel.setObjectName(u"osanaLabel")
        self.osanaLabel.setGeometry(QRect(220, 40, 370, 470))
        self.osanaLabel.setPixmap(QPixmap(u":/image/images/character/figure1.png"))
        self.osanaLabel.setScaledContents(True)
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
        self.blackFrameButton = QPushButton(self.blackFrame)
        self.blackFrameButton.setObjectName(u"blackFrameButton")
        self.blackFrameButton.setGeometry(QRect(0, 0, 800, 600))
        self.blackFrameButton.setStyleSheet(u"background-color: transparent;")
        self.logView = QListView(self.centralwidget)
        self.logView.setObjectName(u"logView")
        self.logView.setGeometry(QRect(370, 470, 400, 100))
        self.logView.setFocusPolicy(Qt.NoFocus)
        self.logView.setStyleSheet(u"QListView {\n"
"	background: transparent;\n"
"	font-size: 20px;\n"
"	line-height: 25px;\n"
"	padding-top: 70px;\n"
"}\n"
"QListView::item{\n"
"	width: 325px;\n"
"	padding: 0px 8px -1px;\n"
"	border: .3px solid white;\n"
"	border-radius: 5px;\n"
"	margin: 1px 30px 1px 35px;\n"
"	color: black;\n"
"}\n"
"QListView::item:hover{\n"
"	background-color: rgba(255, 225, 148, 0.3);\n"
"}")
        self.logView.setWordWrap(True)
        self.timerTimeEdit = QTimeEdit(self.centralwidget)
        self.timerTimeEdit.setObjectName(u"timerTimeEdit")
        self.timerTimeEdit.setEnabled(True)
        self.timerTimeEdit.setGeometry(QRect(300, 510, 180, 50))
        font = QFont()
        font.setFamily(u"Gill Sans MT")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.timerTimeEdit.setFont(font)
        self.timerTimeEdit.setCursor(QCursor(Qt.UpArrowCursor))
        self.timerTimeEdit.setAlignment(Qt.AlignCenter)
        self.timerTimeEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 5, 0)))
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
        self.timerBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_timer.png"))
        self.timerBackLabel.setScaledContents(True)
        self.breakBackLabel = QLabel(self.centralwidget)
        self.breakBackLabel.setObjectName(u"breakBackLabel")
        self.breakBackLabel.setGeometry(QRect(210, 470, 400, 100))
        self.breakBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_break.png"))
        self.breakBackLabel.setScaledContents(True)
        self.finishBackLabel = QLabel(self.centralwidget)
        self.finishBackLabel.setObjectName(u"finishBackLabel")
        self.finishBackLabel.setGeometry(QRect(665, 470, 110, 100))
        self.finishBackLabel.setStyleSheet(u"")
        self.finishBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_finish.png"))
        self.finishBackLabel.setScaledContents(False)
        self.timerSentence = QLabel(self.centralwidget)
        self.timerSentence.setObjectName(u"timerSentence")
        self.timerSentence.setGeometry(QRect(130, 510, 180, 50))
        self.timerSentence.setPixmap(QPixmap(u":/image/images/sentences/breakSentence.png"))
        self.timerSentence.setScaledContents(True)
        self.remainingStudyTime = QLabel(self.centralwidget)
        self.remainingStudyTime.setObjectName(u"remainingStudyTime")
        self.remainingStudyTime.setGeometry(QRect(110, 10, 300, 60))
        font1 = QFont()
        font1.setFamily(u"Let's go Digital")
        font1.setPointSize(36)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(9)
        self.remainingStudyTime.setFont(font1)
        self.remainingStudyTime.setStyleSheet(u"font: 75 italic 36pt \"Let's go Digital\";\n"
"color: red;")
        self.remainingStudyTimeShadow = QLabel(self.centralwidget)
        self.remainingStudyTimeShadow.setObjectName(u"remainingStudyTimeShadow")
        self.remainingStudyTimeShadow.setGeometry(QRect(110, 10, 300, 60))
        self.remainingStudyTimeShadow.setFont(font1)
        self.remainingStudyTimeShadow.setStyleSheet(u"font: 75 italic 36pt \"Let's go Digital\";\n"
"color: rgb(58, 58, 58);")
        self.breakTimeEdit = QTimeEdit(self.centralwidget)
        self.breakTimeEdit.setObjectName(u"breakTimeEdit")
        self.breakTimeEdit.setEnabled(True)
        self.breakTimeEdit.setGeometry(QRect(400, 510, 180, 50))
        self.breakTimeEdit.setFont(font)
        self.breakTimeEdit.setCursor(QCursor(Qt.UpArrowCursor))
        self.breakTimeEdit.setAlignment(Qt.AlignCenter)
        self.breakTimeEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 5, 0)))
        self.breakSentence = QLabel(self.centralwidget)
        self.breakSentence.setObjectName(u"breakSentence")
        self.breakSentence.setGeometry(QRect(230, 510, 180, 50))
        self.breakSentence.setPixmap(QPixmap(u":/image/images/sentences/breakSentence.png"))
        self.breakSentence.setScaledContents(True)
        self.timerStartButton = QPushButton(self.centralwidget)
        self.timerStartButton.setObjectName(u"timerStartButton")
        self.timerStartButton.setGeometry(QRect(215, 510, 180, 50))
        self.timerStartButton.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/image/images/sentences/timerStartButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.timerStartButton.setIcon(icon)
        self.timerStartButton.setIconSize(QSize(180, 50))
        self.breakStartButton = QPushButton(self.centralwidget)
        self.breakStartButton.setObjectName(u"breakStartButton")
        self.breakStartButton.setGeometry(QRect(315, 510, 180, 50))
        self.breakStartButton.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/image/images/sentences/breakStartButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.breakStartButton.setIcon(icon1)
        self.breakStartButton.setIconSize(QSize(180, 50))
        self.finishNoButton = QPushButton(self.centralwidget)
        self.finishNoButton.setObjectName(u"finishNoButton")
        self.finishNoButton.setGeometry(QRect(670, 520, 100, 40))
        self.finishNoButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	font: 75 20pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(0,0,0,0.7);\n"
"	color: white;\n"
"}")
        self.finishYesButton = QPushButton(self.centralwidget)
        self.finishYesButton.setObjectName(u"finishYesButton")
        self.finishYesButton.setGeometry(QRect(670, 470, 100, 40))
        self.finishYesButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	font: 75 20pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(0,0,0,0.7);\n"
"	color: white;\n"
"}")
        self.remainingBreakTime = QLabel(self.centralwidget)
        self.remainingBreakTime.setObjectName(u"remainingBreakTime")
        self.remainingBreakTime.setGeometry(QRect(110, 70, 300, 60))
        self.remainingBreakTime.setFont(font1)
        self.remainingBreakTime.setStyleSheet(u"font: 75 italic 36pt \"Let's go Digital\";\n"
"color: skyblue;")
        self.remainingBreakTimeShadow = QLabel(self.centralwidget)
        self.remainingBreakTimeShadow.setObjectName(u"remainingBreakTimeShadow")
        self.remainingBreakTimeShadow.setGeometry(QRect(110, 70, 300, 60))
        self.remainingBreakTimeShadow.setFont(font1)
        self.remainingBreakTimeShadow.setStyleSheet(u"font: 75 italic 36pt \"Let's go Digital\";\n"
"color: rgb(58, 58, 58);")
        self.studyTimerLabel = QLabel(self.centralwidget)
        self.studyTimerLabel.setObjectName(u"studyTimerLabel")
        self.studyTimerLabel.setGeometry(QRect(10, 12, 90, 60))
        self.studyTimerLabel.setStyleSheet(u"font: 75 24pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"color: pink;")
        self.studyTimerLabel.setAlignment(Qt.AlignCenter)
        self.breakTimerLabel = QLabel(self.centralwidget)
        self.breakTimerLabel.setObjectName(u"breakTimerLabel")
        self.breakTimerLabel.setGeometry(QRect(10, 73, 90, 60))
        self.breakTimerLabel.setStyleSheet(u"font: 75 24pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"color: pink;")
        self.breakTimerLabel.setAlignment(Qt.AlignCenter)
        RoomScreen.setCentralWidget(self.centralwidget)
        self.insideRoomLabel.raise_()
        self.blackFrame.raise_()
        self.osanaLabel.raise_()
        self.timerBackLabel.raise_()
        self.timerStartButton.raise_()
        self.breakBackLabel.raise_()
        self.breakStartButton.raise_()
        self.breakTimeEdit.raise_()
        self.breakSentence.raise_()
        self.timerTimeEdit.raise_()
        self.timerSentence.raise_()
        self.logBackLabel.raise_()
        self.logView.raise_()
        self.logLabel.raise_()
        self.breakLabel.raise_()
        self.timerLabel.raise_()
        self.remainingStudyTimeShadow.raise_()
        self.remainingStudyTime.raise_()
        self.finishBackLabel.raise_()
        self.finishLabel.raise_()
        self.finishYesButton.raise_()
        self.finishNoButton.raise_()
        self.windowLabel.raise_()
        self.osanaText.raise_()
        self.breakButton.raise_()
        self.finishButton.raise_()
        self.logButton.raise_()
        self.timerButton.raise_()
        self.remainingBreakTimeShadow.raise_()
        self.remainingBreakTime.raise_()
        self.studyTimerLabel.raise_()
        self.breakTimerLabel.raise_()

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
        self.finishButton.setText("")
        self.windowLabel.setText("")
        self.blackFrameButton.setText(QCoreApplication.translate("RoomScreen", u"PushButton", None))
        self.timerTimeEdit.setDisplayFormat(QCoreApplication.translate("RoomScreen", u"hh:mm:ss", None))
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
        self.timerSentence.setText("")
        self.remainingStudyTime.setText(QCoreApplication.translate("RoomScreen", u"0 1:00: 12", None))
        self.remainingStudyTimeShadow.setText(QCoreApplication.translate("RoomScreen", u"88:88:88", None))
        self.breakTimeEdit.setDisplayFormat(QCoreApplication.translate("RoomScreen", u"mm:ss", None))
        self.breakSentence.setText("")
        self.timerStartButton.setText("")
        self.breakStartButton.setText("")
        self.finishNoButton.setText(QCoreApplication.translate("RoomScreen", u"\u3044\u3044\u3048", None))
        self.finishYesButton.setText(QCoreApplication.translate("RoomScreen", u"\u306f\u3044", None))
        self.remainingBreakTime.setText(QCoreApplication.translate("RoomScreen", u"0 1:00: 12", None))
        self.remainingBreakTimeShadow.setText(QCoreApplication.translate("RoomScreen", u"88:88:88", None))
        self.studyTimerLabel.setText(QCoreApplication.translate("RoomScreen", u"\u52c9\u5f37", None))
        self.breakTimerLabel.setText(QCoreApplication.translate("RoomScreen", u"\u4f11\u61a9", None))
    # retranslateUi

