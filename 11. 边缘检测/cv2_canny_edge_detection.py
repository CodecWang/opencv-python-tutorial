# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

# 1.Canny边缘检测
img = cv2.imread('handwriting.jpg', 0)
edges = cv2.Canny(img, 30, 70)

cv2.imshow('canny', np.hstack((img, edges)))
cv2.waitKey(0)


# 2.先阈值，后边缘检测
# 阈值分割（使用到了番外篇讲到的Otsu自动阈值）
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30, 70)

cv2.imshow('canny', np.hstack((img, thresh, edges)))
cv2.waitKey(0)
