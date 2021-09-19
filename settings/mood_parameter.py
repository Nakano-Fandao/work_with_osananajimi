from json_files import JsonFiles

class MoodParameter:
    def __init__(self):

        self.osananajimi = JsonFiles().osananajimi

        self.parameter = 50
        self.mood = "normal"
        self.max = 100
        self.min = 0
        self.threshold_1 = int(self.max * 0.9)
        self.threshold_2 = int(self.max * 0.65)
        self.threshold_3 = int(self.max * 0.35)
        self.threshold_4 = int(self.max * 0.10)

    def set(self, parameter):
        self.parameter = parameter
        self.change(0)

    def change(self, dif):
        self.parameter += dif

        if self.max >= self.parameter >= self.threshold_1:
            self.mood = "great"
        elif self.threshold_1 > self.parameter >= self.threshold_2:
            self.mood = "good"
        elif self.threshold_2 > self.parameter >= self.threshold_3:
            self.mood = "normal"
        elif self.threshold_3 > self.parameter >= self.threshold_4:
            self.mood = "awkward"
        else:
            self.mood = "bad"

    def get_osana_image(self, action=None):
        if action == None:
            return self.osananajimi[self.mood]
        else:
            return self.osananajimi[action]