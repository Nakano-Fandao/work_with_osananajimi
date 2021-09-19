# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'website_selection_popup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_WebsiteSelectionPopup(object):
    def setupUi(self, WebsiteSelectionPopup):
        if not WebsiteSelectionPopup.objectName():
            WebsiteSelectionPopup.setObjectName(u"WebsiteSelectionPopup")
        WebsiteSelectionPopup.resize(300, 450)
        WebsiteSelectionPopup.setStyleSheet(u"")
        self.mainFrame = QFrame(WebsiteSelectionPopup)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 300, 450))
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setStyleSheet(u"")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.backgroundLabel = QLabel(self.mainFrame)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(0, 0, 300, 450))
        self.backgroundLabel.setPixmap(QPixmap(u":/image/images/backgrounds/sky.png"))
        self.backgroundLabel.setScaledContents(True)
        self.osanaLabel = QLabel(self.mainFrame)
        self.osanaLabel.setObjectName(u"osanaLabel")
        self.osanaLabel.setGeometry(QRect(150, 290, 150, 225))
        self.osanaLabel.setPixmap(QPixmap(u":/image/images/character/key_visual.png"))
        self.osanaLabel.setScaledContents(True)
        self.urlView = QListView(self.mainFrame)
        self.urlView.setObjectName(u"urlView")
        self.urlView.setGeometry(QRect(10, 60, 280, 220))
        self.urlView.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.urlView.setStyleSheet(u"QListView {\n"
"	background: transparent;\n"
"	font-size: 20px;\n"
"	line-height: 25px;\n"
"	border: 0;\n"
"	outline: none;\n"
"}\n"
"QListView::item{\n"
"	padding: 5px;\n"
"	border: .3px solid white;\n"
"	border-radius: 5px;\n"
"	margin-bottom: 5px;\n"
"	background-color: rgba(255, 225, 148, 0.2);\n"
"}\n"
"QListView::item:hover{\n"
"	background-color: rgba(255, 225, 148, 0.4);\n"
"}\n"
"QListView::item:selected{\n"
"	background-color: rgba(255, 225, 148, 0.6);\n"
"}")
        self.urlView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.urlView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.urlView.setDefaultDropAction(Qt.IgnoreAction)
        self.urlView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.urlView.setViewMode(QListView.ListMode)
        self.urlView.setItemAlignment(Qt.AlignCenter)
        self.fukidashiLabel = QLabel(self.mainFrame)
        self.fukidashiLabel.setObjectName(u"fukidashiLabel")
        self.fukidashiLabel.setGeometry(QRect(0, 300, 200, 111))
        self.fukidashiLabel.setPixmap(QPixmap(u":/image/images/sentences/fukidashi.png"))
        self.fukidashiLabel.setScaledContents(True)
        self.fukidashiText = QTextBrowser(self.mainFrame)
        self.fukidashiText.setObjectName(u"fukidashiText")
        self.fukidashiText.setGeometry(QRect(11, 336, 171, 40))
        self.fukidashiText.setStyleSheet(u"QTextBrowser {\n"
"	background-color: transparent;\n"
"	font: 75 14px \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"	border: 0;\n"
"}")
        self.fukidashiText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.fukidashiText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.urlAdditionEdit = QTextEdit(self.mainFrame)
        self.urlAdditionEdit.setObjectName(u"urlAdditionEdit")
        self.urlAdditionEdit.setGeometry(QRect(5, 10, 255, 30))
        self.urlAdditionEdit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.urlAdditionEdit.setStyleSheet(u"QTextEdit {\n"
"	font: 75 8pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 NK-B\";\n"
"	border-radius: 5px;\n"
"}\n"
"QTextEdit:focused {\n"
"	border: yellow;\n"
"}")
        self.urlAdditionEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.urlAdditionEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.urlAdditionEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.urlAdditionEdit.setPlaceholderText(u"https://www.youtube.com/")
        self.addButton = QPushButton(self.mainFrame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(265, 10, 30, 30))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.addButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/image/images/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(30, 30))
        self.exitButton = QPushButton(self.mainFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(-6, 415, 90, 30))
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.exitButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/image/images/icons/return.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon1)
        self.exitButton.setIconSize(QSize(90, 30))

        self.retranslateUi(WebsiteSelectionPopup)

        QMetaObject.connectSlotsByName(WebsiteSelectionPopup)
    # setupUi

    def retranslateUi(self, WebsiteSelectionPopup):
        WebsiteSelectionPopup.setWindowTitle(QCoreApplication.translate("WebsiteSelectionPopup", u"\u30a6\u30a7\u30d6\u30b5\u30a4\u30c8\u9078\u629e\u753b\u9762", None))
        self.backgroundLabel.setText("")
        self.osanaLabel.setText("")
        self.fukidashiLabel.setText("")
        self.fukidashiText.setHtml(QCoreApplication.translate("WebsiteSelectionPopup", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B'; font-size:14px; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u691c\u77e5\u3057\u305f\u3044\u30a6\u30a7\u30d6\u30b5\u30a4\u30c8\u3092\u9078\u3093\u3067\u306d\uff01</span></p></body></html>", None))
        self.addButton.setText("")
        self.exitButton.setText("")
    # retranslateUi

