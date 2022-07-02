from ast import While
import cv2
from cv2 import COLOR_BAYER_BG2BGR
import numpy as np

img = cv2.VideoCapture(0)

img.set(3,640)
img.set(4,460)

mountain = cv2.imread('mount everest.jpg')

while True:
    status,frame=img.read()

    if status:
        frame=cv2.filp(frame,1)
        frame_rgb=cv2.cvtColor(frame,COLOR_BGR2RGB)

        #creating treshold

        lowwer_g = np.array([10,255,255])
        upper_g = np.array([255,55,25])

        # thresholding image

        ret, mountain = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)