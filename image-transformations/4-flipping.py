import os
import cv2 as cv
import numpy as np

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')
img = cv.imread(img_path)
cv.imshow('Original', img)

# Función voltear
# 0 -> vertical | 1 -> horizontal | -1 -> ambos
flipped = cv.flip(img, 0)
cv.imshow('Image flipped', flipped)


cv.waitKey(0)