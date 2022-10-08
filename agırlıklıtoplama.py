import cv2
import numpy as np

pic1 = cv2.imread("ironman.jpg")
pic2 = cv2.imread("blackpanther.jpg")

print(pic1[50,30])
print(pic2[100,50])
#kordinatlar y,x sıralaması ile

cv2.imshow("IronMan",pic1)
cv2.imshow("BalckPanther",pic2)

print(pic1[50,30]+pic2[100,50])#
#ağırlıklı toplama işlemi




cv2.waitKey(0)
cv2.destroyAllWindows()