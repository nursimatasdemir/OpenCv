import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    success,image = camera.read()

    cv2.imshow("Camera",image)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()