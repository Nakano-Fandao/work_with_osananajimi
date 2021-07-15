class Geometry:
    def __init__(self, func, move_flag, switching_flag):

        #* ----------------------------before-----------------after---------
        self.blackFrame       = [[  0,   0,   0,   0], [  0,   0,   0,   0]]
        self.osanaLabel       = [[220,  40, 370, 470], [220,   0, 370, 470]]
        self.windowLabel      = [[ 20, 405, 760, 182], [ 20, 525, 760, 182]]
        self.osanaText        = [[ 30, 470, 740, 105], [ 30, 600, 740, 105]]

        self.logView          = [[410, 470, 330, 100], [410, 160, 330, 380]]

        self.timerWidget      = [[110, 470, 400, 100], [110, 230, 400, 560]]

        self.breakWidget      = [[210, 470, 400, 100], [210, 230, 400, 560]]

        self.logBackLabel     = [[370, 470, 400, 100], [370,  90, 400, 560]]
        self.finishBackLabel  = [[665, 470, 110, 100], [665, 380, 110, 210]]

        self.finishYesButton  = [[670, 470, 100,  40], [670, 430, 100,  40]]
        self.finishNoButton   = [[670, 520, 100,  40], [670, 480, 100,  40]]

        self.timerLabel       = [[370, 410, 108,  79], [370, 190, 108,  79]]
        self.breakLabel       = [[470, 410, 108,  79], [470, 190, 108,  79]]
        self.logLabel         = [[570, 410, 108,  79], [570,  50, 108,  79]]
        self.finishLabel      = [[670, 410, 108,  79], [670, 350, 108,  79]]

        self.timerButton      = [[377, 414, 101,  40], [377, 260, 101,  60]]
        self.breakButton      = [[477, 414, 101,  40], [477, 200, 101,  60]]
        self.logButton        = [[577, 414, 101,  40], [577,  60, 101,  60]]
        self.finishButton     = [[677, 414, 101,  40], [677, 360, 101,  60]]
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
            self.osanaLabel[1]      = [ 20, 130, 370, 470]
            self.timerLabel[1][1]   = 534
            self.breakLabel[1][1]   = 534
            self.finishLabel[1][1]  = 534
            self.timerButton[1][1]  = 544
            self.breakButton[1][1]  = 544
            self.finishButton[1][1] = 544

        elif self.func == "Finish":
            self.blackFrame[1][3]   = 0.5
            self.osanaLabel[1]      = [220, 110, 370, 470]
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
            self.timerWidget.reverse()

        if self.switching_flag != "Break":
            self.breakWidget.reverse()

        if self.switching_flag != "Log":
            self.logView.reverse()
            self.logBackLabel.reverse()

        if self.switching_flag != "Finish":
            self.finishYesButton.reverse()
            self.finishNoButton.reverse()
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
                [self.timerWidget]

        if (self.func == "Break") | (self.switching_flag == "Break"):
            self.geometry_lists += \
                \
                [self.breakWidget]

        if (self.func == "Log") | (self.switching_flag == "Log"):
            self.geometry_lists += \
                \
                [self.logView]      + \
                [self.logBackLabel]

        if (self.func == "Finish") | (self.switching_flag == "Finish"):
            self.geometry_lists += \
                \
                [self.finishYesButton] + \
                [self.finishNoButton]  + \
                [self.finishBackLabel]


    def add_objects_for_switching_tabs(self):


        #* remove windowLabel & osanaText
        self.geometry_lists.pop(2)
        self.geometry_lists.pop(2)
        #* blackFrame
        self.geometry_lists[0][1] = [  0,  0,  0,  0]
        #* osanaLabel
        self.geometry_lists[1][1] = [220,  0,370,470]
        #* Labels & Buttons
        self.geometry_lists[2][1] = [377,544,101, 60]
        self.geometry_lists[3][1] = [477,544,101, 60]
        self.geometry_lists[4][1] = [577,544,101, 60]
        self.geometry_lists[5][1] = [677,544,101, 60]
        self.geometry_lists[6][1] = [370,534,108, 79]
        self.geometry_lists[7][1] = [470,534,108, 79]
        self.geometry_lists[8][1] = [570,534,108, 79]
        self.geometry_lists[9][1] = [670,534,108, 79]

        if self.func == "Timer":
            """
            2 : timerButton
            6 : timerLabel
            10: timerWidget
            """
            self.geometry_lists[10][1] = [110, 600, 400, 560]

            if self.switching_flag == "Break":
                """
                3 : breakButton
                7 : breakLabel
                11: breakWidget
                """
                self.geometry_lists[3][1]  = [477,200,101, 60]
                self.geometry_lists[7][1]  = [470,190,108, 79]
                self.geometry_lists[11][0] = [210,600,400,560]

            elif self.switching_flag == "Log":
                """
                1 : osanaLabel
                4 : logButton
                8 : logLabel
                11: logView
                12: logBackLabel
                """
                self.geometry_lists[1][1]  = [ 20,130,370,470]
                self.geometry_lists[4][1]  = [577, 60,101, 60]
                self.geometry_lists[8][1]  = [570, 50,108, 79]
                self.geometry_lists[11][0] = [410,670,330,380]
                self.geometry_lists[12][0] = [370,600,400,560]

            elif self.switching_flag == "Finish":
                """
                0 : blackFrame
                1 : osanaLabel
                5 : finishButton
                9 : finishLabel
                11: finishYesButton
                12: finishNoButton
                13: finishBackLabel
                """
                self.geometry_lists[0][1][3] = 0.5
                self.geometry_lists[1][1]  = [220,110,370,470]
                self.geometry_lists[5][1]  = [677,360,101, 60]
                self.geometry_lists[9][1]  = [670,350,108, 79]
                self.geometry_lists[11][0] = [670,650,100, 40]
                self.geometry_lists[12][0] = [670,700,100, 40]
                self.geometry_lists[13][0] = [665,600,110,150]

        elif (self.func == "Break") & (self.switching_flag == "Timer"):
            """
            2 : timerButton
            6 : timerLabel
            10: timerWidget
            11: breakWidget
            """
            self.geometry_lists[2][1]  = [377,200,101, 60]
            self.geometry_lists[6][1]  = [370,190,108, 79]
            self.geometry_lists[10][0] = [110,600,400,560]
            self.geometry_lists[11][1] = [210,600,400,560]

        elif self.func == "Break":
            """
            10: breakWidget
            """
            self.geometry_lists[10][1] = [210,600,400,560]

            if self.switching_flag == "Log":
                """
                1 : osanaLabel
                4 : logButton
                8 : logLabel
                14: logView
                15: logBackLabel
                """
                self.geometry_lists[1][1]  = [ 20,130,370,470]
                self.geometry_lists[4][1]  = [577, 60,101, 60]
                self.geometry_lists[8][1]  = [570, 50,108, 79]
                self.geometry_lists[11][0] = [410,670,330,380]
                self.geometry_lists[12][0] = [370,600,400,560]

            elif self.switching_flag == "Finish":
                """
                0 : blackFrame
                1 : osanaLabel
                5 : finishButton
                9 : finishLabel
                14: finishYesButton
                15: finishNoButton
                16: finishBackLabel
                """
                self.geometry_lists[0][1][3] = 0.5
                self.geometry_lists[1][1]  = [220,110,370,470]
                self.geometry_lists[5][1]  = [677,360,101, 60]
                self.geometry_lists[9][1]  = [670,350,108, 79]
                self.geometry_lists[11][0] = [670,650,100, 40]
                self.geometry_lists[12][0] = [670,700,100, 40]
                self.geometry_lists[13][0] = [665,600,110,150]

        elif (self.func == "Log") & (self.switching_flag == "Timer"):
            """
            2 : timerButton
            6 : timerLabel
            10: timerWodget
            11: logView
            12: logBackLabel
            """
            self.geometry_lists[2][1]  = [377,200,101, 60]
            self.geometry_lists[6][1]  = [370,190,108, 79]
            self.geometry_lists[10][0] = [110,600,400,560]
            self.geometry_lists[11][1] = [410,670,330,380]
            self.geometry_lists[12][1] = [370,600,400,560]

        elif (self.func == "Log") & (self.switching_flag == "Break"):
            """
            3 : breakButton
            7 : breakLabel
            10: breakWidget
            11: logView
            12: logBackLabel
            """
            self.geometry_lists[3][1]  = [477,200,101, 60]
            self.geometry_lists[7][1]  = [470,190,108, 79]
            self.geometry_lists[10][0] = [210,600,400,560]
            self.geometry_lists[11][1] = [410,670,330,380]
            self.geometry_lists[12][1] = [370,600,400,560]

        elif (self.func == "Log") & (self.switching_flag == "Finish"):
            """
            0 : blackFrame
            1 : osanaLabel
            5 : finishButton
            9 : finishLabel
            10: logView
            11: logBackLabel
            12: finishYesButton
            13: finishNoButton
            14: finishBackLabel
            """
            self.geometry_lists[0][1][3] = 0.5
            self.geometry_lists[1][1]  = [220,110,370,470]
            self.geometry_lists[5][1]  = [677,360,101, 60]
            self.geometry_lists[9][1]  = [670,350,108, 79]
            self.geometry_lists[10][1] = [410,670,330,380]
            self.geometry_lists[11][1] = [370,600,400,560]
            self.geometry_lists[12][0] = [670,650,100, 40]
            self.geometry_lists[13][0] = [670,700,100, 40]
            self.geometry_lists[14][0] = [665,600,110,150]


        elif (self.func == "Finish") & (self.switching_flag == "Timer"):
            """
            0 : blackFrame
            1 : osanaLabel
            2 : timerButton
            6 : timerLabel
            10: timerWidget
            11: finishYesButton
            12: finishNoButton
            13: finishBackLabel
            """
            self.geometry_lists[0][0][3] = 0.5
            self.geometry_lists[1][0]  = [220,110,370,470]
            self.geometry_lists[2][1]  = [377,200,101, 60]
            self.geometry_lists[6][1]  = [370,190,108, 79]
            self.geometry_lists[10][0] = [110,600,400,560]
            self.geometry_lists[11][1] = [670,650,100, 40]
            self.geometry_lists[12][1] = [670,700,100, 40]
            self.geometry_lists[13][1] = [665,600,110,150]

        elif (self.func == "Finish") & (self.switching_flag == "Break"):
            """
            0 : blackFrame
            1 : osanaLabel
            3 : breakButton
            7 : breakLabel
            10: breakWidget
            11: finishYesButton
            12: finishNoButton
            13: finishBackLabel
            """
            self.geometry_lists[0][0][3] = 0.5
            self.geometry_lists[1][0]  = [220,110,370,470]
            self.geometry_lists[3][1]  = [477,200,101, 60]
            self.geometry_lists[7][1]  = [470,190,108, 79]
            self.geometry_lists[10][0] = [210,600,400,560]
            self.geometry_lists[11][1] = [670,650,100, 40]
            self.geometry_lists[12][1] = [670,700,100, 40]
            self.geometry_lists[13][1] = [665,600,110,150]

        elif (self.func == "Finish") & (self.switching_flag == "Log"):
            """
            0 : blackFrame
            1 : osanaLabel
            4 : logButton
            8 : logLabel
            10: logView
            11: logBackLabel
            12: finishYesButton
            13: finishNoButton
            14: finishBackLabel
            """
            self.geometry_lists[0][0][3] = 0.5
            self.geometry_lists[1][0]  = [220,110,370,470]
            self.geometry_lists[1][1]  = [ 20,130,370,470]
            self.geometry_lists[4][1]  = [577, 60,101, 60]
            self.geometry_lists[8][1]  = [570, 50,108, 79]
            self.geometry_lists[10][0] = [410,670,330,380]
            self.geometry_lists[11][0] = [370,600,400,560]
            self.geometry_lists[12][1] = [670,650,100, 40]
            self.geometry_lists[13][1] = [670,700,100, 40]
            self.geometry_lists[14][1] = [665,600,110,150]
