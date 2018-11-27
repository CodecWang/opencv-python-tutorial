# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

img = cv2.imread('chessboard.png')

# 1. Harris角点检测基于灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Harris角点检测
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
# 腐蚀一下，便于标记
dst = cv2.dilate(dst, None)
# 3. 角点标记为红色
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)
cv2.waitKey()
