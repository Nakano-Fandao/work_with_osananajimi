#! /usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtMultimedia import QSound
from json_files import JsonFiles

class PlayBgm():
    #* BGM start
    def __init__(self, bgm):
        self.json = JsonFiles()
        print("**BGM voice loaded**")
        self.bgm = QSound(self.json.correspondence[bgm])
        self.bgm.setLoops(100)
        self.bgm.play()
        print('BGM "'+bgm+'" starts')

    #* BGM stop
    def stop(self):
        self.bgm.stop()
