import os
import cv2 as cv
import numpy as np

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')
img = cv.imread(img_path)
cv.imshow('Original', img)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Image Resized', resized)


cv.waitKey(0)