import cv2
import numpy as np

pic = cv2.imread("ironman.jpg")
pic2 = cv2.pyrUp(pic)
pic3 = cv2.pyrDown(pic)


print("Orijinal resim ",pic.shape)
print("2 kat ",pic2.shape)
print("' kat kucuk ",pic3.shape)

cv2.imshow("IronMan",pic)
cv2.imshow("2 kat buyutulmus",pic2)
cv2.imshow("2 kat kucultulmus ",pic3)

cv2.waitKey(0)
cv2.destroyAllWindows()