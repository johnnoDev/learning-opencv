import os
import cv2 as cv
from cv2.typing import MatLike

# TODO -- Images Resized
def rescaleFrame(frame: MatLike, scale=0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    # cv.resize() recibe 3 argumentos principales:
    # 1) frame: la imagen o frame original que queremos redimensionar.
    # 2) dimensions: una tupla (width, height) con el nuevo tamaño.
    # 3) interpolation: la técnica usada para calcular los nuevos píxeles.
    # cv.INTER_AREA se usa normalmente para reducir imágenes, porque hace
    # una mejor mezcla de píxeles y evita que se vean muy pixeladas.
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img_path = os.path.join(os.path.dirname(__file__), 'Photos', 'cat.jpg')

img = cv.imread(img_path)

img_resized = rescaleFrame(img, scale=0.3)

cv.imshow('Cat', img_resized)

cv.waitKey(0)



# TODO -- Videos Resized

# capture = cv.VideoCapture('./Videos/dog.mp4')

# # Iniciamos un bucle infinito para leer y mostrar cada frame del video.
# while True:
#     # read() devuelve dos valores:
#     # isTrue = indica si se leyó correctamente un frame.
#     # frame = la imagen actual del video (cada cuadro).
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)
#     # Mostramos el frame actual en una ventana.
#     # imshow = image show (mostrar imagen).
#     cv.imshow('Video', frame)
#     cv.imshow('Video_resized', frame_resized)

#     # Esperamos 20 milisegundos para cada frame.
#     # waitKey = esperar tecla.
#     # Si se presiona la tecla 'd', salimos del bucle.
#     # 0xFF == ord('d') compara la tecla presionada con la letra d.
#     # 0xFF es una máscara que extrae solo los últimos 8 bits (donde está el código de la tecla).
#     # ord() es una función de Python que convierte un carácter (letra) a su código ASCII (número).
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# # Liberamos la cámara o archivo de video después de terminar.
# # release = liberar.
# capture.release()

# # Cerramos todas las ventanas abiertas por OpenCV.
# # destroyAllWindows = destruir todas las ventanas.
# cv.destroyAllWindows()


