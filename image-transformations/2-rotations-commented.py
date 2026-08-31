# os = operating system (sistema operativo). Para construir rutas portables.
import os

# cv2 = OpenCV (Open Source Computer Vision), aliasada como cv.
import cv2 as cv

# Armamos la ruta a la imagen subiendo un nivel ('..') hasta 'Photos'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')

# imread = image read (leer imagen).
img = cv.imread(img_path)

# imshow = image show (mostrar imagen).
cv.imshow('Original', img)

# ============== Rotación ===================
# Rotar = girar la imagen un ángulo alrededor de un punto de pivote
# (rotPoint). Como la imagen sigue siendo un rectángulo, al girarla
# aparecen triángulos negros en las esquinas (píxeles "vacíos").
def rotate(img, angle, rotPoint=None):
    # img.shape = (alto, ancho, canales). Tomamos solo alto y ancho con [:2].
    (height, width) = img.shape[:2]

    # rotPoint = rotation point (punto de pivote / eje de giro).
    # Si no se especifica, giramos alrededor del centro de la imagen.
    # '//' es división entera: width // 2 = mitad del ancho sin decimales.
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # getRotationMatrix2D = "get rotation matrix 2D"
    #   = obtener la matriz de rotación en 2 dimensiones.
    # Recibe 3 argumentos:
    #   1) rotPoint : punto alrededor del cual se gira.
    #   2) angle    : ángulo en grados. Positivo = sentido antihorario en OpenCV.
    #   3) 1.0      : scale (escala). 1.0 = mismo tamaño; 0.5 = gira y achica.
    # Devuelve una matriz afín 2x3, igual que la de traslación:
    #   [ cos  -sin   tx ]
    #   [ sin   cos   ty ]
    # (tx, ty se calculan solos para que el giro quede centrado en rotPoint)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    # dimensions = tamaño de salida (ancho, alto). OpenCV lo pide en ese orden.
    dimensions = (width, height)

    # warpAffine = "warp affine" = deformar de forma afín.
    # Aplica rotMat a cada píxel y devuelve la imagen girada.
    return cv.warpAffine(img, rotMat, dimensions)

# angle positivo -> antihorario | angle negativo -> horario
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# OJO: rotar una imagen YA rotada recorta todavía más las esquinas,
# porque el segundo giro trabaja sobre el rectángulo con zonas negras.
# rotate(img, 90) NO es igual a rotate(rotate(img, 45), 45).
rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)

# ============== Rotación exacta sin recorte ===================
# Para 90 / 180 / 270 grados exactos conviene cv.rotate: NO usa warpAffine,
# solo reordena filas y columnas, así que no pierde ni un píxel.
# ROTATE_90_CLOCKWISE = rotar 90 grados en sentido horario ("clockwise").
rotated_90 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imshow('Rotated 90 (cv.rotate)', rotated_90)

# waitKey(0) = esperar una tecla indefinidamente para no cerrar las ventanas.
cv.waitKey(0)
