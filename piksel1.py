import cv2
import numpy as np

atResmi = cv2.imread("at.jpg")

cv2.imshow("At Resmi",atResmi)

print(atResmi[(230,80)])
#resmin sağdan ve soldan yerini belirlediğimiz pikselini görmek için
#resmin sol köşesi baz alınarak aşağı 230 sağa doğru 80 piksel gidildiğinde ulaşılan pikselin BGR değerleini yazdırır

print("Resmin Boyutu: "+str(atResmi.size))
print("Resmin özellikleri: "+str(atResmi.shape))
print("Resmin veri tipi: "+str(atResmi.dtype))



cv2.waitKey(0)
cv2.destroyAllWindows()