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
        RoomScreen.setMinimumSize(QSize(800, 600))
        RoomScreen.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(RoomScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.insideRoomLabel = QLabel(self.centralwidget)
        self.insideRoomLabel.setObjectName(u"insideRoomLabel")
        self.insideRoomLabel.setGeometry(QRect(0, 0, 800, 600))
        self.insideRoomLabel.setPixmap(QPixmap(u":/image/images/backgrounds/inside.jpg"))
        self.osanaText = QTextBrowser(self.centralwidget)
        self.osanaText.setObjectName(u"osanaText")
        self.osanaText.setGeometry(QRect(30, 470, 740, 105))
        self.osanaText.setStyleSheet(u"font: 75 24px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";")
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
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.blackFrame.setFrameShape(QFrame.StyledPanel)
        self.blackFrame.setFrameShadow(QFrame.Raised)
        self.blackFrameButton = QPushButton(self.blackFrame)
        self.blackFrameButton.setObjectName(u"blackFrameButton")
        self.blackFrameButton.setGeometry(QRect(0, 0, 800, 600))
        self.blackFrameButton.setStyleSheet(u"background-color: transparent;")
        self.logView = QListView(self.centralwidget)
        self.logView.setObjectName(u"logView")
        self.logView.setGeometry(QRect(410, 470, 330, 100))
        self.logView.setFocusPolicy(Qt.NoFocus)
        self.logView.setContextMenuPolicy(Qt.NoContextMenu)
        self.logView.setStyleSheet(u"QListView {\n"
"	background: transparent;\n"
"	font-size: 20px;\n"
"	line-height: 25px;\n"
"	border: 0;\n"
"}\n"
"QListView::item{\n"
"	width: 328px;\n"
"	padding: 0px 2px -1px;\n"
"	border: .3px solid white;\n"
"	border-radius: 5px;\n"
"	margin: 1px 1px 28px;\n"
"	color: black;\n"
"}\n"
"QListView::item:hover{\n"
"	background-color: rgba(255, 225, 148, 0.3);\n"
"}")
        self.logView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.logView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.logView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.logView.setWordWrap(True)
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
        self.logBackLabel.setGeometry(QRect(370, 460, 400, 100))
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
        self.finishBackLabel = QLabel(self.centralwidget)
        self.finishBackLabel.setObjectName(u"finishBackLabel")
        self.finishBackLabel.setGeometry(QRect(665, 470, 110, 100))
        self.finishBackLabel.setStyleSheet(u"")
        self.finishBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_finish.png"))
        self.finishBackLabel.setScaledContents(False)
        self.remainingStudyTime = QLabel(self.centralwidget)
        self.remainingStudyTime.setObjectName(u"remainingStudyTime")
        self.remainingStudyTime.setGeometry(QRect(110, 10, 300, 60))
        font = QFont()
        font.setFamily(u"Let's go Digital")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.remainingStudyTime.setFont(font)
        self.remainingStudyTime.setStyleSheet(u"font: 75 italic 48px \"Let's go Digital\";\n"
"color: red;")
        self.remainingStudyTimeShadow = QLabel(self.centralwidget)
        self.remainingStudyTimeShadow.setObjectName(u"remainingStudyTimeShadow")
        self.remainingStudyTimeShadow.setGeometry(QRect(110, 10, 300, 60))
        self.remainingStudyTimeShadow.setFont(font)
        self.remainingStudyTimeShadow.setStyleSheet(u"font: 75 italic 48px \"Let's go Digital\";\n"
"color: rgb(58, 58, 58);")
        self.finishNoButton = QPushButton(self.centralwidget)
        self.finishNoButton.setObjectName(u"finishNoButton")
        self.finishNoButton.setGeometry(QRect(670, 520, 100, 40))
        self.finishNoButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	font: 75 27px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
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
"	font: 75 27px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
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
        self.remainingBreakTime.setFont(font)
        self.remainingBreakTime.setStyleSheet(u"font: 75 italic 48px \"Let's go Digital\";\n"
"color: skyblue;")
        self.remainingBreakTimeShadow = QLabel(self.centralwidget)
        self.remainingBreakTimeShadow.setObjectName(u"remainingBreakTimeShadow")
        self.remainingBreakTimeShadow.setGeometry(QRect(110, 70, 300, 60))
        self.remainingBreakTimeShadow.setFont(font)
        self.remainingBreakTimeShadow.setStyleSheet(u"font: 75 italic 48px \"Let's go Digital\";\n"
"color: rgb(58, 58, 58);")
        self.studyTimerLabel = QLabel(self.centralwidget)
        self.studyTimerLabel.setObjectName(u"studyTimerLabel")
        self.studyTimerLabel.setGeometry(QRect(10, 12, 90, 60))
        self.studyTimerLabel.setStyleSheet(u"font: 75 32px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"color: pink;")
        self.studyTimerLabel.setAlignment(Qt.AlignCenter)
        self.breakTimerLabel = QLabel(self.centralwidget)
        self.breakTimerLabel.setObjectName(u"breakTimerLabel")
        self.breakTimerLabel.setGeometry(QRect(10, 73, 90, 60))
        self.breakTimerLabel.setStyleSheet(u"font: 75 32px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"color: pink;")
        self.breakTimerLabel.setAlignment(Qt.AlignCenter)
        self.breakWidget = QWidget(self.centralwidget)
        self.breakWidget.setObjectName(u"breakWidget")
        self.breakWidget.setGeometry(QRect(210, 470, 400, 100))
        self.breakBackLabel = QLabel(self.breakWidget)
        self.breakBackLabel.setObjectName(u"breakBackLabel")
        self.breakBackLabel.setGeometry(QRect(0, 0, 400, 560))
        self.breakBackLabel.setFocusPolicy(Qt.StrongFocus)
        self.breakBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_break.png"))
        self.breakBackLabel.setScaledContents(True)
        self.breakStartButton = QPushButton(self.breakWidget)
        self.breakStartButton.setObjectName(u"breakStartButton")
        self.breakStartButton.setGeometry(QRect(40, 240, 340, 55))
        self.breakStartButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0, 150, 50, 0.2);\n"
"	border-radius: 13px;\n"
"	font: 75 32px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(0, 150, 50, 0.6);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.breakStartButton.setIconSize(QSize(180, 50))
        self.break_smallUpButton_hour = QPushButton(self.breakWidget)
        self.break_smallUpButton_hour.setObjectName(u"break_smallUpButton_hour")
        self.break_smallUpButton_hour.setGeometry(QRect(105, 106, 42, 24))
        self.break_smallUpButton_hour.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/image/images/icons/largeUpButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.break_smallUpButton_hour.setIcon(icon)
        self.break_smallUpButton_hour.setIconSize(QSize(38, 20))
        self.break_largeUpButton_hour = QPushButton(self.breakWidget)
        self.break_largeUpButton_hour.setObjectName(u"break_largeUpButton_hour")
        self.break_largeUpButton_hour.setGeometry(QRect(113, 82, 26, 24))
        self.break_largeUpButton_hour.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/image/images/icons/smallUpButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.break_largeUpButton_hour.setIcon(icon1)
        self.break_largeUpButton_hour.setIconSize(QSize(22, 20))
        self.break_smallUpButton_minute = QPushButton(self.breakWidget)
        self.break_smallUpButton_minute.setObjectName(u"break_smallUpButton_minute")
        self.break_smallUpButton_minute.setGeometry(QRect(186, 106, 42, 24))
        self.break_smallUpButton_minute.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.break_smallUpButton_minute.setIcon(icon)
        self.break_smallUpButton_minute.setIconSize(QSize(38, 20))
        self.break_largeUpButton_minute = QPushButton(self.breakWidget)
        self.break_largeUpButton_minute.setObjectName(u"break_largeUpButton_minute")
        self.break_largeUpButton_minute.setGeometry(QRect(194, 82, 26, 24))
        self.break_largeUpButton_minute.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.break_largeUpButton_minute.setIcon(icon1)
        self.break_largeUpButton_minute.setIconSize(QSize(22, 20))
        self.break_smallUpButton_second = QPushButton(self.breakWidget)
        self.break_smallUpButton_second.setObjectName(u"break_smallUpButton_second")
        self.break_smallUpButton_second.setGeometry(QRect(267, 106, 42, 24))
        self.break_smallUpButton_second.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.break_smallUpButton_second.setIcon(icon)
        self.break_smallUpButton_second.setIconSize(QSize(38, 20))
        self.break_largeUpButton_second = QPushButton(self.breakWidget)
        self.break_largeUpButton_second.setObjectName(u"break_largeUpButton_second")
        self.break_largeUpButton_second.setGeometry(QRect(275, 82, 26, 24))
        self.break_largeUpButton_second.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.break_largeUpButton_second.setIcon(icon1)
        self.break_largeUpButton_second.setIconSize(QSize(22, 20))
        self.break_smallDownButton_hour = QPushButton(self.breakWidget)
        self.break_smallDownButton_hour.setObjectName(u"break_smallDownButton_hour")
        self.break_smallDownButton_hour.setGeometry(QRect(105, 186, 42, 24))
        self.break_smallDownButton_hour.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/image/images/icons/largeDownButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.break_smallDownButton_hour.setIcon(icon2)
        self.break_smallDownButton_hour.setIconSize(QSize(38, 20))
        self.break_largeDownButton_hour = QPushButton(self.breakWidget)
        self.break_largeDownButton_hour.setObjectName(u"break_largeDownButton_hour")
        self.break_largeDownButton_hour.setGeometry(QRect(113, 209, 26, 24))
        self.break_largeDownButton_hour.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/image/images/icons/smallDownButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.break_largeDownButton_hour.setIcon(icon3)
        self.break_largeDownButton_hour.setIconSize(QSize(22, 20))
        self.break_smallDownButton_minute = QPushButton(self.breakWidget)
        self.break_smallDownButton_minute.setObjectName(u"break_smallDownButton_minute")
        self.break_smallDownButton_minute.setGeometry(QRect(186, 186, 42, 24))
        self.break_smallDownButton_minute.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.break_smallDownButton_minute.setIcon(icon2)
        self.break_smallDownButton_minute.setIconSize(QSize(38, 20))
        self.break_largeDownButton_minute = QPushButton(self.breakWidget)
        self.break_largeDownButton_minute.setObjectName(u"break_largeDownButton_minute")
        self.break_largeDownButton_minute.setGeometry(QRect(194, 209, 26, 24))
        self.break_largeDownButton_minute.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.break_largeDownButton_minute.setIcon(icon3)
        self.break_largeDownButton_minute.setIconSize(QSize(22, 20))
        self.break_smallDownButton_second = QPushButton(self.breakWidget)
        self.break_smallDownButton_second.setObjectName(u"break_smallDownButton_second")
        self.break_smallDownButton_second.setGeometry(QRect(267, 186, 42, 24))
        self.break_smallDownButton_second.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.break_smallDownButton_second.setIcon(icon2)
        self.break_smallDownButton_second.setIconSize(QSize(38, 20))
        self.break_largeDownButton_second = QPushButton(self.breakWidget)
        self.break_largeDownButton_second.setObjectName(u"break_largeDownButton_second")
        self.break_largeDownButton_second.setGeometry(QRect(275, 209, 26, 24))
        self.break_largeDownButton_second.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.break_largeDownButton_second.setIcon(icon3)
        self.break_largeDownButton_second.setIconSize(QSize(22, 20))
        self.breakTimeEditer = QLabel(self.breakWidget)
        self.breakTimeEditer.setObjectName(u"breakTimeEditer")
        self.breakTimeEditer.setGeometry(QRect(55, 126, 300, 60))
        self.breakTimeEditer.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0;\n"
"	font: 75 italic 48px \"Let's go Digital\";\n"
"}")
        self.breakTimeEditer.setAlignment(Qt.AlignCenter)
        self.timerWidget = QWidget(self.centralwidget)
        self.timerWidget.setObjectName(u"timerWidget")
        self.timerWidget.setGeometry(QRect(110, 460, 400, 100))
        self.timerBackLabel = QLabel(self.timerWidget)
        self.timerBackLabel.setObjectName(u"timerBackLabel")
        self.timerBackLabel.setGeometry(QRect(0, 0, 400, 560))
        self.timerBackLabel.setFocusPolicy(Qt.StrongFocus)
        self.timerBackLabel.setPixmap(QPixmap(u":/image/images/windows/loose_leaf_timer.png"))
        self.timerBackLabel.setScaledContents(True)
        self.timerStartButton = QPushButton(self.timerWidget)
        self.timerStartButton.setObjectName(u"timerStartButton")
        self.timerStartButton.setGeometry(QRect(40, 240, 340, 55))
        self.timerStartButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0, 100, 150, 0.2);\n"
"	border-radius: 13px;\n"
"	font: 75 32px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(0, 100, 150, 0.6);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.timerStartButton.setIconSize(QSize(180, 50))
        self.timer_smallUpButton_hour = QPushButton(self.timerWidget)
        self.timer_smallUpButton_hour.setObjectName(u"timer_smallUpButton_hour")
        self.timer_smallUpButton_hour.setGeometry(QRect(105, 106, 42, 24))
        self.timer_smallUpButton_hour.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_smallUpButton_hour.setIcon(icon)
        self.timer_smallUpButton_hour.setIconSize(QSize(38, 20))
        self.timer_largeUpButton_hour = QPushButton(self.timerWidget)
        self.timer_largeUpButton_hour.setObjectName(u"timer_largeUpButton_hour")
        self.timer_largeUpButton_hour.setGeometry(QRect(113, 82, 26, 24))
        self.timer_largeUpButton_hour.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_largeUpButton_hour.setIcon(icon1)
        self.timer_largeUpButton_hour.setIconSize(QSize(22, 20))
        self.timer_smallUpButton_minute = QPushButton(self.timerWidget)
        self.timer_smallUpButton_minute.setObjectName(u"timer_smallUpButton_minute")
        self.timer_smallUpButton_minute.setGeometry(QRect(186, 106, 42, 24))
        self.timer_smallUpButton_minute.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_smallUpButton_minute.setIcon(icon)
        self.timer_smallUpButton_minute.setIconSize(QSize(38, 20))
        self.timer_largeUpButton_minute = QPushButton(self.timerWidget)
        self.timer_largeUpButton_minute.setObjectName(u"timer_largeUpButton_minute")
        self.timer_largeUpButton_minute.setGeometry(QRect(194, 82, 26, 24))
        self.timer_largeUpButton_minute.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_largeUpButton_minute.setIcon(icon1)
        self.timer_largeUpButton_minute.setIconSize(QSize(22, 20))
        self.timer_smallUpButton_second = QPushButton(self.timerWidget)
        self.timer_smallUpButton_second.setObjectName(u"timer_smallUpButton_second")
        self.timer_smallUpButton_second.setGeometry(QRect(267, 106, 42, 24))
        self.timer_smallUpButton_second.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_smallUpButton_second.setIcon(icon)
        self.timer_smallUpButton_second.setIconSize(QSize(38, 20))
        self.timer_largeUpButton_second = QPushButton(self.timerWidget)
        self.timer_largeUpButton_second.setObjectName(u"timer_largeUpButton_second")
        self.timer_largeUpButton_second.setGeometry(QRect(275, 82, 26, 24))
        self.timer_largeUpButton_second.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_largeUpButton_second.setIcon(icon1)
        self.timer_largeUpButton_second.setIconSize(QSize(22, 20))
        self.timer_smallDownButton_hour = QPushButton(self.timerWidget)
        self.timer_smallDownButton_hour.setObjectName(u"timer_smallDownButton_hour")
        self.timer_smallDownButton_hour.setGeometry(QRect(105, 186, 42, 24))
        self.timer_smallDownButton_hour.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_smallDownButton_hour.setIcon(icon2)
        self.timer_smallDownButton_hour.setIconSize(QSize(38, 20))
        self.timer_largeDownButton_hour = QPushButton(self.timerWidget)
        self.timer_largeDownButton_hour.setObjectName(u"timer_largeDownButton_hour")
        self.timer_largeDownButton_hour.setGeometry(QRect(113, 209, 26, 24))
        self.timer_largeDownButton_hour.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_largeDownButton_hour.setIcon(icon3)
        self.timer_largeDownButton_hour.setIconSize(QSize(22, 20))
        self.timer_smallDownButton_minute = QPushButton(self.timerWidget)
        self.timer_smallDownButton_minute.setObjectName(u"timer_smallDownButton_minute")
        self.timer_smallDownButton_minute.setGeometry(QRect(186, 186, 42, 24))
        self.timer_smallDownButton_minute.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_smallDownButton_minute.setIcon(icon2)
        self.timer_smallDownButton_minute.setIconSize(QSize(38, 20))
        self.timer_largeDownButton_minute = QPushButton(self.timerWidget)
        self.timer_largeDownButton_minute.setObjectName(u"timer_largeDownButton_minute")
        self.timer_largeDownButton_minute.setGeometry(QRect(194, 209, 26, 24))
        self.timer_largeDownButton_minute.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_largeDownButton_minute.setIcon(icon3)
        self.timer_largeDownButton_minute.setIconSize(QSize(22, 20))
        self.timer_smallDownButton_second = QPushButton(self.timerWidget)
        self.timer_smallDownButton_second.setObjectName(u"timer_smallDownButton_second")
        self.timer_smallDownButton_second.setGeometry(QRect(267, 186, 42, 24))
        self.timer_smallDownButton_second.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_smallDownButton_second.setIcon(icon2)
        self.timer_smallDownButton_second.setIconSize(QSize(38, 20))
        self.timer_largeDownButton_second = QPushButton(self.timerWidget)
        self.timer_largeDownButton_second.setObjectName(u"timer_largeDownButton_second")
        self.timer_largeDownButton_second.setGeometry(QRect(275, 209, 26, 24))
        self.timer_largeDownButton_second.setStyleSheet(u"font: 24px \"MS UI Gothic\";\n"
"background-color: transparent;")
        self.timer_largeDownButton_second.setIcon(icon3)
        self.timer_largeDownButton_second.setIconSize(QSize(22, 20))
        self.timerTimeEditer = QLabel(self.timerWidget)
        self.timerTimeEditer.setObjectName(u"timerTimeEditer")
        self.timerTimeEditer.setGeometry(QRect(55, 126, 300, 60))
        self.timerTimeEditer.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0;\n"
"	font: 75 italic 48px \"Let's go Digital\";\n"
"}")
        self.timerTimeEditer.setAlignment(Qt.AlignCenter)
        self.smaphoButton = QPushButton(self.centralwidget)
        self.smaphoButton.setObjectName(u"smaphoButton")
        self.smaphoButton.setGeometry(QRect(742, 3, 55, 55))
        self.smaphoButton.setStyleSheet(u"background-color: transparent;")
        icon4 = QIcon()
        icon4.addFile(u":/image/images/icons/pink_smapho.png", QSize(), QIcon.Normal, QIcon.Off)
        self.smaphoButton.setIcon(icon4)
        self.smaphoButton.setIconSize(QSize(51, 51))
        self.chromeButton = QPushButton(self.centralwidget)
        self.chromeButton.setObjectName(u"chromeButton")
        self.chromeButton.setGeometry(QRect(742, 61, 55, 55))
        self.chromeButton.setStyleSheet(u"background-color: transparent;")
        icon5 = QIcon()
        icon5.addFile(u":/image/images/icons/blue_chrome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chromeButton.setIcon(icon5)
        self.chromeButton.setIconSize(QSize(51, 51))
        self.smallButton = QPushButton(self.centralwidget)
        self.smallButton.setObjectName(u"smallButton")
        self.smallButton.setGeometry(QRect(744, 120, 51, 51))
        self.smallButton.setStyleSheet(u"QPushButton{\n"
"	background: red;\n"
"}")
        RoomScreen.setCentralWidget(self.centralwidget)
        self.insideRoomLabel.raise_()
        self.blackFrame.raise_()
        self.osanaLabel.raise_()
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
        self.breakButton.raise_()
        self.finishButton.raise_()
        self.logButton.raise_()
        self.timerButton.raise_()
        self.remainingBreakTimeShadow.raise_()
        self.remainingBreakTime.raise_()
        self.studyTimerLabel.raise_()
        self.breakTimerLabel.raise_()
        self.breakWidget.raise_()
        self.timerWidget.raise_()
        self.windowLabel.raise_()
        self.osanaText.raise_()
        self.smaphoButton.raise_()
        self.chromeButton.raise_()
        self.smallButton.raise_()

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
"</style></head><body style=\" font-family:'UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B'; font-size:24px; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u30e1\u30a4\u30ea\u30aa'; font-size:16pt;\">\u3077\u3063\u3001\u306a\u306b\u305d\u308c\u3002\u305d\u3082\u305d\u3082\u4ed8\u304d\u5408\u3046\u6c17\u306a\u304b\u3063\u305f\u3088\u3002\u3042\u3063\u3001\u5b89\u5fc3\u3057\u3066\u308b\uff1f\u3075\u3075\u3001\u305c\u30fc\u3093\u3076\u304a\u898b\u901a\u3057\u3063\u3066\u308f\u3051\uff57</span></p></body></html>", None))
        self.osanaLabel.setText("")
        self.finishButton.setText("")
        self.windowLabel.setText("")
        self.blackFrameButton.setText("")
        self.logButton.setText("")
        self.breakButton.setText("")
        self.timerButton.setText("")
        self.logBackLabel.setText("")
        self.finishLabel.setText("")
        self.logLabel.setText("")
        self.breakLabel.setText("")
        self.timerLabel.setText("")
        self.finishBackLabel.setText("")
        self.remainingStudyTime.setText(QCoreApplication.translate("RoomScreen", u"0 1:00: 12", None))
        self.remainingStudyTimeShadow.setText(QCoreApplication.translate("RoomScreen", u"88:88:88", None))
        self.finishNoButton.setText(QCoreApplication.translate("RoomScreen", u"\u3044\u3044\u3048", None))
        self.finishYesButton.setText(QCoreApplication.translate("RoomScreen", u"\u306f\u3044", None))
        self.remainingBreakTime.setText(QCoreApplication.translate("RoomScreen", u"0 1:00: 12", None))
        self.remainingBreakTimeShadow.setText(QCoreApplication.translate("RoomScreen", u"88:88:88", None))
        self.studyTimerLabel.setText(QCoreApplication.translate("RoomScreen", u"\u52c9\u5f37", None))
        self.breakTimerLabel.setText(QCoreApplication.translate("RoomScreen", u"\u4f11\u61a9", None))
        self.breakBackLabel.setText("")
        self.breakStartButton.setText(QCoreApplication.translate("RoomScreen", u"\u4f11\u61a9\u306f\u3058\u3081\uff01\uff01", None))
        self.break_smallUpButton_hour.setText("")
        self.break_largeUpButton_hour.setText("")
        self.break_smallUpButton_minute.setText("")
        self.break_largeUpButton_minute.setText("")
        self.break_smallUpButton_second.setText("")
        self.break_largeUpButton_second.setText("")
        self.break_smallDownButton_hour.setText("")
        self.break_largeDownButton_hour.setText("")
        self.break_smallDownButton_minute.setText("")
        self.break_largeDownButton_minute.setText("")
        self.break_smallDownButton_second.setText("")
        self.break_largeDownButton_second.setText("")
        self.breakTimeEditer.setText(QCoreApplication.translate("RoomScreen", u"00 : 00 : 00", None))
        self.timerBackLabel.setText("")
        self.timerStartButton.setText(QCoreApplication.translate("RoomScreen", u"\u30bf\u30a4\u30de\u30fc\u30b9\u30bf\u30fc\u30c8\uff01\uff01", None))
        self.timer_smallUpButton_hour.setText("")
        self.timer_largeUpButton_hour.setText("")
        self.timer_smallUpButton_minute.setText("")
        self.timer_largeUpButton_minute.setText("")
        self.timer_smallUpButton_second.setText("")
        self.timer_largeUpButton_second.setText("")
        self.timer_smallDownButton_hour.setText("")
        self.timer_largeDownButton_hour.setText("")
        self.timer_smallDownButton_minute.setText("")
        self.timer_largeDownButton_minute.setText("")
        self.timer_smallDownButton_second.setText("")
        self.timer_largeDownButton_second.setText("")
        self.timerTimeEditer.setText(QCoreApplication.translate("RoomScreen", u"00 : 00 : 00", None))
        self.smaphoButton.setText("")
        self.chromeButton.setText("")
        self.smallButton.setText(QCoreApplication.translate("RoomScreen", u"\u5c0f", None))
    # retranslateUi

