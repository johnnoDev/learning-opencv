# ============== Color Channels (canales de color) ===================

# 1. Importar os, cv2 (como cv) y numpy (como np).
import os
import cv2 as cv
import numpy as np

# 2. Armar la ruta a 'Photos/park.jpg' subiendo un nivel con '..'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')

# 3. Leer la imagen con imread (queda en BGR) y mostrarla.
img = cv.imread(img_path)
cv.imshow('Original', img)

# 4. Imprimir img.shape. Recordar qué representa el 3er valor.
print(f'Valores de img: {img.shape}') 

# 5. Separar la imagen en sus 3 canales con split.
#    Pista: devuelve una tupla en orden Blue, Green, Red.
b,g,r = cv.split(img)

# 6. Mostrar cada canal por separado.
#    Observar que se ven en gris, no en su color: cada canal es
#    intensidad de "cuánto hay de ese color", no el color en sí.
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# 7. Imprimir el shape de un solo canal y compararlo con el de la
#    imagen completa. ¿Cuántos valores tiene la tupla ahora?
print(f'Shape del canal Blue: {b.shape}')
print(f'Shape del canal Green: {g.shape}')
print(f'Shape del canal Red: {r.shape}')

# 8. Reconstruir la imagen original combinando los 3 canales con merge,
#    respetando el orden B, G, R.
merged = cv.merge([b,g,r])
cv.imshow('Image merged', merged)

# 9. Crear un lienzo en blank (negro, 1 canal, mismo alto/ancho que la
#    imagen) con np.zeros.
blank = np.zeros(img.shape[:2], dtype='uint8')

# 10. Usando merge, armar 3 imágenes de 3 canales donde solo esté
#     "encendido" un canal por vez (los otros dos = blank) para ver
#     cada canal en su color real (azul de verdad, verde de verdad,
#     rojo de verdad).
blue = cv.merge([b, blank, blank])
cv.imshow('Image Blue', blue)

green = cv.merge([blank, g, blank])
cv.imshow('Image Green', green)

red = cv.merge([blank, blank, r])
cv.imshow('Image Red', red)

# 11. Reconstruir la imagen original pero "apagando" el canal Red
#     (reemplazándolo por blank) y mostrar el resultado.
img = cv.merge([b,g,blank])
cv.imshow('Image OFF RED', img)


# 12. waitKey(0) y destroyAllWindows al final.
cv.waitKey(0)
cv.destroyAllWindows()