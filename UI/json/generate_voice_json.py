import os, json

# Load json file
correspondence_path = os.path.join(os.path.dirname(__file__), "correspondence.json")
with open(correspondence_path, "r") as f:
    correspondence_json = json.load(f)

mood_json = {
    "great": [],
    "good": [],
    "normal": [],
    "awkward": [],
    "bad": []
}
ask_json = {
    "ask": "",
    "a": "",
    "b": "",
    "c": ""
}
sound_json = {}

sound_json["voice"] = {}
sound_json["voice"]["smapho"] = mood_json
sound_json["voice"]["youtube"] = mood_json
sound_json["voice"]["hentai"] = mood_json
sound_json["voice"]["common"] = mood_json
sound_json["voice"]["announcement"] = {"3h": "","6h": "","9h": "","12h": "","15h": "","18h": "","21h": "","24h": "",}
sound_json["voice"]["app"] = {}
sound_json["voice"]["app"]["start"] = mood_json
sound_json["voice"]["app"]["finish"] = mood_json
sound_json["voice"]["break"] = {}
sound_json["voice"]["break"]["start"] = mood_json
sound_json["voice"]["break"]["finish"] = mood_json
sound_json["voice"]["chat"] = mood_json
sound_json["voice"]["choicechat"] = mood_json
sound_json["voice"]["choicechat"]["great"] = {"1": ask_json}
sound_json["voice"]["choicechat"]["good"] = {"1": ask_json, "2": ask_json, "3": ask_json, "4": ask_json}
sound_json["voice"]["choicechat"]["normal"] = {"1": ask_json, "2": ask_json, "3": ask_json, "4": ask_json, "5": ask_json}
sound_json["voice"]["choicechat"]["awkward"] = {"1": ask_json, "2": ask_json}
sound_json["voice"]["extra"] = {"1": "", "2": "", "3": "", "4": "", "5": ""}
sound_json["voice"]["hentai"] = mood_json
sound_json["voice"]["timer"] = {}
sound_json["voice"]["timer"]["start"] = mood_json
sound_json["voice"]["timer"]["finish"] = mood_json
sound_json["voice"]["timer"]["intro"] = {"1": "", "2": "", "3": "", "4": ""}
sound_json["voice"]["timer"]["mid"] = {}
sound_json["voice"]["timer"]["mid"]["10"] = mood_json
sound_json["voice"]["timer"]["mid"]["30"] = mood_json
sound_json["voice"]["timer"]["mid"]["half"] = mood_json
sound_json["voice"]["timer"]["stop"] = mood_json
sound_json["effects"] = {
    "door_knocking": ":effect/sounds/effects/door_knocking.wav"
}

sound_path = os.path.join(os.path.dirname(__file__), "sound.json")
with open(sound_path, "w") as f:
    json.dump(sound_json, f, indent=4)
