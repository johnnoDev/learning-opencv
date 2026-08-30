# Importamos la biblioteca OpenCV.
# cv2 = OpenCV, y lo aliasamos como cv para escribir menos.
import cv2 as cv

# Leemos la imagen desde la ruta indicada.
# imread = image read (leer imagen).
# './Photos/cat.jpg' es la ubicación de la imagen.
img = cv.imread('./Photos/cat.jpg')

# Mostramos la imagen en una ventana.
# imshow = image show (mostrar imagen).
# 'Cat' es el título de la ventana.
cv.imshow('Cat', img)

# Esperamos a que el usuario presione una tecla.
# waitKey = esperar tecla.
# 0 significa esperar indefinidamente hasta que se presione una tecla.
cv.waitKey(0)