import os
import cv2 as cv
import numpy as np

img_path = os.path.join(os.path.dirname(__file__), '../..', 'Photos', 'park.jpg')

img = cv.imread(img_path)
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
# Respuesta: Observo que existen más tonalidad del canal Rojo

merged = cv.merge([b,g,r])
print(f'1. ¿Es igual?: {"Si" if np.array_equal(img, merged) else "No"}')

merged_2 = cv.merge([r,g,b])
print(f'2. ¿Es igual?: {"Si" if np.array_equal(img, merged_2) else "No"}')

# 4. Armá solo_azul, solo_verde, solo_rojo (con blank en los otros 2 canales) y mostralos junto a b, g, r "crudos". Explicá con tus palabras la diferencia entre ver un canal en gris y verlo "en su color real".
blank = np.zeros(img.shape[:2], dtype='uint8')
only_blue = cv.merge([b, blank, blank])
only_green = cv.merge([blank, g, blank])
only_red = cv.merge([blank, blank, r])
cv.imshow('Only Blue', only_blue)
cv.imshow('Only Green', only_green)
cv.imshow('Only Red', only_red)



# 5. Apagá 2 canales a la vez (dejá solo uno encendido combinando con dos blank) contra apagar 1 canal (dejar 2 encendidos, como el ejemplo sin_rojo). ¿Cuál da una imagen más parecida a la original?

other = cv.merge([b,blank, blank])
not_red = cv.merge([b,g,blank])
cv.imshow('Two channels is OFF', other)
cv.imshow('Not Red in Image', not_red)

# Respuesta: La que tiene más canales encendidos tiene más 'similitud' a la original.

# 6. cv.split es cómodo pero un poco lento porque copia memoria. Investigá y probá indexar directo con NumPy: b = img[:, :, 0]. Compará el resultado contra cv.split(img)[0] con np.array_equal.
blue = img[:, :, 0]
cv.imshow('Blue with numpy', blue)

cv.waitKey(0)
cv.destroyAllWindows()