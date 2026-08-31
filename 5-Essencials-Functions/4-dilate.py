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

# Dilatar los bordes encontrados
# Parámetros: (imagen_origen, tamaño_del_kernel, iteraciones)
img_dilated = cv.dilate(img_canny, (7,7), iterations=1)
"""
Una iteración es simplemente el número de veces consecutivas que OpenCV ejecuta el proceso matemático de expansión sobre la misma imagen.

iterations=1: El sistema desliza la cuadrícula (Kernel) sobre la imagen original de bordes (Canny) una sola vez. Añade una única capa de "pintura blanca" al perímetro de los objetos.

iterations=2: OpenCV toma el resultado del paso anterior (cuyas líneas ya están engrosadas) y le vuelve a aplicar la cuadrícula encima. Añade una segunda capa de píxeles blancos, haciendo la línea aún más ancha.

iterations=5: Repite el ciclo de expansión cinco veces. Los bordes blancos crecen agresivamente hacia afuera, fusionándose unos con otros y destruyendo los detalles finos.
"""

cv.imshow('Original', img)
cv.imshow('Image Blur', img_blur)
cv.imshow('Image with canny', img_canny)
cv.imshow('Image with dilated', img_dilated)

cv.waitKey(0)