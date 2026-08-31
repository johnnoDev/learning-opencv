import os
import cv2 as cv
import numpy as np

img_path = os.path.join(os.path.dirname(__file__), '../..', 'Photos', 'cats.jpg')
img = cv.imread(img_path)
cv.imshow('Original', img)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=0.5)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Image rotated', rotated)

cv.waitKey(0)