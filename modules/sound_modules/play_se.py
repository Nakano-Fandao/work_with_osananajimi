#! /usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtMultimedia import QSound
from json_files import JsonFiles

class PlaySe():
    #* SE start
    def __init__(self):
        self.json = JsonFiles()
        print("**SE loaded**")
        self.se = QSound("")

    #* se stop
    def play(self, se):
      self.se.stop()
      self.se = QSound(self.json.correspondence[se])
      self.se.play()
      print('se: "'+se+'"')
