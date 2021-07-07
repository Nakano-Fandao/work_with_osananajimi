#!python3
# -*- coding: utf-8 -*-

import sys, os, json

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import *
from PySide2.QtGui import *

add_list = ["../detect_modules", "../UI", "../screens"]
for dir in add_list:
    sys.path.append(os.path.join(os.path.dirname(__file__), dir))

from ui_log_popup import Ui_LogPopup

from play_voice import PlayVoice


class LogPopup(QDialog):
    def __init__(self, model_list):
        QDialog.__init__(self)
        self.ui = Ui_LogPopup()
        self.ui.setupUi(self)

        self.osana = PlayVoice()

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Model作成
        self.model = QtCore.QStringListModel()
        self.model.setStringList(model_list)
        self.ui.logList.setModel(self.model)

        # Signal-Slot作成
        self.ui.logList.clicked.connect(self.list_clicked)
        self.ui.exitButton.clicked.connect(lambda x: self.close())


    def list_clicked(self, index):
        # 選択した声を再生する
        self.osana.find_and_play(index.data())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    model_list = [
        'え～終わっちゃうの～？そっかぁ、早く戻ってきてよね！',
        '休憩終わったよー！気持ち入れ替えてがんばろう！',
        'ちょちょっと、まだ別に返事したわけじゃないし、なんなら断るつもりだったし。でも、そんなに焦ってくれるなんてね～ｗちょっと嬉しいかもｗ',
        "ぷっ、なにそれ。そもそも付き合う気なかったよ。あっ、安心してる？ふふ、ぜーんぶお見通しってわけｗ",
        "そっか。そういえば最近、天気よくないよね。明日は晴れるといいな。ふふ、冗談だよ。仲良くなかったら一緒に作業なんてしないよねw"
    ]
    window = LogPopup(model_list)
    window.show()
    sys.exit(app.exec_())
