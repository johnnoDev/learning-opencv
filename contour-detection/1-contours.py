import cv2 as cv
import numpy as np
import os

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'cats.jpg')

img = cv.imread(img_path)
cv.imshow('Cats', img)

canva = np.zeros(img.shape, dtype='uint8')

# Image Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Gaussian Blur
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Canny
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'Contornos totales: {len(contours)}')

# Dibujar el contorno
cv.drawContours(canva, contours, -1, (0,0,255), 1)

cv.imshow('Contours Drawn', canva)


cv.waitKey(0)