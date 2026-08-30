import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'cats.jpg')

img = cv.imread(img_path)

cv.imshow('Cats', img)

cv.waitKey(0)