import cv2
import numpy as np

resim = cv2.imread("Daniel-Ricciardo (1).jpg",0)
#yazdığımız reim adını numpy arrayine dönüştürüyor,2.parametre olarak 0 verirsek resmi grileştirir renkleri kullanmaz
#grileştirirsek tek kanala indirmiş oluruz

cv2.imshow("Daniel Ricciardo",resim)
#resim açıldığında sol üstte yazacak yazıyı ilk parametreye,hangi resmi göstereceğini de 2.parametreye

cv2.imwrite("Daniel Ricciardo(grey).jpg",resim)
#grileştirdiğimiz resmi yeni bir resim olarak kaydetmemizi sağlar
#yeniresmin adı ilk parametre,2.parametre resmi nerden aldığımız


cv2.waitKey(0)
#temel iskelette kapanışta kullanıyoruz pencereyi kapatmamız için herhangi bir tuşa basılmasını bekler

cv2.destroyAllWindows()
#temel iskelette x ya bastığımızda opencvye bağlı tüm pencereleri kapatır
