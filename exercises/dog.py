import os
import cv2 as cv

capture_path = os.path.join(os.path.dirname(__file__), '..', 'Videos','dog.mp4') 

capture = cv.VideoCapture(capture_path)

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()

cv.destroyAllWindows()