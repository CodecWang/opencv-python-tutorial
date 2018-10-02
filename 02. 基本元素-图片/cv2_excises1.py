# More: http://ex2tron.top

import cv2

img = cv2.imread('lena.jpg')
cv2.imshow('lena', img)

k = cv2.waitKey(0)
# ord用来获取某个字符的编码
if k == ord('s'):
    cv2.imwrite('lena_save.bmp', img)
