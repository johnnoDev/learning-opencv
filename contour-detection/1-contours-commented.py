# cv2 = OpenCV (Open Source Computer Vision), aliasada como cv.
import cv2 as cv

# numpy = Numerical Python. La usamos para crear un lienzo (canvas) en negro
# donde vamos a dibujar los contornos encontrados.
import numpy as np

import os

# Armamos la ruta a la imagen subiendo un nivel ('..') hasta 'Photos'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'cats.jpg')

# imread = image read (leer imagen).
img = cv.imread(img_path)
cv.imshow('Cats', img)

# blank = "en blanco". Creamos un lienzo negro del MISMO tamaño que la
# imagen original (mismo alto, ancho y canales), relleno de ceros.
# dtype='uint8' = unsigned int de 8 bits (0 a 255), el mismo tipo que usan
# las imágenes normales. Ahí vamos a dibujar los contornos, no sobre la foto.
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# ============== Paso 1: escala de grises ===================
# cvtColor = "convert color" = convertir color.
# findContours necesita una imagen de UN solo canal (gris), no BGR de 3.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# ============== Paso 2: reducir ruido ===================
# GaussianBlur = desenfoque gaussiano. Suaviza la imagen para que el
# detector de bordes no confunda "ruido" (granulado de la foto) con bordes
# reales. (5,5) es el tamaño del kernel: debe ser impar.
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# ============== Paso 3: detectar bordes ===================
# Canny = nombre del algoritmo (por su creador, John F. Canny).
# Devuelve una imagen binaria (blanco = borde, negro = no-borde).
# 125 y 175 son los umbrales (thresholds) mínimo y máximo para decidir
# qué gradientes de intensidad se consideran "borde".
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ============== Alternativa: binarizar por threshold ===================
# threshold = umbral. Convierte la imagen gris en blanco y negro puro:
# todo píxel con intensidad >= 125 se vuelve 255 (blanco), el resto 0 (negro).
# THRESH_BINARY = "threshold binary" = umbral binario (blanco/negro, sin grises).
# Devuelve 2 valores: ret (el umbral usado) y thresh (la imagen resultante).
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# ============== Paso 4: encontrar los contornos ===================
# findContours = "find contours" = encontrar contornos.
# Recibe una imagen binaria (blanco/negro) y devuelve:
#   contours   : lista de contornos. Cada contorno es un array de puntos (x,y)
#                que forman el borde de una figura.
#   hierarchies: la relación de "padre/hijo" entre contornos (ej: un contorno
#                que está DENTRO de otro, como un agujero en una dona).
#
# Argumentos:
#   1) canny             : la imagen binaria de bordes (también podría ser 'thresh').
#   2) RETR_LIST          : "retrieval mode" = modo de recuperación.
#                            LIST = devolver TODOS los contornos, sin jerarquía.
#   3) CHAIN_APPROX_SIMPLE : "chain approximation" = aproximación de la cadena
#                            de puntos. SIMPLE comprime los puntos redundantes
#                            (ej: una línea recta la guarda como 2 puntos, no 100).
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# len(contours) = cuántos contornos (figuras/bordes) se encontraron.
print(f'{len(contours)} contorno(s) encontrado(s)!')

# ============== Paso 5: dibujar los contornos ===================
# drawContours = "draw contours" = dibujar contornos.
# Argumentos:
#   1) blank      : la imagen donde se dibuja (nuestro lienzo negro).
#   2) contours   : la lista de contornos a dibujar.
#   3) -1         : índice del contorno a dibujar. -1 = TODOS.
#   4) (0, 0, 255): color en BGR (acá: rojo puro).
#   5) 1          : grosor de línea en píxeles.
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

# waitKey(0) = esperar tecla indefinidamente para no cerrar las ventanas.
cv.waitKey(0)
