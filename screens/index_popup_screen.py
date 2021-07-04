#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QMovie


## ==> MAIN WINDOW

## ==> INDEX POPUP SCREEN
from ui_index_popup_screen import Ui_indexPopupScreen


# YOUR APPLICATION
class IndexPopupScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_indexPopupScreen()
        self.ui.setupUi(self)

        # gif setting
        loading_gif_path = u":/image/images/backgrounds/loading.gif"
        movie = QMovie()
        movie.setFileName(loading_gif_path)
        self.ui.loadingLabel.setMovie(movie)

        movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IndexPopupScreen()
    window.show()
    sys.exit(app.exec_())
