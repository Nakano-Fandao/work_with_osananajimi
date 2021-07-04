# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index_popup_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_indexPopupScreen(object):
    def setupUi(self, indexPopupScreen):
        if not indexPopupScreen.objectName():
            indexPopupScreen.setObjectName(u"indexPopupScreen")
        indexPopupScreen.resize(600, 450)
        self.loadingLabel = QLabel(indexPopupScreen)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setGeometry(QRect(0, 0, 600, 450))
        self.loadingLabel.setScaledContents(True)

        self.retranslateUi(indexPopupScreen)

        QMetaObject.connectSlotsByName(indexPopupScreen)
    # setupUi

    def retranslateUi(self, indexPopupScreen):
        indexPopupScreen.setWindowTitle(QCoreApplication.translate("indexPopupScreen", u"Form", None))
        self.loadingLabel.setText("")
    # retranslateUi

