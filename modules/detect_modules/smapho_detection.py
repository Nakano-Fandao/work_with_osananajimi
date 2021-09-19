import cv2, time
from detect_smapho_tool import PoseEstimator

class SmaphoDetection():
    def __init__(self):
        self.estimator = PoseEstimator()

    def judge_smapho(self):
        #* ******Smapho Detection starts********
        is_head_pose_down = self.estimator.estimate_head_pose()
        return is_head_pose_down

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detect = SmaphoDetection()
    while True:
        detect.judge_smapho()
        time.sleep(1)
