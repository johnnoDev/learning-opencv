import os
import cv2 as cv

video_path = os.path.join(os.path.dirname(__file__), '..', 'videos', 'kitten.mp4')
capture = cv.VideoCapture(video_path)

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()

cv.destroyAllWindows()