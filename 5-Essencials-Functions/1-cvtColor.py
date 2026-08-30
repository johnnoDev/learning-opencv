import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'cat.jpg')

img = cv.imread(img_path)

# Aplicar la conversión usando la constante BGR a GRAY
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Original', img)

cv.imshow('Picture Grey', img_grey)

cv.waitKey(0)