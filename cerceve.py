import cv2
import numpy as np

resim = cv2.imread("joker.jpg")

sarilanResim = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT ,value=(75,150,255))
#copymakeborder yeni sısnırlar
#borderconstant çerçeve oluşturmak için
#value de de çerçevenin rengini oluşturduk bgr de 


cv2.imshow("Cercevelenen Resim",sarilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows()
