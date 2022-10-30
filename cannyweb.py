import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    def autoCanny(blur,sigma=0.05):
       median = np.median(blur)
       lower=int(max(0,(1.0 - sigma)*median))
       upper=int(min(255,(1.0 + sigma)*median))
       canny = cv2.Canny(blur,lower,upper)
       return canny
    wide = cv2.Canny(blur,20,250)
    tight = cv2.Canny(blur,100,150)
    auto = autoCanny(blur)

    # cv2.imshow("blurred image",blur)
    cv2.imshow("canny edges",np.hstack([auto,blur]))
    # cv2.imshow("autocanny",auto)     
    # cv2.imshow("original",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

  
   