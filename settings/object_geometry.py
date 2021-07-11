class Geometry:
    def __init__(self, func, move_flag, trans_flag):

        #* ----------------------------before-----------------after---------
        self.blackFrame       = [[  0,   0,   0,   0], [  0,   0,   0, 0.4]]
        self.osanaLabel       = [[220,  40, 370, 470], [220,   0, 370, 470]]
        self.windowLabel      = [[ 20, 405, 760, 182], [ 20, 525, 760, 182]]
        self.osanaText        = [[ 30, 470, 740, 105], [ 30, 590, 740, 105]]

        self.logView          = [[370, 470, 400, 100], [370,  90, 400, 560]]

        self.timerSentence    = [[130, 510, 180,  50], [130, 380, 180,  50]]
        self.timerTimeEdit    = [[300, 510, 180,  50], [300, 380, 180,  50]]
        self.timerStartButton = [[215, 510, 180,  42], [215, 470, 180,  42]]

        self.breakSentence    = [[230, 510, 180,  50], [230, 380, 180,  50]]
        self.breakTimeEdit    = [[400, 510, 180,  50], [400, 380, 180,  50]]
        self.breakStartButton = [[315, 510, 180,  50], [315, 470, 180,  50]]

        self.timerBackLabel   = [[110, 470, 400, 100], [110, 290, 400, 560]]
        self.breakBackLabel   = [[210, 470, 400, 100], [210, 290, 400, 560]]
        self.logBackLabel     = [[370, 470, 400, 100], [370,  90, 400, 560]]
        self.finishBackLabel  = [[380, 470, 400, 100], [380, 290, 400, 560]]

        self.timerLabel       = [[370, 410, 108,  79], [370, 250, 108,  79]]
        self.breakLabel       = [[470, 410, 108,  79], [470, 250, 108,  79]]
        self.logLabel         = [[570, 410, 108,  79], [570,  50, 108,  79]]
        self.finishLabel      = [[670, 410, 108,  79], [670, 250, 108,  79]]

        self.timerButton      = [[377, 414, 101,  40], [377, 260, 101,  60]]
        self.breakButton      = [[477, 414, 101,  40], [477, 260, 101,  60]]
        self.logButton        = [[577, 414, 101,  40], [577,  60, 101,  60]]
        self.finishButton     = [[677, 414, 101,  40], [677, 260, 101,  60]]
        #* -----------------------------------------------------------------

        if func == "Timer":
            self.breakLabel[1][1]   = 534
            self.logLabel[1][1]     = 534
            self.finishLabel[1][1]  = 534
            self.breakButton[1][1]  = 544
            self.logButton[1][1]    = 544
            self.finishButton[1][1] = 544

        elif func == "Break":
            self.timerLabel[1][1]   = 534
            self.logLabel[1][1]     = 534
            self.finishLabel[1][1]  = 534
            self.timerButton[1][1]  = 544
            self.logButton[1][1]    = 544
            self.finishButton[1][1] = 544

        elif func == "Log":
            self.osanaLabel[1]      = [20, 130, 370, 470]
            self.timerLabel[1][1]   = 534
            self.breakLabel[1][1]   = 534
            self.finishLabel[1][1]  = 534
            self.timerButton[1][1]  = 544
            self.breakButton[1][1]  = 544
            self.finishButton[1][1] = 544

        elif func == "Finish":
            self.timerLabel[1][1]   = 534
            self.breakLabel[1][1]   = 534
            self.logLabel[1][1]     = 534
            self.timerButton[1][1]  = 544
            self.breakButton[1][1]  = 544
            self.logButton[1][1]    = 544


        if not move_flag:
            self.blackFrame.reverse()
            self.osanaLabel.reverse()
            self.logView.reverse()
            self.timerSentence.reverse()
            self.timerTimeEdit.reverse()
            self.timerStartButton.reverse()
            self.breakSentence.reverse()
            self.breakTimeEdit.reverse()
            self.breakStartButton.reverse()
            self.windowLabel.reverse()
            self.osanaText.reverse()
            self.timerBackLabel.reverse()
            self.breakBackLabel.reverse()
            self.logBackLabel.reverse()
            self.finishBackLabel.reverse()
            self.timerLabel.reverse()
            self.breakLabel.reverse()
            self.logLabel.reverse()
            self.finishLabel.reverse()
            self.timerButton.reverse()
            self.breakButton.reverse()
            self.logButton.reverse()
            self.finishButton.reverse()


        self.geometry_lists = \
            [self.blackFrame]     + \
            [self.osanaLabel]


        if not trans_flag:
            self.geometry_lists += \
                \
                [self.windowLabel]    + \
                [self.osanaText]      + \
                [self.timerButton]    + \
                [self.breakButton]    + \
                [self.logButton]      + \
                [self.finishButton]   + \
                [self.timerLabel]     + \
                [self.breakLabel]     + \
                [self.logLabel]       + \
                [self.finishLabel]


            if func == "Timer":
                self.geometry_lists += \
                    \
                    [self.timerSentence]  + \
                    [self.timerTimeEdit]  + \
                    [self.timerStartButton]  + \
                    [self.timerBackLabel]


            elif func == "Break":
                self.geometry_lists += \
                    \
                    [self.breakSentence]  + \
                    [self.breakTimeEdit]  + \
                    [self.breakStartButton]  + \
                    [self.breakBackLabel]


            elif func == "Log":
                self.geometry_lists += \
                    \
                    [self.logView]      + \
                    [self.logBackLabel]


            elif func == "Finish":
                self.geometry_lists += \
                    \
                    [self.finishBackLabel]


        elif trans_flag == "Timer":
            if func == "Log":
                self.blackFrame = [[  0,  0,  0,  0], [  0,  0,  0,0.4]]
                self.osanaLabel = [[ 20,130,370,470], [220,  0,370,470]]
