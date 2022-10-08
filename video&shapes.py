import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret,img = cam.read()

    cv2.rectangle(img,(200,200),(20,20),(0,75,25),4)
    #cv2.rectangle kare çizmek için kullanılır
    #cv2.rectangle(görüntü,(sol alt),(sağ üst),renk(bgr),kalınlık)

    cv2.line(img,(10,10),(10,300),(0,0,85),3)

    cv2.circle(img,(150,100),50,(200,0,0),3)

    cv2.putText(img,"Nurs",(250,100),cv2.FONT_HERSHEY_TRIPLEX,4,(150,30,50),4)

    cv2.imshow("Shapes",img)

    if cv2.waitKey(20) & 0xFF == (27):
        break

cam.release()

cv2.destroyAllWindows()