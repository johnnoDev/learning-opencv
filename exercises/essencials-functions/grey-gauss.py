"""
Reto 2 (Encadenamiento de funciones): Construye un flujo donde primero conviertas una imagen a escala de grises (cv2.cvtColor) y luego le apliques el desenfoque gaussiano (cv2.GaussianBlur) al resultado obtenido en grises, mostrando la imagen final en pantalla.
"""


import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '../..', 'Photos', 'park.jpg')

img = cv.imread(img_path)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_grey, (21, 21), cv.BORDER_DEFAULT)

cv.imshow('Picture updated', img_blur)

cv.waitKey(0)