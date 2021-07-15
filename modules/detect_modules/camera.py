import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        print("******Camera opens**********")

        self.frame_width = 640
        self.frame_height = 480

    def get_cap(self):
        return self.cap

    def get_frame(self):
        return self.frame_width, self.frame_height

    def get_resized_face_image(self):
        _, image = self.cap.read()
        resized_image = cv2.resize(image,dsize=(int(self.frame_width),int(self.frame_height)))
        return resized_image

    def release(self):
        self.cap.release()
