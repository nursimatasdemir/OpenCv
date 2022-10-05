import cv2
import numpy as np
 
resim = cv2.imread("Daniel-Ricciardo.jpg")
resim1 = cv2.imread("Daniel-Ricciardo.jpg",0)
#resmi grileştirdiğimizde boyutu da 3te birine düşer ve tek kanallı olur
#resmi okudu

cv2.imshow("Danny Ric",resim1)
#resmi gösterir

#print(resim)
#resmin her bir pikselinin matrissel görünümünü verir

print(resim1.size)
#resmin boyutunu çıktı verir

print(resim1.dtype)
#resmin hangi veri türünde olduğunu çıktı verir

print(resim1.shape)
#resminn genişliğini,yüksekliğini,kaç kanaldan oluştuğunu verir
#bu üçünün çarpımı size ı verir



cv2.waitKey(0)
cv2.destroyAllWindows()
