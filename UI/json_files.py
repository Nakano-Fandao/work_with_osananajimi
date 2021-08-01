import json, os

class JsonFiles:
    def __init__(self):
        # Load json file
        json_path = os.path.join(os.path.dirname(__file__),'json')

        with open(json_path+"/voice.json", encoding="utf-8_sig") as f:
            self.voice = json.load(f)
        self.voice = self.voice["voice"]

        with open(json_path+"/correspondence.json", encoding="utf-8_sig") as f:
            self.correspondence = json.load(f)

        with open(json_path+"/choicechat.json", encoding="utf-8_sig") as f:
            self.choicechat = json.load(f)
