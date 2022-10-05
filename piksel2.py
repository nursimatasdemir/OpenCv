import cv2
import numpy as np

resim = cv2.imread("at.jpg")

resim[50,30] = [255,255,255]
#resmin sol üst köşesinden 50 aşağı 50 sağdaki pikseli ynei bir bgr değerine eşitleme
#pikselin rengini değiştirme


for i in range(100):
    resim[70,i] = [255,255,255]
    resim[i,70] = [255,255,255]
#for dögüsünü kullanarak bir çizgi çektik


cv2.imshow("At",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()



