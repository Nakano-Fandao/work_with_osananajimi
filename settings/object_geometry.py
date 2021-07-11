class Geometry:
    def __init__(self, func, move_flag, switching_flag):

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

        self.func = func
        self.move_flag = move_flag
        self.switching_flag = switching_flag

        self.set_for_specific_cases()

        if not self.move_flag: self.reverse();

        self.add_objects()

        if self.switching_flag: self.add_objects_for_switching_tabs();


    def set_for_specific_cases(self):

        if self.func == "Timer":
            self.breakLabel[1][1]   = 534
            self.logLabel[1][1]     = 534
            self.finishLabel[1][1]  = 534
            self.breakButton[1][1]  = 544
            self.logButton[1][1]    = 544
            self.finishButton[1][1] = 544

        elif self.func == "Break":
            self.timerLabel[1][1]   = 534
            self.logLabel[1][1]     = 534
            self.finishLabel[1][1]  = 534
            self.timerButton[1][1]  = 544
            self.logButton[1][1]    = 544
            self.finishButton[1][1] = 544

        elif self.func == "Log":
            self.osanaLabel[1]      = [20, 130, 370, 470]
            self.timerLabel[1][1]   = 534
            self.breakLabel[1][1]   = 534
            self.finishLabel[1][1]  = 534
            self.timerButton[1][1]  = 544
            self.breakButton[1][1]  = 544
            self.finishButton[1][1] = 544

        elif self.func == "Finish":
            self.timerLabel[1][1]   = 534
            self.breakLabel[1][1]   = 534
            self.logLabel[1][1]     = 534
            self.timerButton[1][1]  = 544
            self.breakButton[1][1]  = 544
            self.logButton[1][1]    = 544


    def reverse(self):

        self.blackFrame.reverse()
        self.osanaLabel.reverse()

        self.windowLabel.reverse()
        self.osanaText.reverse()

        self.timerButton.reverse()
        self.breakButton.reverse()
        self.logButton.reverse()
        self.finishButton.reverse()

        self.timerLabel.reverse()
        self.breakLabel.reverse()
        self.logLabel.reverse()
        self.finishLabel.reverse()

        if self.switching_flag != "Timer":
            self.timerSentence.reverse()
            self.timerTimeEdit.reverse()
            self.timerStartButton.reverse()
            self.timerBackLabel.reverse()

        if self.switching_flag != "Break":
            self.breakSentence.reverse()
            self.breakTimeEdit.reverse()
            self.breakStartButton.reverse()
            self.breakBackLabel.reverse()

        if self.switching_flag != "Log":
            self.logView.reverse()
            self.logBackLabel.reverse()

        if self.switching_flag != "Finish":
            self.finishBackLabel.reverse()


    def add_objects(self):

        self.geometry_lists = \
            [self.blackFrame]     + \
            [self.osanaLabel]     + \
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

        if (self.func == "Timer") | (self.switching_flag == "Timer"):
            self.geometry_lists += \
                \
                [self.timerSentence]  + \
                [self.timerTimeEdit]  + \
                [self.timerStartButton]  + \
                [self.timerBackLabel]

        if (self.func == "Break") | (self.switching_flag == "Break"):
            self.geometry_lists += \
                \
                [self.breakSentence]  + \
                [self.breakTimeEdit]  + \
                [self.breakStartButton]  + \
                [self.breakBackLabel]

        if (self.func == "Log") | (self.switching_flag == "Log"):
            self.geometry_lists += \
                \
                [self.logView]      + \
                [self.logBackLabel]

        if (self.func == "Finish") | (self.switching_flag == "Finish"):
            self.geometry_lists += \
                \
                [self.finishBackLabel]


    def add_objects_for_switching_tabs(self):


        #* remove windowLabel & osanaText
        self.geometry_lists.pop(2)
        self.geometry_lists.pop(2)
        #* blackFrame
        self.geometry_lists[0][1] = [  0,  0,  0,0.4]
        #* osanaLabel
        self.geometry_lists[1][1] = [ 20,130,370,470]
        #* Labels & Buttons
        self.geometry_lists[2][1] = [377,544,101, 60]
        self.geometry_lists[3][1] = [477,544,101, 60]
        self.geometry_lists[4][1] = [577,544,101, 60]
        self.geometry_lists[5][1] = [677,544,101, 60]
        self.geometry_lists[6][1] = [377,534,108, 79]
        self.geometry_lists[7][1] = [477,534,108, 79]
        self.geometry_lists[8][1] = [577,534,108, 79]
        self.geometry_lists[9][1] = [677,534,108, 79]

        if self.func == "Timer":
            """
            2 : timerButton
            3 : timerLabel
            10: timerSentence
            11: timerTimeEdit
            12: timerStartButton
            13: timerBackLabel
            """
            self.geometry_lists[10][1] = [130, 600, 180,  50]
            self.geometry_lists[11][1] = [300, 600, 180,  50]
            self.geometry_lists[12][1] = [215, 600, 180,  42]
            self.geometry_lists[13][1] = [110, 600, 400, 100]

            if self.switching_flag == "Log":
                """
                4 : logButton
                8 : logLabel
                14: logView
                15: logBackLabel
                """
                self.geometry_lists[4][1]  = [577, 60,101, 60]
                self.geometry_lists[8][1]  = [577, 50,108, 79]
                self.geometry_lists[14][1] = [370, 90,400,560]
                self.geometry_lists[15][1] = [370, 90,400,560]
