import json, os

class JsonFiles:
    def __init__(self):
        # Load json file
        json_path = os.path.join(os.path.dirname(__file__),'../UI/json')

        with open(json_path+"/voice.json") as f:
            self.voice = json.load(f)
        self.voice = self.voice["voice"]

        with open(json_path+"/correspondence.json") as f:
            self.correspondence = json.load(f)

        with open(json_path+"/choicechat.json") as f:
            self.choicechat = json.load(f)
