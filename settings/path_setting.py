import os, sys

class PathSetting:
    def __init__(self):

        add_list = ["../detect_modules", "../UI", "../screens"]

        for dir in add_list:
            sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), dir)))
