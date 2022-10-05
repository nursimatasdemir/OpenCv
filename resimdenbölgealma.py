import cv2
import numpy as np

resim = cv2.imread("at.jpg")
print(resim.shape)


kesit = resim[100:350,300:400]
#ana resimden belirttiğimiz kısmı kesit olarak alıp kaydeder
#ilk parametre y ikinci x kordinatı

resim[200:450,100:200] = kesit
#aldığımız kesiti resmin belirli bölgesine yapıştırma
#bunu yaparken kesiti yapıştıracağın yeri girerkendikkat et kesitten daha küçük olmasın
resim[450:500,100:200] = (0,100,250)
#resmin belirlediğimiz alanına efekt vermek bgr karışık
cv2.imshow("At",resim)
cv2.imshow("Kesit",kesit)

cv2.waitKey(0)
cv2.destroyAllWindows()