#! /usr/bin/python
# -*- coding: utf-8 -*-

import cv2, dlib, os, numpy as np
from imutils import face_utils

from camera import Camera
from eye import Eye

class PoseEstimator():
    def __init__(self):
        self.landmark_detector = dlib.shape_predictor(os.path.join(os.path.dirname(__file__), "./model/shape_predictor_68_face_landmarks.dat"))
        self.face_detector = dlib.get_frontal_face_detector()
        print("******Detector loaded*******")

        self.EYE_THRESHOLD = 0.4
        self.HEAD_POSE_THRESHOLD = 60

        self.camera = Camera()
        print("******Camera opened*********")

    #* 黒目の大きさから推定
    def judge_eye(self, debug=False):
        #* カメラキャプチャーの画像をリサイズ
        image = self.camera.get_resized_face_image()
        #* グレースケール
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        #* 顔検出
        rects = self.face_detector(gray, 1)

        #* Dlibの顔検出箇所の矩型描画ループ
        for dets in rects:
            #* 顔画像のランドマークを取得する
            landmark_dets = self.landmark_detector(gray, dets)
            landmark = face_utils.shape_to_np(landmark_dets)

            if debug:
                #* ランドマーク68箇所に数字表示変数を初期化
                for (xx, yy) in landmark:
                    #* 顔の1箇所毎に合計68箇所にプロットする
                    cv2.circle(image, (xx,yy),2, (0,255,0), thickness= -1)

            #* 両目情報の取得
            eye = Eye(landmark)
            #* 両目閉じているかチェック
            if (eye.left_eye_ear + eye.right_eye_ear) < self.EYE_THRESHOLD:
                print(eye.left_eye_ear + eye.right_eye_ear)
                #* 目を閉じるメッセージを出力
                print("スマホ触ってんにぇ!!!")
                if not debug: return True
            else:
                if debug:
                    #* 目中心位置算出とに描画
                    center_right_eye,center_left_eye = eye.get_eye_center(landmark_dets)
                    eye.draw_eye_center(image, center_right_eye)
                    eye.draw_eye_center(image, center_left_eye)
                else:
                    return False

        if debug:
            #* ウィンドウに表示
            cv2.moveWindow("DLIB_Landmark", 450, 100)
            cv2.imshow('DLIB_Landmark', image)

    #* 頭部姿勢推定のための3Dモデルの座標校正
    def caribrate_3dmodel(self):
        #* カメラキャプチャーの画像をリサイズ
        image = self.camera.get_resized_face_image()
        #* グレースケール
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        #* 顔検出
        rects = self.face_detector(gray, 1)

        image_points = None
        for rect in rects:
            landmark_dets = self.landmark_detector(gray, rect)
            landmark = face_utils.shape_to_np(landmark_dets)
            #* 鼻先との相対座標
            cal = landmark - landmark[30]
            print("######[X,Y]#######",
                "\n point31=",cal[30],
                "\n point52=",cal[51],
                "\n point37=",cal[36],
                "\n point46=",cal[45],
                "\n point49=",cal[48],
                "\n point55=",cal[54])

            for i, (x, y) in enumerate(landmark):
                if i in set([30, 51, 36, 45, 48, 54]):
                    cv2.circle(image, (x, y), 1, (255, 255, 255), -1)
                    cv2.putText(image, str((x, y)-landmark[30]),(x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255), 2)

        #* ウィンドウに表示
        cv2.moveWindow("DLIB_Landmark", 450, 100)
        cv2.imshow('DLIB_Landmark', image)

    #* 頭部姿勢推定
    def estimate_head_pose(self, debug=False):
        #* カメラキャプチャーの画像をリサイズ
        image = self.camera.get_resized_face_image()
        #* グレースケール
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        #* 顔検出
        rects = self.face_detector(gray, 1)

        image_points = None
        for rect in rects:
            shape = self.landmark_detector(gray, rect)
            shape = face_utils.shape_to_np(shape)

            if debug:
                #* 顔全体の68箇所のランドマークをプロット
                for (x, y) in shape:
                    cv2.circle(image, (x, y), 1, (255, 255, 255), -1)

            image_points = np.array([
                tuple(shape[30]), #* 鼻先
                tuple(shape[51]),  #* 顎先
                tuple(shape[36]), #* 左目尻
                tuple(shape[45]), #* 右目尻
                tuple(shape[48]), #* 口左端点
                tuple(shape[54]), #* 口右端点
            ], dtype='double')

        if len(rects) > 0:
            model_points = np.array([
                (   0.0,    0.0,   0.0), #* 鼻先
                (   0.0,  -37.0, -20.0), #* 顎先
                ( -60.0,   45.0, -30.0), #* 左目尻
                (  60.0,   45.0, -30.0), #* 右目尻
                ( -33.0,  -45.0, -50.0), #* 口左端点
                (  33.0,  -45.0, -50.0)  #* 口右端点
            ])

            size = image.shape
            focal_length = size[1]
            center = (size[1] // 2, size[0] // 2)
            camera_matrix = np.array([
                [focal_length,            0,   center[0]],
                [           0, focal_length,   center[1]],
                [           0,            0,           1]
            ], dtype='double')
            #* レンズの歪みがないと仮定
            dist_coeffs = np.zeros((4, 1))

            (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
            #* 回転行列とヤコビアン
            (rotation_matrix, jacobian) = cv2.Rodrigues(rotation_vector)
            mat = np.hstack((rotation_matrix, translation_vector))

            #* yaw,pitch,rollの取り出し
            (_, _, _, _, _, _, eulerAngles) = cv2.decomposeProjectionMatrix(mat)
            yaw = eulerAngles[1]
            pitch = eulerAngles[0]
            roll = eulerAngles[2]

            # print("yaw",int(yaw),"pitch",int(pitch),"roll",int(roll))
            (nose_end_point2D, _) = cv2.projectPoints(np.array([(0.0, 0.0, 500.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
            p1 = (int(image_points[0][0]), int(image_points[0][1]))
            p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
            y_vector_dif = p2[1]-p1[1]
            print(y_vector_dif)

            if not debug:
                #* アウトならTrueを返す
                return y_vector_dif > self.HEAD_POSE_THRESHOLD
            else:
                cv2.putText(image, 'yaw : ' + str(int(yaw)), (20, 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                cv2.putText(image, 'pitch : ' + str(int(pitch)), (20, 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                cv2.putText(image, 'roll : ' + str(int(roll)), (20, 40), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

                #* 計算に使用した点のプロット/顔方向のベクトルの表示
                for p in image_points:
                    cv2.drawMarker(image, (int(p[0]), int(p[1])),  (0.0, 1.409845, 255), markerType=cv2.MARKER_CROSS, thickness=1)

                cv2.arrowedLine(image, p1, p2, (255, 0, 0), 2)

        if debug:
            #* ウィンドウに表示
            cv2.moveWindow("DLIB_Landmark", 450, 100)
            cv2.imshow('DLIB_Landmark', image)

    #* Debug
    def debug(self):
        while True:
            # judge_smapho(self.landmark_detector, detector, camera)
            self.estimate_head_pose(True)

            #* ESCキーで終了
            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break

        self.camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    pose_estimator = PoseEstimator()
    pose_estimator.debug()
