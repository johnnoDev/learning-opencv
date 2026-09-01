# os = operating system (sistema operativo). Para construir rutas portables.
import os

# cv2 = OpenCV (Open Source Computer Vision), aliasada como cv.
import cv2 as cv

# matplotlib = librería de gráficos de Python. La usamos SOLO para mostrar
# cómo interpreta los colores un programa que espera RGB (y no BGR como OpenCV).
# pyplot = "plot" = graficar. Se alias como plt por convención.
import matplotlib.pyplot as plt

# ============== ¿Qué es un "color space" (espacio de color)? ===================
# Es la forma en que se representa un color con números. El mismo color se
# puede describir de varias maneras:
#   - BGR / RGB : mezcla de Azul, Verde y Rojo (Blue, Green, Red).
#   - Grayscale : un solo número de intensidad (0 negro ... 255 blanco).
#   - HSV       : Hue, Saturation, Value = Matiz, Saturación, Valor/Brillo.
#   - L*a*b     : Lightness + dos ejes de color (a: verde-rojo, b: azul-amarillo).
# OpenCV carga las imágenes en BGR (¡ojo, NO en RGB!).

# Armamos la ruta a la imagen subiendo un nivel ('..') hasta 'Photos'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')

# imread = image read (leer imagen). La deja en formato BGR.
img = cv.imread(img_path)
cv.imshow('BGR (original)', img)

# ============== BGR  ->  Escala de grises (Grayscale) ===================
# cvtColor = "convert color" = convertir color.
# COLOR_BGR2GRAY = "BGR to GRAY" = de BGR a gris.
# Resultado: 1 solo canal. Muestra la INTENSIDAD de luz, se pierde el color.
# Se usa antes de detección de bordes, contornos, umbral, etc.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# ============== BGR  ->  HSV ===================
# HSV = Hue, Saturation, Value = Matiz, Saturación, Valor(brillo).
# COLOR_BGR2HSV = "BGR to HSV".
# Muy útil para DETECTAR COLORES: el matiz (Hue) separa el "qué color es"
# del "qué tan brillante/apagado está", así un filtro de color aguanta
# mejor los cambios de iluminación.
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# ============== BGR  ->  L*a*b  (también escrito LAB) ===================
# COLOR_BGR2LAB = "BGR to LAB".
# L = Lightness (luminosidad). a = eje verde<->rojo. b = eje azul<->amarillo.
# Diseñado para que la distancia entre dos colores se parezca a cómo el
# ojo humano percibe esa diferencia. Se usa para comparar/segmentar colores.
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# ============== BGR  ->  RGB ===================
# COLOR_BGR2RGB = "BGR to RGB". Solo invierte el orden de los canales.
# OpenCV usa BGR; casi todo lo demás (matplotlib, PIL, la web) usa RGB.
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# Demostración del problema BGR vs RGB:
# matplotlib asume RGB. Si le pasamos la imagen BGR original, los colores
# salen MAL (el cielo azul se ve naranja). Con 'rgb' ya convertida, sale bien.
plt.imshow(img)          # <- se ve con los colores cambiados (BGR mal interpretado)
plt.title('BGR visto por matplotlib (mal)')
plt.show()

# ============== Volver atrás: HSV -> BGR ===================
# COLOR_HSV2BGR = "HSV to BGR". Toda conversión tiene su inversa.
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV -> BGR', hsv_bgr)

# COLOR_LAB2BGR = "LAB to BGR".
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB -> BGR', lab_bgr)

# ============== IMPORTANTE: limitación de grayscale ===================
# No se puede pasar de GRIS directo a HSV: el gris no tiene información de
# color, y cvtColor no acepta ese camino.
# Sí se puede GRIS -> BGR (queda "gris" pero con 3 canales), y de ahí a HSV.
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('GRAY -> BGR', gray_bgr)

# waitKey(0) = esperar una tecla indefinidamente para no cerrar las ventanas.
cv.waitKey(0)

# destroyAllWindows = destruir todas las ventanas abiertas por OpenCV.
cv.destroyAllWindows()
