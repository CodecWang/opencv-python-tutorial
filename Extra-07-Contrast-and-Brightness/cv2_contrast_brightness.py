import cv2
import numpy as np

img = cv2.imread('lena.jpg')
# numpy默认是取模运算，250+10 = 260%256 = 4
# 所以此处需要用np.clip进行范围限定，
# a<0 => a=0, a>255 => a=255
res = np.uint8(np.clip((1.5 * img + 10), 0, 255))

# 两张图片横向合并（便于对比显示）
tmp = np.hstack((img, res))
cv2.imshow('image', tmp)
cv2.waitKey(0)
