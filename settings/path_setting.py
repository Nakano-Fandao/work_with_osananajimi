import os, sys

class PathSetting:
    def __init__(self):

        add_list = ["../modules", "../modules/detect_modules", "../modules/sound_modules", "../UI", "../settings", "../screens"]

        for dir in add_list:
            sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), dir)))
