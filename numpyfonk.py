import cv2
import numpy as np

img = np.zeros((400,400,3),dtype = "uint8")


#             x,y
cv2.line(img,(0,0),(100,100),(150,25,60),4)
#cv2.line çizgi oluşturmak için kullanırız
#cv2.line(işlem yapılacak resim,çizgi nereden başlasın(sol üst köşenin kordinatları),nerede bitsin(kordiinatları),renk,kalınlık)
#renk için bgr değerleri girilir
#kalınlık 0-9 arası

cv2.circle(img,(175,175),20,(150,25,60),4)
#cv2.line daire oluşturmak için kullanılır
#cv2.line(resim,dairenin merkezi(x,y),yarıFONT_HERSHEY_SIMPLEXıçap,rengi(bgr),kalınlık)

cv2.putText(img,"Deneme",(80,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),4)
#cv2.putText resmin içine text koymak için kullanılır
#cv2.putText(resim,"Text",(textin başlayacağı piksel),font,yazının boyutu,yazınıın rengi(bgr),kalınlık)
#cv2.FONT_HERSHEY_COMPLEX font 


cv2.imshow("Deneme",img)

cv2.waitKey(0)
cv2.destroyAllWindows()















