import cv2
import numpy as np

picture = cv2.imread("hababamsinifi.jpeg")

cv2.rectangle(picture,(200,300),(350,100),[255,255,0],3)
#rectangle resimde verdiğimiz noktaları sol alt ve sağ üst kabul edip dikdörtgen oluşturur
#ilk parametre işlem yapılacak resim
#ikinci parametre sol alt köşe () içinde belirtildiği için x,y şeklinde
#3.parametre sağ üst köşe () içinde belirtildiği için x,yşeklinde
#4. parametre bu çerçevenin rengini belirtiyor bgr mantığı
#5. parametre de çerçevenin kalınlığı 0-9 arasında değişiyor

cv2.imshow("Hababam Sinifi",picture)

cv2.waitKey(0)
cv2.destroyAllWindows()