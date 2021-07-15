#! /usr/bin/python
# -*- coding: utf-8 -*-
import cv2, dlib, time, os
from imutils import face_utils

from camera import Camera
from eye import Eye


def load_detector():
    # print(os.path.join(os.path.dirname(__file__), "model\shape_predictor_68_face_landmarks.dat"))
    face_parts_detector = dlib.shape_predictor(os.path.join(os.path.dirname(__file__), "./model/shape_predictor_68_face_landmarks.dat"))
    detector = dlib.get_frontal_face_detector()
    print("******Detector loaded*******")

    return face_parts_detector, detector


def simple_judge_smapho(face_parts_detector, detector, image):
    # グレースケール
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # 顔検出
    rects = detector(gray, 1)

    # Dlibの顔検出箇所の矩型描画ループ
    for dets in rects:
        # 顔画像のランドマークを取得する
        face_parts_dets = face_parts_detector(gray, dets)
        face_parts = face_utils.shape_to_np(face_parts_dets)

        # 両目閉じているかチェック
        eye = Eye(face_parts)
        if (eye.left_eye_ear + eye.right_eye_ear) < 0.5:
            # 目を閉じるメッセージを出力
            print("スマホ触ってんにぇ!!!")
            return "smapho"
        else:
            return False


def judge_smapho(face_parts_detector, detector, camera):

    # カメラキャプチャーを画像をリサイズ
    image = camera.get_resized_face_image()
    # グレースケール
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # 顔検出
    rects = detector(gray, 1)

    # Dlibの顔検出箇所の矩型描画ループ
    for dets in rects:
        # 顔画像のランドマークを取得する
        face_parts_dets = face_parts_detector(gray, dets)
        face_parts = face_utils.shape_to_np(face_parts_dets)

        # ランドマーク68箇所に数字表示変数を初期化
        for (xx, yy) in face_parts:
            # 顔の1箇所毎に合計68箇所にプロットする
            cv2.circle(image, (xx,yy),2, (0,255,0), thickness= -1)

        eye = Eye(face_parts)


        # 両目閉じているかチェック
        if (eye.left_eye_ear + eye.right_eye_ear) < 0.4:
            # 目を閉じるメッセージを出力
            smapho_log = "スマホ触ってんにぇ!!!"
            cv2.putText(image, smapho_log,(10,430), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
        else:
            # 目中心位置算出とに描画
            center_right_eye,center_left_eye = eye.get_eye_center(face_parts_dets)
            eye.draw_eye_center(image, center_right_eye)
            eye.draw_eye_center(image, center_left_eye)

    # ウィンドウに表示
    cv2.moveWindow("DLIB_Landmark",200,100) # Window表示位置指定
    cv2.imshow('DLIB_Landmark', image)


##############
# メイン処理  #
##############
def main():
    print("******Program starts********")

    face_parts_detector, detector = load_detector()

    #カメラデバイスオープン
    camera = Camera()
    print("******Preparation ends******")

    print("******Loop starts***********")
    while True:

        judge_smapho(face_parts_detector, detector, camera)

        # ESCキーで終了
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
