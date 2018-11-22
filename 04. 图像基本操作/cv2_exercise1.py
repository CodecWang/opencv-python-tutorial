# ex2tron's blog:
# http://ex2tron.wang

import cv2

img = cv2.imread('lena.jpg')

# 帽子ROI的红色通道
hat_r = img[25:120, 50:220, 2]
cv2.imshow('hat', hat_r)
cv2.waitKey(0)
