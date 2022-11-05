import cv2
from cv2 import getTrackbarPos
import numpy as np
# import stackfunc as sf

framewidth = 360
frameheight = 360

cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)

def empty(a):
    pass

cv2.namedWindow("Parametres")
cv2.resizeWindow("Parametres",640,240)
cv2.createTrackbar("Threshold1","Parametres",150,255,empty)
cv2.createTrackbar("Threshold2","Parametres",255,255,empty)

def getcontours(img,imgcontour):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgcontour,contours,-1,(150,75,100),5)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3)





while True:
    succsess,img = cap.read()
    imgcontour=img.copy()
    imgblur = cv2.GaussianBlur(img,(7,7),1)
    imggray = cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)
    # imgstack = sf.stackImages(0.8,([img,imgblur,imggray]))
    threshold1 = getTrackbarPos("Threshold1","Parametres")
    threshold2 = getTrackbarPos("Threshold2","Parametres")

    imgcanny = cv2.Canny(imgblur,threshold1,threshold2)

    kernel = np.ones((5,5))
    imgdil = cv2.dilate(imgcanny,kernel,iterations=1)

    getcontours(imgdil,imgcontour)




    # cv2.imshow("Result",img)
    # cv2.imshow("Blurred",imgblur)
    cv2.imshow("Converted to gray",imgcanny)
    cv2.imshow("Contoured",imgcontour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
