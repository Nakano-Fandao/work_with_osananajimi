import cv2
import numpy as np
from scipy.spatial import distance

class Eye:
    def __init__(self, face_parts):
        ############ 左目 ###########
        left_eye = face_parts[42:48]
        self.left_eye_ear = self.calc_eye(left_eye)
        ############ 右目 ###########
        right_eye = face_parts[36:42]
        self.right_eye_ear = self.calc_eye(right_eye)

    # 目が閉じているか計算する
    def calc_eye(self, eye):
        p2_p6 = distance.euclidean(eye[1], eye[5])
        p3_p5 = distance.euclidean(eye[2], eye[4])
        p1_p4 = distance.euclidean(eye[0], eye[3])
        EAR = (p2_p6 + p3_p5) / (2.0 * p1_p4)
        return round(EAR,3)

    # 目の中心位置算出
    def get_eye_center(self, shape):
        eyel, eyer = np.array([0, 0]), np.array([0, 0])
        # 左目の位置
        for i in range(36, 42):
            eyel[0] += shape.part(i).x
            eyel[1] += shape.part(i).y
        # 右目の位置
        for i in range(42, 48):
            eyer[0] += shape.part(i).x
            eyer[1] += shape.part(i).y
        return eyel / 6, eyer / 6

    # 目の中心を表示
    def draw_eye_center(self, image, eye):
        cv2.circle(image, (int(eye[0]),int(eye[1])), 3, (0, 0, 255), -1)
