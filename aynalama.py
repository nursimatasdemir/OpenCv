import cv2
import numpy as np

resim = cv2.imread("joker.jpg")
aynalananResim = cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)
#copyMakeBorder resme yeni sınırlar oluştururken kullanılır
#ilk parametre işlem yapılacak resim
#üst alt sol sağ parametreleri sonraki 4
#border reflect sınırları tekrarlar aynalama işlemi yaparken istediğimiz de bu


cv2.imshow("Aynalama Joker",aynalananResim)

cv2.waitKey(0)
cv2.destroyAllWindows()