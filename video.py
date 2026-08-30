# Importamos la biblioteca OpenCV.
# cv2 = OpenCV, y lo aliasamos como cv para escribir menos.
import cv2 as cv

# Creamos un objeto de captura para leer un video desde la ruta indicada.
# VideoCapture = capturar video.
# './Videos/dog.mp4' es la ubicación del archivo de video.
capture = cv.VideoCapture('./Videos/dog.mp4')

# Iniciamos un bucle infinito para leer y mostrar cada frame del video.
while True:
    # read() devuelve dos valores:
    # isTrue = indica si se leyó correctamente un frame.
    # frame = la imagen actual del video (cada cuadro).
    isTrue, frame = capture.read()

    # Mostramos el frame actual en una ventana.
    # imshow = image show (mostrar imagen).
    cv.imshow('Video', frame)

    # Esperamos 20 milisegundos para cada frame.
    # waitKey = esperar tecla.
    # Si se presiona la tecla 'd', salimos del bucle.
    # 0xFF == ord('d') compara la tecla presionada con la letra d.
    # 0xFF es una máscara que extrae solo los últimos 8 bits (donde está el código de la tecla).
    # ord() es una función de Python que convierte un carácter (letra) a su código ASCII (número).
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Liberamos la cámara o archivo de video después de terminar.
# release = liberar.
capture.release()

# Cerramos todas las ventanas abiertas por OpenCV.
# destroyAllWindows = destruir todas las ventanas.
cv.destroyAllWindows()