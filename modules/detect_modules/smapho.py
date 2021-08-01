import cv2

import time
from camera import Camera
from detect_smapho_tool import load_detector, simple_judge_smapho


class DetectSmaphoClass(Camera):
    def __init__(self):
        Camera.__init__(self)
        print("******Camera opened*********")

        self.face_parts_detector, self.detector = load_detector()

        print("******Preparation ends******")

    def judge_smapho(self):
        print("******Smapho Detection starts********")
        resized_image = self.get_resized_face_image()
        smapho_touching = simple_judge_smapho(self.face_parts_detector, self.detector, resized_image)
        return smapho_touching

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    detect = DetectSmaphoClass()
    while True:
        detect.judge_smapho()
        time.sleep(1)
