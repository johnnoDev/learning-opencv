import os
import cv2 as cv
import numpy as np

"""
Nivel 1 -- Mecánica

Cargá park.jpg y mostrala en BGR, gris, HSV y LAB en 4 ventanas. Fijate cómo se ven "raras" HSV y LAB cuando imshow las interpreta como si fueran BGR.
Imprimí img.shape, gray.shape y hsv.shape. ¿Por qué gris tiene 2 valores en la tupla y las otras 3?
Convertí img a RGB y de vuelta a BGR. Restá las dos imágenes BGR (cv.absdiff) y verificá que la diferencia es todo ceros.
"""

img_path = os.path.join(os.path.dirname(__file__), '../..', 'Photos', 'park.jpg')
bgr = cv.imread(img_path)
(height, width) = bgr.shape[:2]
cv.imshow('Original (BGR)', bgr)

# canva = np.zeros((height, width), dtype='uint8')
# cv.imshow('Canva', canva)

gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
cv.imshow('BGR --> Gray', gray)

hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
cv.imshow('BGR --> HSV', hsv)

lab = cv.cvtColor(bgr, cv.COLOR_BGR2LAB)
cv.imshow('BGR --> LAB', lab)

print(f'Img (BGR) shape: {bgr.shape}')
print(f'Gray shape: {gray.shape}')
print(f'HSV shape: {hsv.shape}')

# Convertí img a RGB y de vuelta a BGR. Restá las dos imágenes BGR (cv.absdiff) y verificá que la diferencia es todo ceros.
rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
back_bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)

diff = cv.absdiff(bgr, back_bgr)
cv.imshow('Differente into images BGR\'s', diff)


cv.waitKey(0)
