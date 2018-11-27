# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

img = cv2.imread('chessboard.png')
imgShi, imgHarris = np.copy(img), np.copy(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1.Shi-Tomasi角点检测
# 优点：
# 速度相比Harris有所提升，可以直接得到角点坐标
corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 10)
corners = np.int0(corners)  # 12个角点坐标

for i in corners:
    x, y = i.ravel()
    cv2.circle(imgShi, (x, y), 4, (0, 0, 255), -1)


# 2. Harris角点检测
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
imgHarris[dst > 0.001 * dst.max()] = [255, 0, 0]

cv2.imshow('compare', np.hstack((imgHarris, imgShi)))
cv2.waitKey()
