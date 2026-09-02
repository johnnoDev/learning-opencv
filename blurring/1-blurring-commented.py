# os = operating system (sistema operativo). Para construir rutas portables.
import os

# cv2 = OpenCV (Open Source Computer Vision), aliasada como cv.
import cv2 as cv

# Armamos la ruta a la imagen subiendo un nivel ('..') hasta 'Photos'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')

# imread = image read (leer imagen).
img = cv.imread(img_path)
cv.imshow('Original', img)

# ============== ¿Qué es "blurring" (desenfoque/suavizado)? ===================
# Suavizar una imagen significa recalcular cada píxel como una MEZCLA de los
# píxeles que tiene alrededor (sus "vecinos"), en vez de dejarlo como está.
# El resultado es que los detalles finos y el ruido (granulado) se atenúan,
# y los bordes se vuelven más difusos.
#
# Todas las técnicas de blur usan un "kernel" (o "ventana"): un cuadradito
# que se desliza por toda la imagen, píxel por píxel, y en cada posición
# calcula el nuevo valor del píxel central en base a lo que hay dentro
# del cuadradito. El tamaño del kernel SIEMPRE debe ser impar (3x3, 5x5,
# 7x7...) para que exista un píxel central exacto.

# ============== 1) Average Blur (desenfoque por promedio) ===================
# blur = "desenfoque". Es la técnica más simple: el nuevo valor del píxel
# central es el PROMEDIO aritmético de todos los píxeles dentro del kernel.
# Argumentos: (imagen, tamaño_del_kernel).
# (7, 7) = kernel de 7x7 = promedia 49 píxeles para cada píxel de salida.
# Cuanto más grande el kernel, más "borroneada" queda la imagen.
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# ============== 2) Gaussian Blur (desenfoque gaussiano) ===================
# GaussianBlur = desenfoque "gaussiano", nombrado por la campana de Gauss
# (distribución normal). A diferencia del promedio simple, NO le da el
# mismo peso a todos los vecinos: los píxeles más CERCANOS al centro pesan
# más, y los más lejanos pesan menos. Resultado: un desenfoque más natural,
# con menos "artefactos" que el promedio plano.
# Argumentos:
#   1) img       : imagen de entrada.
#   2) (7, 7)    : tamaño del kernel (impar).
#   3) sigmaX    : desviación estándar en X. 0 = que OpenCV la calcule sola
#                  en base al tamaño del kernel.
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gauss)

# ============== 3) Median Blur (desenfoque por mediana) ===================
# median = "mediana" (el valor del MEDIO al ordenar una lista de números).
# En vez de promediar, ORDENA los valores de todos los píxeles del kernel
# y se queda con el que está justo en el medio. Es muy efectivo contra el
# ruido "sal y pimienta" (puntitos blancos/negros sueltos) porque un valor
# extremo aislado no afecta a la mediana como sí afecta a un promedio.
# Argumentos: (imagen, tamaño_del_kernel) -> acá el kernel es UN SOLO número
# (no una tupla), porque medianBlur solo admite kernels cuadrados.
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# ============== 4) Bilateral Blur (desenfoque bilateral) ===================
# bilateral = "de dos lados/criterios". Es el más sofisticado: suaviza la
# imagen PERO intenta conservar los bordes nítidos. Para eso, no solo mira
# qué tan CERCA está un vecino en distancia (como el gaussiano), sino
# también qué tan PARECIDO es su color/intensidad. Si un vecino tiene un
# color muy distinto (probable borde real), pesa poco y no se mezcla.
# Argumentos:
#   1) img          : imagen de entrada.
#   2) d = 10        : diámetro del vecindario de píxeles a considerar.
#   3) sigmaColor=35 : cuánta diferencia de color se tolera al mezclar.
#                      Más alto = colores más distintos se siguen mezclando.
#   4) sigmaSpace=25 : cuánta distancia espacial se tolera al mezclar.
#                      Más alto = píxeles más lejanos influyen más.
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

# waitKey(0) = esperar una tecla indefinidamente para no cerrar las ventanas.
cv.waitKey(0)

# destroyAllWindows = destruir todas las ventanas abiertas por OpenCV.
cv.destroyAllWindows()
