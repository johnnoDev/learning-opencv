import os
import cv2 as cv
import numpy as np

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')
img = cv.imread(img_path)
cv.imshow('Original', img)

cropped = img[200:300, 400:500]
cv.imshow('Image cropped', cropped)



cv.waitKey(0)