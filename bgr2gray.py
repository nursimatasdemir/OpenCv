import cv2
import numpy as np

pic = cv2.imread("DanielRicciardo.jpg")
#resmi tanımlarken 2.parametre olarak 0 vermek de resmi grileştirir

graypic = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
#cvtColor -> convertcolor resmin rengini dönüştürme
#cv2.COLOR_BGR2GRAY  bgr -> gray

hight, width, channel = pic.shape
hight1, width1 = graypic.shape
#gri resmin kanal sayısı 1 olduğu için shape te sadece hight ve width tutar
#kanalını yazdırmaya çalışmak hata verir

print("Original",hight,width,channel)
print("Graypic",hight1,width1)

cv2.imshow("DannyRic",pic)
cv2.imshow("GrayDannyRic",graypic)

cv2.waitKey(0)
cv2.destroyAllWindows()