# os = operating system (sistema operativo). Para construir rutas portables.
import os

# cv2 = OpenCV (Open Source Computer Vision), aliasada como cv.
import cv2 as cv

# numpy = Numerical Python. La usamos para crear los lienzos negros donde
# vamos a dibujar las figuras de prueba.
import numpy as np

# ============== ¿Qué son las operaciones "bitwise"? ===================
# bitwise = "a nivel de bits". Son operaciones lógicas (AND, OR, XOR, NOT)
# que ya conocés de programación normal, pero aplicadas PÍXEL A PÍXEL entre
# dos imágenes del mismo tamaño.
# En una imagen binaria (blanco = 255 = "encendido", negro = 0 = "apagado"),
# cada operación se comporta igual que con booleanos:
#   AND -> True  si AMBOS  son blancos (intersección: lo que comparten)
#   OR  -> True  si ALGUNO es blanco   (unión: todo lo que aparece)
#   XOR -> True  si SOLO UNO es blanco (diferencia: lo que NO comparten)
#   NOT -> invierte: blanco se vuelve negro y viceversa

# Creamos 2 lienzos negros de 400x400, 1 solo canal (no hace falta color
# para esta demo). dtype='uint8' = enteros sin signo de 8 bits (0 a 255).
blank = np.zeros((400, 400), dtype='uint8')

# Dibujamos un RECTÁNGULO blanco sobre una copia del lienzo.
# rectangle(imagen, punto1, punto2, color, grosor).
# 255 = blanco (máxima intensidad en 1 canal). -1 = grosor "relleno" (fill).
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow('Rectangle', rectangle)

# Dibujamos un CÍRCULO blanco sobre otra copia del lienzo, desplazado para
# que se solape parcialmente con el rectángulo (así se nota cada operación).
# circle(imagen, centro, radio, color, grosor).
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow('Circle', circle)

# ============== bitwise_and: intersección ===================
# bitwise_and = "Y a nivel de bits". El píxel de salida es blanco SOLO si
# es blanco en AMBAS imágenes al mismo tiempo. Muestra dónde se SOLAPAN.
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND (interseccion)', bitwise_and)

# ============== bitwise_or: unión ===================
# bitwise_or = "O a nivel de bits". El píxel de salida es blanco si es
# blanco en CUALQUIERA de las dos imágenes (o en ambas). Muestra TODO lo
# que aparece en al menos una de las dos figuras.
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR (union)', bitwise_or)

# ============== bitwise_xor: diferencia simétrica ===================
# bitwise_xor = "O exclusivo a nivel de bits" (eXclusive OR).
# El píxel de salida es blanco si es blanco en UNA de las dos imágenes,
# pero NO en ambas. Es la unión MENOS la intersección: muestra lo que
# NO comparten (donde se "cruzan" desaparece).
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR (no compartido)', bitwise_xor)

# ============== bitwise_not: inversión ===================
# bitwise_not = "NO a nivel de bits". Invierte cada píxel: donde había
# blanco (255) queda negro (0), y donde había negro queda blanco.
# Solo recibe UNA imagen (no compara dos).
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT (invertido)', bitwise_not)

# ============== Uso real: recortar una FOTO con una MÁSCARA ===================
# mask = "máscara". Una máscara es una imagen binaria (blanco/negro) que
# se usa como "molde": donde la máscara es blanca, se conserva el píxel
# original de la foto; donde es negra, se descarta (queda negro).
# Es el uso más común de bitwise_and en la práctica: aislar una región
# de forma NO rectangular (algo que el slicing simple [y1:y2, x1:x2] no
# puede hacer, porque solo recorta rectángulos).
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')
img = cv.imread(img_path)
cv.imshow('Original', img)

# La máscara debe tener el mismo alto y ancho que la foto (1 solo canal).
mask_blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(mask_blank, (img.shape[1] // 2, img.shape[0] // 2), 150, 255, -1)
cv.imshow('Mask', mask)

# bitwise_and(src1, src2, mask=mask): compara la foto CONSIGO MISMA
# (src1 = src2 = img), pero el parámetro mask filtra el resultado:
# solo se conservan los píxeles donde la máscara es blanca (255).
recortado_con_mascara = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Recortado con mascara (circulo)', recortado_con_mascara)

# waitKey(0) = esperar una tecla indefinidamente para no cerrar las ventanas.
cv.waitKey(0)

# destroyAllWindows = destruir todas las ventanas abiertas por OpenCV.
cv.destroyAllWindows()
