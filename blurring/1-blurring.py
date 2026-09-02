# ============== Blurring (desenfoque / suavizado) ===================

# 1. Importar os y cv2 (como cv).
import os
import cv2 as cv

# 2. Armar la ruta a 'Photos/park.jpg' subiendo un nivel con '..'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')
# 3. Leer la imagen con imread y mostrarla.
img = cv.imread(img_path)
# cv.imshow('Park', img)

# 4. Aplicar Average Blur con un kernel de 7x7 y mostrarlo.
#    Pista: promedia todos los píxeles dentro del kernel, mismo peso.
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# 5. Aplicar Gaussian Blur con kernel 7x7 y sigmaX en 0, y mostrarlo.
#    Pista: le da más peso a los píxeles cercanos al centro del kernel.
gaussian_blur = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Image gaussian blur', gaussian_blur)

# 6. Aplicar Median Blur con kernel 7, y mostrarlo.
#    Pista: usa la mediana en vez del promedio; el kernel es un solo
#    número, no una tupla.
median = cv.medianBlur(img, 7)
cv.imshow('Median', median)

# 7. Aplicar Bilateral Blur (d=10, sigmaColor=35, sigmaSpace=25) y mostrarlo.
#    Pista: es el único que intenta conservar los bordes nítidos.
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

# 8. Comparar las 4 ventanas resultantes. Anotar cuál conserva mejor
#    los bordes y cuál desenfoca más "parejo".

# 9. waitKey(0) y destroyAllWindows al final.
cv.waitKey(0)
cv.destroyAllWindows()