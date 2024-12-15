import cv2
from matplotlib import pyplot as plt
import numpy as np
path = 'screen.png'
image = cv2.imread(path)
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("The coordinates of the left mouse click are (%d, %d)" % (x, y))
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", on_mouse)
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, result = cv2.threshold(img,85,255, cv2.THRESH_BINARY)

cv2.imshow("Image", image)
cv2.waitKey(0)