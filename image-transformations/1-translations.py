# os = operating system (sistema operativo).
# Lo usamos para construir rutas de archivos que funcionen en cualquier SO.
import os

# cv2 = OpenCV (Open Source Computer Vision), la aliasamos como cv.
import cv2 as cv

# numpy = Numerical Python. Nos da los arreglos (arrays) con los que
# se representan las imágenes y con los que armamos la matriz de traslación.
import numpy as np

# os.path.dirname(__file__) = carpeta donde vive ESTE archivo.
# '..' = subir un nivel (salir de 'image-transformations').
# os.path.join une todo con el separador correcto ('\' en Windows, '/' en Linux).
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')

# imread = image read (leer imagen). Carga la imagen del disco a una matriz BGR.
img = cv.imread(img_path)

# imshow = image show (mostrar imagen). Abre una ventana 'Original' con la imagen.
cv.imshow('Original', img)

# ============== Traslación ===================
# Trasladar = mover la imagen en los ejes X (horizontal) e Y (vertical),
# sin deformarla. Los píxeles que quedan fuera del marco se pierden y el
# hueco que dejan se rellena con negro.
def translate(img, x, y):
    # transMat = translation matrix (matriz de traslación).
    # np.float32 la crea con decimales de 32 bits, que es lo que exige warpAffine.
    #
    # Es una matriz afín 2x3. warpAffine calcula la nueva posición de CADA píxel:
    #   x' = 1*x + 0*y + x   ->  x' = x + x   (corre en horizontal)
    #   y' = 0*x + 1*y + y   ->  y' = y + y   (corre en vertical)
    #
    # La sub-matriz [[1,0],[0,1]] es la identidad ("no hagas nada"): no escala
    # ni inclina. La tercera columna (x, y) es la que produce el desplazamiento.
    transMat = np.float32([[1,0,x],
                           [0,1,y]])

    # dimensions = tamaño de salida como tupla (ancho, alto).
    # img.shape es (alto, ancho, canales); por eso [1] = ancho y [0] = alto.
    # OpenCV pide (ancho, alto), al revés de shape: cuidado con ese orden.
    dimensions = (img.shape[1], img.shape[0])

    # warpAffine = "warp affine" = deformar de forma afín.
    # Aplica transMat a la imagen y devuelve la imagen ya trasladada.
    return cv.warpAffine(img, transMat, dimensions)

# x negativo -> izquierda | x positivo -> derecha
# y negativo -> arriba    | y positivo -> abajo

# Movemos la imagen 100 px a la derecha y 100 px hacia abajo.
translated = translate(img, 100, 100)

# Mostramos el resultado en otra ventana.
cv.imshow('Image Translated', translated)

# waitKey(0) = esperar tecla, 0 = indefinidamente.
# Mantiene las ventanas abiertas hasta que se presione cualquier tecla.
cv.waitKey(0)
