#! /usr/bin/python
# -*- coding: utf-8 -*-

import json, os, random
from PySide2.QtMultimedia import QSound

class PlayVoice:
    def __init__(self):
        # Load json file
        json_path = os.path.join(os.path.dirname(__file__),'../UI/json')
        with open(json_path+"/voice.json") as f:
            self.voice_json = json.load(f)
        with open(json_path+"/correspondence.json") as f:
            self.correspondence_json = json.load(f)

        self.voice_json = self.voice_json["voice"]

    def play_voice(self, case, mood):
        """
        smapho, youtube, hentai, common
        """
        common_voices = list(self.voice_json["common"][mood].values())
        voices = list(self.voice_json[case][mood].values())
        voice = random.choice(voices + common_voices)
        voice_path = self.correspondence_json[voice]
        QSound.play(voice_path)
        return voice

    def play_annoucement(self, when):
        annoucement = self.voice_json["annoucement"][when]
        voice_path = self.correspondence_json[annoucement]
        QSound.play(voice_path)
        return annoucement

    def play_app_voice(self, when, mood, added=False):
        if (when == "start") & (mood == "great"):
            mood = "good"

        voices = list(self.voice_json["app"][when][mood].values())
        if added:
            voices += list(self.voice_json["extra"].values())

        voice = random.choice(voices)
        voice_path = self.correspondence_json[voice]
        QSound.play(voice_path)
        return voice
