import cv2
import numpy as np

# 1. Crear el lienzo negro de 500x500
lienzo = np.zeros((500, 500, 3), dtype='uint8')

# 2. Definir los límites del recorte (slicing)
inicio_y, fin_y = 200, 300
inicio_x, fin_x = 300, 400

print("Iniciando animación... presiona 'q' en la ventana para salir antes de tiempo.")

# 3. Animación: Colorear fila por fila (Eje Y) de arriba hacia abajo
for y in range(inicio_y, fin_y):
    # En la fila 'y' actual, coloreamos la sección del Eje X de rojo (BGR)
    lienzo[y, inicio_x:fin_x] = (0, 0, 255) 
    
    # Mostrar el lienzo actualizado
    cv2.imshow('Animacion Slicing', lienzo)
    
    # Pausar 50 milisegundos para crear el efecto de animación
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Mantener la ventana abierta al terminar hasta que presiones cualquier tecla
cv2.waitKey(0)
cv2.destroyAllWindows()