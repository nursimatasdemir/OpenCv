import cv2
import numpy as np


frameWidth = 360
frameHeight = 360
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)


while True:
    timer= cv2.getTickCount()
    success, img = cap.read()

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),3)
    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


