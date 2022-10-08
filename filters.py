import cv2
import numpy as np

pic = cv2.imread("noise.jpg")
# pic1 = cv2.pyrUp(pic)

newPic1 = cv2.blur(pic,(7,7))
# newPic2 = cv2.blur(pic1,(3,3))

medianFilter = cv2.medianBlur(pic,7)

gaussfiltered = cv2.GaussianBlur(pic,(7,7),0)


cv2.imshow("Gürültülü resim",pic)
# cv2.imshow("Mean filtered",newPic2)
# cv2.imshow("2 kat",pic1)
cv2.imshow("Mean filtered small",newPic1)
cv2.imshow("Median filtered",medianFilter)
cv2.imshow("Gauss filtered",gaussfiltered)






cv2.waitKey(0)
cv2.destroyAllWindows()
