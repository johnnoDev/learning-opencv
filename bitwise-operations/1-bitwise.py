# ============== Bitwise Operations (operaciones a nivel de bits) ===================

# 1. Importar os, cv2 (como cv) y numpy (como np).
import os
import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt

# 2. Crear un lienzo negro (blank) de 400x400, 1 solo canal, con np.zeros.
blank = np.zeros((400, 400), dtype='uint8')

# 3. Dibujar un rectángulo blanco (255) relleno sobre una copia del
#    lienzo y mostrarlo.
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), color=255, thickness=-1)
cv.imshow('Rectangle', rectangle)

# 4. Dibujar un círculo blanco (255) relleno sobre otra copia del
#    lienzo, desplazado para que se solape con el rectángulo, y mostrarlo.
circle = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 190, 255, -1)
cv.imshow('Circle', circle)

# 5. Aplicar bitwise_and entre el rectángulo y el círculo, y mostrarlo.
#    Pista: queda blanco solo donde AMBAS figuras son blancas
#    (la intersección / lo que comparten).
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise And', bitwise_and)

# 6. Aplicar bitwise_or entre el rectángulo y el círculo, y mostrarlo.
#    Pista: queda blanco donde CUALQUIERA de las dos es blanca (la unión).
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise Or', bitwise_or)

# 7. Aplicar bitwise_xor entre el rectángulo y el círculo, y mostrarlo.
#    Pista: queda blanco donde SOLO UNA de las dos es blanca
#    (lo que no comparten).
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise Xor', bitwise_xor)

# 8. Aplicar bitwise_not sobre el círculo, y mostrarlo.
#    Pista: solo recibe 1 imagen; invierte blanco y negro.
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise Not', bitwise_not)

# 9. Cargar 'Photos/park.jpg'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')
img = cv.imread(img_path)
cv.imshow('Park', img)
# 10. Crear una máscara (mask) del mismo alto/ancho que la foto, con un
#     círculo blanco relleno en el centro.
mask_blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(mask_blank, (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)


# 11. Usar bitwise_and(foto, foto, mask=mascara) para recortar solo la
#     zona circular de la foto y mostrar el resultado.

# 12. waitKey(0) y destroyAllWindows al final.
cv.waitKey(0)
cv.destroyAllWindows()