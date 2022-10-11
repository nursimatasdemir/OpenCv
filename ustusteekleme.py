import numpy as np
import cv2
import numpy as np

pic1 = cv2.imread("ironman.jpg")
pic2 = cv2.imread("blackpanther.jpg")

newpic = cv2.add(pic1,pic2)

cv2.imshow("IronMan",pic1)
cv2.imshow("BlackPanther",pic2)


cv2.imshow("NewPic",newpic)
#iki resmi üst üste ekleme fonksiyonu
#iki resmin aynı boyutta olması şart

newpic2 = cv2.addWeighted(pic1,0.6,pic2,0.4,0)
#addWeighted apırlıklı toplama yapıyor resimleri verdiğimiz oranda birbiri üzerine ekler
#2 resmin aynı boyutta olması şart

cv2.imshow("Newpic2",newpic2)


cv2.waitKey(0)
cv2.destroyAllWindows()