import os
import cv2 as cv
import numpy as np

# 9. Video en vivo/archivo: leé Videos/dog.mp4 y mostrá cada frame con cv.medianBlur(frame, 5) aplicado, simulando limpieza de ruido en tiempo real.
capture_path = os.path.join(os.path.dirname(__file__), '../..', 'Videos', 'dog.mp4')

capture = cv.VideoCapture(capture_path)

while True:
    isTrue, frame = capture.read()
    median = cv.medianBlur(frame, 5)
    cv.imshow('Video', median)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()