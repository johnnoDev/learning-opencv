import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '../..', 'Photos', 'park.jpg')

img = cv.imread(img_path)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Original', img)
cv.imshow('Photo Grey', img_grey)

cv.waitKey(0)