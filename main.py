#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from settings.path_setting import PathSetting
from PySide2.QtWidgets import QApplication


if __name__ == "__main__":
    """
    通常よみこみ             ：LOAD = 0
    マチカネバグキタルロード  ：LOAD = 1
    """
    LOAD = 0

    PathSetting().__init__()
    app = QApplication(sys.argv)

    if LOAD:
        from special_splash_screen import SplashScreen
    else:
        from splash_screen import SplashScreen

    window = SplashScreen()
    sys.exit(app.exec_())
