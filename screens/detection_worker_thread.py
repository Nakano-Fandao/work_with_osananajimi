#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from website_detection import WebsiteDetection

class DetectionWorker(QThread):
    smapho_detected = Signal()
    website_detected = Signal(str)

    def __init__(self, smapho_detection, url_list):
        print("Detection Worker Thread starts")
        QThread.__init__(self)
        self.smapho_detection = smapho_detection
        self.website_detection = WebsiteDetection()
        self.url_list = url_list

        self.mutex = QMutex()
        self.stopped = False
        self.smapho_flag = True
        self.chrome_flag = True

    def __del__(self):
        #* Threadオブジェクトが削除されたときにThreadを停止する(念のため)
        self.end()

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stopped = True

    def end(self):
        self.stop()
        self.terminate()

    def restart(self, url_list):
        print("Detection Worker Thread restarts")
        self.set_websites(url_list)
        with QMutexLocker(self.mutex):
            self.stopped = False
        self.start()

    def set_websites(self, url_list):
        self.url_list = url_list

    def run(self):
        """Long-running task."""
        count = 0
        smapho_counter = 0
        while not self.stopped:
            if self.smapho_flag:
                #* 3秒ごとにスマホ検知
                if self.smapho_detection.judge_smapho():
                    smapho_counter += 1
                    print("スマホ触ってる？ {}/5回目".format(smapho_counter))
                else:
                    smapho_counter = 0
                    print("スマホ触ってなくてえらい！")

            if self.chrome_flag:
                #* 30秒ごとにウェブサイト検知（1回で即アウト）
                if count%10 == 0:
                    detected_website = self.website_detection.detect(self.url_list)
                    if detected_website != "safe":
                        self.website_detected.emit(detected_website)

            #* 5回連続スマホ検知したら、アウト
            if smapho_counter >= 5:
                smapho_counter = 0
                self.smapho_detected.emit()

            count += 1
            time.sleep(3)
