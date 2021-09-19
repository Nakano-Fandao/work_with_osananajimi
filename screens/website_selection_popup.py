#!python3
# -*- coding: utf-8 -*-

import sys, os, json

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

add_list = ["../detect_modules", "../UI", "../screens"]
for dir in add_list:
    sys.path.append(os.path.join(os.path.dirname(__file__), dir))

from ui_website_selection_popup import Ui_WebsiteSelectionPopup

class WebsiteSelectionPopup(QDialog):
    def __init__(self, model_list):
        QDialog.__init__(self)

        #*------ UI setting -------
        self.ui = Ui_WebsiteSelectionPopup()
        self.ui.setupUi(self)

        self.addIcon = QIcon()
        self.addIcon.addFile(u":/image/images/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addHoverIcon = QIcon()
        self.addHoverIcon.addFile(u":/image/images/icons/add_hover.png", QSize(), QIcon.Normal, QIcon.Off)

        self.open_cur = QCursor()
        self.open_cur.setShape(Qt.OpenHandCursor)
        self.closed_cur = QCursor()
        self.closed_cur.setShape(Qt.ClosedHandCursor)
        self.pointer_cur = QCursor()
        self.pointer_cur.setShape(Qt.PointingHandCursor)
        self.ui.mainFrame.setCursor(self.open_cur)

        #* REMOVE TITLE BAR
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.fukidashiText.setText("検知したいウェブサイトを追加・選択してね！")
        #*-------------------------

        #* Model作成
        self.model = QStringListModel()
        self.model.setStringList(model_list)
        self.ui.urlView.setModel(self.model)

        #* Signal-Slot作成
        self.ui.addButton.clicked.connect(self.add_website)
        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.exitButton.clicked.connect(self.accept)

    def add_website(self):
        self.ui.addButton.setIcon(self.addHoverIcon)
        new_url = self.ui.urlAdditionEdit.toPlainText()
        if new_url != "":
            url_list = self.model.stringList()
            url_list.append(new_url)
            self.model.setStringList(url_list)
            self.ui.urlAdditionEdit.clear()
        QTimer.singleShot(100, lambda: self.ui.addButton.setIcon(self.addIcon))

    @property
    def selected_items(self):
        self.close()
        items = list(map(lambda x: x.data(), self.ui.urlView.selectedIndexes()))
        return items

    def exit(self):
        self.ui.exitButton.setIconSize(QSize(95, 33))
        QTimer.singleShot(80, lambda: self.ui.exitButton.setIconSize(QSize(90, 30)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    url_list = [
        'https://www.youtube.com/',
        'https://www.nicovideo.jp/',
        'https://video.unext.jp/'
    ]
    window = WebsiteSelectionPopup(url_list)
    window.show()
    sys.exit(app.exec_())
