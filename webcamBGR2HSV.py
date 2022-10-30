import cv2
import numpy as np

frameWidth = 360
frameHeight = 120
cap  = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

while True:
    ret,img = cap.read()

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV)
    cv2.imshow("BGR to HSV",np.hstack([img,imgHSV]))



    if cv2.waitKey(1) %0xFF == ord('q'):
        break
cv2.destroyAllWindows()



