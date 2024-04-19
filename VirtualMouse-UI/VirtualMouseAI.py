import cv2

import time
###########################################
wCam, hCam = 1000, 640
#########################
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)




