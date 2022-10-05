import cv2
import numpy as np


resim = cv2.imread("joker.jpg")

tekrarlananResim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
#copymakeborder resme yeni sınırlar eklerken
#ilk parametre işlem yapacağımız resim
#üst alt sağ sol sonraki 4 parametre
#border wrap (paketlemek) verdiğimiz sınırları paketleyip tekrar etmek

cv2.imshow("Tekrarlanan Joker",tekrarlananResim)

cv2.waitKey(0)
cv2.destroyAllWindows()