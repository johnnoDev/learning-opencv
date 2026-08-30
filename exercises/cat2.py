import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'cats 2.jpg')

img = cv.imread(img_path)

cv.imshow('Cat 2', img)

cv.waitKey(0)