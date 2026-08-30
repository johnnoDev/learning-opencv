import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'cat.jpg')

img = cv.imread(img_path)

# Aplicar desenfoque gaussiano (el kernel debe ser estrictamente de números impares)
img_blur = cv.GaussianBlur(img, (25,25), cv.BORDER_DEFAULT)
cv.imshow('Original', img)
cv.imshow('Image Blur', img_blur)

cv.waitKey(0)