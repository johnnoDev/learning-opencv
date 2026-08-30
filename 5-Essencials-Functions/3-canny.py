import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')

img = cv.imread(img_path)

img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Aplicar desenfoque gaussiano (el kernel debe ser estrictamente de números impares)
img_blur = cv.GaussianBlur(img_grey, (3,3), cv.BORDER_DEFAULT)
# Pasamos la imagen ya difuminada para que Canny ignore las hojas del parque
# Los parámetros numéricos son (imagen, umbral_inferior, umbral_superior)
img_canny = cv.Canny(img_blur, 125, 175)

cv.imshow('Original', img)
cv.imshow('Image Blur', img_blur)
cv.imshow('Image with canny', img_canny)

cv.waitKey(0)