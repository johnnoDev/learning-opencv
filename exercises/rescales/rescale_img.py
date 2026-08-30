import os
import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img_path = os.path.join(os.path.dirname(__file__), '../..', 'Photos', 'cats.jpg')

img = cv.imread(img_path)

img_resized = rescaleFrame(img)

cv.imshow('Cat Resized', img_resized)

cv.waitKey(0)