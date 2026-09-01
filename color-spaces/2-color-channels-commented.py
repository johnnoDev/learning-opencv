# os = operating system (sistema operativo). Para construir rutas portables.
import os

# cv2 = OpenCV (Open Source Computer Vision), aliasada como cv.
import cv2 as cv

# numpy = Numerical Python. La usamos para crear un lienzo negro (canvas)
# y para armar los canales "vacíos" al reconstruir una imagen en color.
import numpy as np

# Armamos la ruta a la imagen subiendo un nivel ('..') hasta 'Photos'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')

# imread = image read (leer imagen). Queda en BGR (Azul, Verde, Rojo).
img = cv.imread(img_path)
cv.imshow('BGR (original)', img)

# ============== ¿Qué es un "canal" (channel)? ===================
# Una imagen BGR es en realidad 3 imágenes en escala de grises apiladas:
# una que dice "cuánto Azul hay en cada píxel", otra "cuánto Verde",
# otra "cuánto Rojo". Cada una de esas 3 capas es un "canal".
# img.shape = (alto, ancho, canales). El 3er valor es la cantidad de canales.
print(f'Forma de la imagen BGR: {img.shape}')   # (alto, ancho, 3)

# ============== Separar canales: split ===================
# split = "dividir/separar". Devuelve una TUPLA con 3 imágenes de 1 solo
# canal cada una (mismo alto y ancho que la original, sin el 3er valor).
# Como la imagen es BGR, el orden de retorno es (Blue, Green, Red).
b, g, r = cv.split(img)

# Cada canal por separado se ve en escala de GRISES: el valor de cada
# píxel representa "cuánta cantidad de ese color hay ahí" (0 = nada,
# 255 = el máximo de ese color). Por eso NO se ve azul/verde/rojo,
# se ve blanco donde hay mucho de ese color y negro donde hay poco.
cv.imshow('Canal Blue (gris)', b)
cv.imshow('Canal Green (gris)', g)
cv.imshow('Canal Red (gris)', r)

# Cada canal tiene 1 solo valor de "profundidad" -> shape de 2 dimensiones.
print(f'Forma del canal Blue: {b.shape}')       # (alto, ancho)  -> sin 3er valor

# ============== Reconstruir: merge ===================
# merge = "combinar/fusionar". Es la operación inversa a split: junta
# 3 canales de 1 solo canal en una imagen BGR de 3 canales.
# El orden en el que los pases IMPORTA: acá reconstruimos en orden B,G,R
# tal cual estaba la imagen original.
merged = cv.merge([b, g, r])
cv.imshow('Reconstruida (b,g,r)', merged)

# ============== Ver un canal "en su color real" ===================
# blank = "en blanco". Un canal de 1 solo valor no puede mostrar color
# por sí solo; para verlo "en azul de verdad" hay que crear una imagen
# BGR de 3 canales donde los otros 2 canales sean CERO (apagados).
blank = np.zeros(img.shape[:2], dtype='uint8')   # lienzo negro, 1 canal

# merge([canal, cero, cero]) en orden B,G,R: solo prende el canal Blue.
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Solo canal Blue (color real)', blue)
cv.imshow('Solo canal Green (color real)', green)
cv.imshow('Solo canal Red (color real)', red)

# ============== "Apagar" un canal en la imagen completa ===================
# Otro uso típico: quedarte con la imagen original pero anulando 1 canal.
# Acá apagamos el canal Rojo (lo reemplazamos por el lienzo en blank/negro).
sin_rojo = cv.merge([b, g, blank])
cv.imshow('Imagen sin canal Red', sin_rojo)

# waitKey(0) = esperar una tecla indefinidamente para no cerrar las ventanas.
cv.waitKey(0)

# destroyAllWindows = destruir todas las ventanas abiertas por OpenCV.
cv.destroyAllWindows()
