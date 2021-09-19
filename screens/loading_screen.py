#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, random
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "../settings")))
from path_setting import PathSetting
PathSetting().__init__()

from smapho_detection import SmaphoDetection
from json_files import JsonFiles

## ==> MAIN WINDOW
from room_screen import RoomScreen
## ==> LOADING SCREEN
from ui_loading_screen import Ui_LoadingScreen

# LOADING SCREEN
class LoadingScreen(QMainWindow):
    def __init__(self, mood_parameter, bgm):
        QMainWindow.__init__(self)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)
        print("Loading screen")

        self.mood_parameter = mood_parameter
        self.bgm = bgm
        self.runLongTask_camera_and_model()

        self.tips_json = JsonFiles().tips
        self.tips = random.choice(list(self.tips_json))
        self.ui.tipsBrowser.setText(self.tips)

        #* REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)

        loading_gif = QMovie(u":/image/images/sentences/loading.gif")
        self.ui.loadingLabel.setMovie(loading_gif)
        loading_gif.start()

    def runLongTask_camera_and_model(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.thread.finished.connect(self.show_room_screen)

    def show_room_screen(self):
        print("Worker thread ended")
        self.bgm.stop()
        self.room_screen = RoomScreen(self.mood_parameter, self.worker.smapho_detection)
        self.room_screen.show()
        self.close()

class Worker(QObject):
    camera = Signal(SmaphoDetection)
    finished = Signal()

    def run(self):
        """Long-running task."""
        #* カメラオープン！
        self.smapho_detection = SmaphoDetection()
        self.camera.emit(self.smapho_detection)
        self.finished.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingScreen(50, "bgm")
    window.show()
    sys.exit(app.exec_())
