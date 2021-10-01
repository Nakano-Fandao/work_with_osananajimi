#! /usr/bin/python
# -*- coding: utf-8 -*-

import random
from PySide2.QtMultimedia import QSound
from json_files import JsonFiles


class PlayVoice():
    def __init__(self):
        self.json = JsonFiles()
        print("**Osananajimi voice loaded**")
        self.voice = QSound("")

    #* サボりを検知したとき
    def play_voice(self, case, mood):
        """
        smapho, youtube, hentai, common
        """

        if mood == "great":
            if case == "hentai":
                voices = list(self.json.voice[case]["good"].values())
            else:
                voices = list(self.json.voice[case][mood].values())
        elif mood == "bad":
            if case == "youtube":
                voices = []
            else:
                voices = list(self.json.voice[case][mood].values())
            common_voices = list(self.json.voice["common"][mood].values())
        else:
            voices = list(self.json.voice[case][mood].values())
            common_voices = list(self.json.voice["common"][mood].values())

        voice = random.choice(voices + common_voices)
        self.find_and_play(voice)
        return voice

    #* 時報
    def play_announcement(self, when):
        """
        announcements
        """
        announcement = self.json.voice["announcement"][when]
        self.find_and_play(announcement)
        return announcement

    #* 作業を始めたとき、アプリ終了時
    def play_app_voice(self, when, mood, touched=False):
        """
        app
        """

        if (when == "start") & (mood == "great"): mood = "good";

        app_voices = list(self.json.voice["app"][when][mood].values())

        #* タイトル画面で幼馴染をタッチしたとき
        if touched:
            app_voices += list(self.json.voice["extra"].values())
        #* ----------------------------------

        app_voice = random.choice(app_voices)
        self.find_and_play(app_voice)
        return app_voice

    #* 勉強タイマー関係
    def play_study_timer_voice(self, when, mood, timing=None):
        """
        study_timer
        """
        if mood == "great": mood = "good";
        if when == "start":
            pass
        else:
            if mood == "bad": mood = "awkward";
            if when == "finish":
                pass
            else:
                if timing in set(["10", "30"]):
                    if mood == "good": mood = "normal";
                else:
                    if mood == "awkward": mood = "normal";

        if when == "mid":
            study_timer_voices = list(self.json.voice["timer"][when][timing][mood].values())
        else:
            study_timer_voices = list(self.json.voice["timer"][when][mood].values())

        study_timer_voice = random.choice(study_timer_voices)
        if str(type(study_timer_voice)) == "<class 'dict'>":
            study_timer_voice = study_timer_voice["ask"]
        self.find_and_play(study_timer_voice)
        return study_timer_voice

    #* 休憩タイマー関係
    def play_break_timer_voice(self, when, mood):
        """
        break_timer
        """
        if mood == "great": mood = "good";
        if (when == "finish") & (mood == "bad"):
            mood = "awkward"

        break_timer_voices = list(self.json.voice["break"][when][mood].values())
        break_timer_voice = random.choice(break_timer_voices)
        self.find_and_play(break_timer_voice)
        return break_timer_voice

    #* 世間話
    def play_chat_voice(self, mood):
        """
        chats
        """
        if mood in set(["bad", "awkward"]): mood = "normal";

        chats = list(self.json.voice["chat"][mood].values())
        chat = random.choice(chats)
        self.find_and_play(chat)
        return chat

    #* 選択肢のある世間話
    def play_choicechat_ask(self, mood):
        """
        choicechats
        """
        if mood == "bad": mood = "awkward";
        choicechats = list(self.json.voice["choicechat"][mood].values())
        choicechat = random.choice(choicechats)["ask"]
        choicechat_detail = self.json.choicechat[choicechat]
        self.find_and_play(choicechat)
        return choicechat, choicechat_detail

    #* 世間話の返答
    def play_chat_reply(self, reply):
        """
        chats, choicechats
        """
        self.find_and_play(reply)


    #* 声を再生する関数
    def find_and_play(self, serif):
        self.voice.stop()
        voice_path = self.json.correspondence[serif]
        self.voice = QSound(voice_path)
        self.voice.play()
        print(serif)
