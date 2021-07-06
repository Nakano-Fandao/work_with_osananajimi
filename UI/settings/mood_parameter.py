class MoodParameter:
    def __init__(self, parameter):

        max = 100
        min = 0

        threshold_1 = int(max * 0.9)
        threshold_2 = int(max * 0.65)
        threshold_3 = int(max * 0.35)
        threshold_4 = int(max * 0.10)

        if max >= parameter >= threshold_1:
            self.mood = "great"
        elif threshold_1 > parameter >= threshold_2:
            self.mood = "good"
        elif threshold_2 > parameter >= threshold_3:
            self.mood = "normal"
        elif threshold_3 > parameter >= threshold_4:
            self.mood = "awkward"
        else:
            self.mood = "bad"
