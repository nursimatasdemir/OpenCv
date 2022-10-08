import cv2
import numpy as np

img = np.zeros((200,200,3),dtype="uint8")
#bir satırdaki piksellerin matrislerini yazdırmamızı sağlar
#bir görüntü değil boş bir yapı oluşturduğumuz için 0 çıktısı alırız her matriste
#parametreler ((boyutlar,kanal),dtype)
#uint8 -> 0-255 arasında bgr değerleri kullanacağımız için

print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()











