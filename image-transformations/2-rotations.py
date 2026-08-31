import os
import cv2 as cv
import numpy as np

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')
img = cv.imread(img_path)
cv.imshow('Original', img)

def rotate(img, angle, rotPoint=None):
    if rotPoint is None:
        rotPoint = ...

cv.waitKey(0)