import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '../..', 'Photos', 'park.jpg')

img = cv.imread(img_path)

img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Aplicar desenfoque gaussiano (el kernel debe ser estrictamente de números impares)
img_blur = cv.GaussianBlur(img_grey, (3,3), cv.BORDER_DEFAULT)

# Pasamos la imagen ya difuminada para que Canny ignore las hojas del parque
# Los parámetros numéricos son (imagen, umbral_inferior, umbral_superior)
img_canny = cv.Canny(img_blur, 125, 175)

# Dilatar los bordes encontrados
# Parámetros: (imagen_origen, tamaño_del_kernel, iteraciones)
img_dilated = cv.dilate(img_canny, (7,7), iterations=3)

# Desgastar los bordes previamente dilatados
# Es crucial usar el mismo tamaño de kernel que usaste en la dilatación
img_eroded = cv.erode(img_dilated, (7,7), iterations=3)

img_resized = cv.resize(img_eroded, (500, 500), interpolation=cv.INTER_CUBIC) # cv.INTER_CUBIC es un algoritmo lento pero de altísima calidad. Si necesitas encoger imágenes rápido para un video en vivo, suele usarse cv.INTER_AREA.

cv.imshow('Original', img)
cv.imshow('Image Blur', img_blur)
cv.imshow('Image with canny', img_canny)
cv.imshow('Image with dilated', img_dilated)
cv.imshow('Image with eroded', img_eroded)
cv.imshow('Resized', img_resized)

# Cropping
img_cropped = img[200:300, 300:400]
cv.imshow('Image cropped', img_cropped)


cv.waitKey(0)