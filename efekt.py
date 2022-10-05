import cv2
import numpy as np

resim = cv2.imread("jinx.jpg")
# resim[:,:,0] = 255 #resme mavi efekt verir bgr 0 mavi
# resim[:,:,1] = 255 #resme yeşil efekt verir
# resim[:,:,2] = 255 #resme kırmızı efekt verir
#değerler 0-255 arasında değişebilir

resim[110:150,335:475,0] = 255
#ilk parametre y parametresi 110-150 arası,ikinci parametre x parametresi 335-475 arası
cv2.imshow("Jinx",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

