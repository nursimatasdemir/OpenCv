import cv2
import numpy as np

resim = cv2.imread("joker.jpg")

uzatilanResim = cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
#copymakeborder resme yeni sınırlar oluştururken kullandık
#ilk parametre işlem yapacağımız resim
#üst alt sol sağ değerleri sonraki 4 parametre
#border replicate sınırları tekrarlıyor uzatırken kullanıyoruz

cv2.imshow("Uzatılan Joker",uzatilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows()
