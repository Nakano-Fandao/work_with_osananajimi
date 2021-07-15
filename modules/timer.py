class Timer:
    def __init__(self, str_time):

        whole_seconds = self.get_whole_seconds(str_time)

        self.initial_time = whole_seconds
        self.str_initial_time = self.get_str_time(whole_seconds)

        self.ten    = 600
        self.thirty = 1800
        self.half   = int(whole_seconds/2)


    #* [1] → [ 1]
    def add_space(self, str_time):
        return str_time.replace("1", " 1")

    #* 秒換算
    def get_whole_seconds(self, str_time):
        h, m, s = list(map(lambda x: int("".join(x.split())), str_time.split(":")))
        return 3600*h + 60*m + s

    def get_str_time(self, whole_seconds):
        h = whole_seconds // 3600
        if h > 0: whole_seconds -= 3600*h;

        m = whole_seconds // 60
        if m > 0: whole_seconds -= 60*m;

        s = whole_seconds
        remaining_time = f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"
        return self.add_space(remaining_time)
