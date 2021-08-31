#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys, os

from PySide2.QtCore import Qt, QTimer, QCoreApplication, QSize
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QPixmap

add_list = ["../detect_modules", "../UI", "../settings", "../screens"]
for dir in add_list:
    sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), dir)))

## ==> roomscreen


## ==> miniROOM SCREEN
from ui_miniroom_screen import Ui_miniRoomScreen

#miniRoomScree
class miniRoomScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #*------ UI setting -------
        self.ui = Ui_miniRoomScreen()
        self.ui.setupUi(self)
        #*-------------------------
        
        #slot,signal 
        self.ui.bigButton.clicked.connect(self.show_room)
    
    def show_room(self):
        from room_screen import RoomScreen
        self.RoomScreen = RoomScreen()
        self.RoomScreen.show()
        self.hide()

    def mousePressEvent(self, event):
        self.__isDrag = True
        self.__startPos = event.pos()
        
    def mouseReleaseEvent(self, event):
        self.__isDrag = False
       
    def mouseMoveEvent(self, event):
        if self.__isDrag:
            self.move(self.mapToParent(event.pos() - self.__startPos))
       
#実行処理
if __name__=="__main__":
    #アプリケーション作成
    app = QApplication(sys.argv)
    #オブジェクト作成
    window = miniRoomScreen()
    #TestWindow1の表示
    window.show()
    sys.exit(app.exec_())



