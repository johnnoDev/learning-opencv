# ============== Color Spaces (espacios de color) ===================

# 1. Importar os, cv2 (como cv) y matplotlib.pyplot (como plt).
import os
import cv2 as cv
import matplotlib.pyplot as plt

# 2. Armar la ruta a 'Photos/park.jpg' subiendo un nivel con '..'.
img_path = os.path.join(os.path.dirname(__file__), '..', 'Photos', 'park.jpg')

# 3. Leer la imagen con imread (queda en BGR) y mostrarla.
bgr = cv.imread(img_path)
cv.imshow('BGR', bgr)

# 4. Convertir BGR -> escala de grises y mostrarla.
#    Pista: constante que va de BGR a GRAY. Queda 1 solo canal.
gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
cv.imshow('BGR --> Gray Scale', gray)

# 5. Convertir BGR -> HSV y mostrarla.
#    HSV = Matiz, Saturación, Valor. Sirve para detectar colores.
hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
cv.imshow('BGR --> HSV', hsv)

# 6. Convertir BGR -> L*a*b (LAB) y mostrarla.
#    LAB = luminosidad + dos ejes de color, pensado para el ojo humano.
lab = cv.cvtColor(bgr, cv.COLOR_BGR2LAB)
cv.imshow('BGR --> LAB', lab)

# 7. Convertir BGR -> RGB y mostrarla.
#    Solo invierte el orden de canales.
rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
cv.imshow('BGR --> RGB', rgb)

# 8. Mostrar la imagen BGR original con plt.imshow y plt.show.
#    Observar que los colores salen mal (matplotlib espera RGB).
#    Repetir con la imagen ya convertida a RGB y comparar.
plt.imshow(bgr)
plt.title('Perspectiva mal por Matplotlib')
plt.show()

plt.imshow(rgb)
plt.title('Perspectiva Corregida (RGB)')
plt.show()

# 9. Volver atrás: HSV -> BGR y LAB -> BGR. Comprobar que se recupera.
hsv_to_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_to_bgr)

lab_to_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_to_bgr)

# 10. Intentar GRIS -> HSV directo (falla). Hacer GRIS -> BGR -> HSV.
# gray_to_hsv = cv.cvtColor(gray, cv.COLOR_GRAY2HSV) # No se puede
gray_to_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
bgr_to_hsv = cv.cvtColor(gray_to_bgr, cv.COLOR_BGR2HSV)
cv.imshow('Gray --> BGR --> HSV', bgr_to_hsv)

# 11. waitKey(0) y destroyAllWindows al final.
cv.waitKey(0)
cv.destroyAllWindows()
