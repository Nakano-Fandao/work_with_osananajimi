#!python3
# -*- coding: utf-8 -*-

import sys, os, json

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound

from ui_log_screen import Ui_LogScreen
import files_rc

# Load json file
json_path = os.path.join(os.path.dirname(__file__),'../UI/json')
with open(json_path+"/voice.json") as f:
    voice_json = json.load(f)
with open(json_path+"/correspondence.json") as f:
    correspondence_json = json.load(f)

class LogScreen(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_LogScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Model作成
        self.model = QtCore.QStringListModel()
        self.model.setStringList(['aaa', 'bbb', 'ccc'])
        self.ui.logList.setModel(self.model)

        # Signal-Slot作成
        self.ui.logList.clicked.connect(self.list_clicked)
        self.ui.exitButton.clicked.connect(self.button_clicked)


    def list_clicked(self, index):
        # 現在選択している文字列を取得する
        if index.data() == "あ～またスマホ触ってるなぁ？じゃあ、3.2.1でスマホ置いてね！さん、に、いち、、ぜろ、ふふ❤スマホ置いてくれたかな？笑":
            print(index.data())

        self.addList()
        self.play_voice()

    def addList(self):
        txt = "あ～またスマホ触ってるなぁ？じゃあ、3.2.1でスマホ置いてね！さん、に、いち、、ぜろ、ふふ❤スマホ置いてくれたかな？笑"
        strList = self.model.stringList()
        strList.append(txt)
        self.model.setStringList(strList)

    def play_voice(self):
        QSound.play(correspondence_json["door_knocking"])


    def button_clicked(self):
        sys.exit(-1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogScreen()
    window.show()
    sys.exit(app.exec_())
