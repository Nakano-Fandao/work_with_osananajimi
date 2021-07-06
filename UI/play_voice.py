#! /usr/bin/python
# -*- coding: utf-8 -*-

import random
from PySide2.QtMultimedia import QSound
from json_files import JsonFiles

from settings.mood_parameter import MoodParameter

class PlayVoice():
    def __init__(self):
        self.json = JsonFiles()
        print("Loading 幼馴染の声 completed")

    # サボりを検知したとき
    def play_voice(self, case, parameter):
        """
        smapho, youtube, hentai, common
        """
        mood = MoodParameter(parameter).mood

        common_voices = list(self.json.voice["common"][mood].values())
        voices = list(self.json.voice[case][mood].values())
        voice = random.choice(voices + common_voices)
        self.find_and_play(voice)
        return voice

    # 時報
    def play_annoucement(self, when):
        """
        annoucements
        """
        annoucement = self.json.voice["annoucement"][when]
        self.find_and_play(annoucement)
        return annoucement

    # 作業を始めたとき
    def play_app_voice(self, when, parameter, touched=False):
        """
        app
        """
        mood = MoodParameter(parameter).mood

        if (when == "start") & (mood == "great"):
            mood = "good"

        app_voices = list(self.json.voice["app"][when][mood].values())

        #* タイトル画面で幼馴染をタッチしたとき
        if touched:
            app_voices += list(self.json.voice["extra"].values())
        #* ----------------------------------

        app_voice = random.choice(app_voices)
        self.find_and_play(app_voice)
        return app_voice

    # 選択肢のある世間話
    def play_choicechat_ask(self, parameter):
        """
        choicechats
        """
        mood = MoodParameter(parameter).mood

        choicechats = list(self.json.voice["choicechat"][mood].values())
        choicechat = random.choice(choicechats)["ask"]
        choicechat_detail = self.json.choicechat[choicechat]
        self.find_and_play(choicechat)
        return choicechat, choicechat_detail

        # 選択肢のある世間話
    def play_choicechat_reply(self, reply):
        """
        choicechats
        """
        self.find_and_play(reply)


    # 声を再生する関数
    def find_and_play(self, voice):
        voice_path = self.json.correspondence[voice]
        QSound.play(voice_path)
        print(voice)
