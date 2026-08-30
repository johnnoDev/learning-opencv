# import os
import cv2 as cv
import numpy as np

# img_path = os.path.join(os.path.dirname(__file__), 'Photos', 'cat.jpg')
# img = cv.imread(img_path)
# cv.imshow('Cat', img)

canva = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Canvas Black', canva)

# canva[:] = 0, 255, 0
# cv.imshow('Canvas Green', canva)

# Eje Y (Altura - Horizontal) & Eje X (Ancho - Vertical)
# canva[200:300, 300:400] = 0, 0, 255 # BGR
# cv.imshow('Canva updated', canva)

# rectangle = cv.rectangle(canva, (0,0), (250, 250), (0,0,255), thickness=2)

# cv.rectangle(canva, (0,0), (250, 500), (0,255,0), thickness=-1)

# cv.imshow('Rectangle', canva)

# Draw other rectangle

# cv.rectangle(canva, (0,0), (canva.shape[1]//2, canva.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Other Rectangle', canva)


# # 3. Draw a circle
# cv.circle(canva, (canva.shape[1]//2, canva.shape[0]//2), 50, (0,0,255), thickness=-1)
# cv.imshow('Circle', canva)

# # 4. Draw a Line
# cv.line(canva, (0,0), (canva.shape[1]//2, canva.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('Line in windows', canva)

# 5. Draw Text

cv.putText(canva, 'Hola', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow('Text', canva)


cv.waitKey(0)