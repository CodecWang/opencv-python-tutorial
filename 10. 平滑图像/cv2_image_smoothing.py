# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

img = cv2.imread('lena.jpg')
# 1.均值滤波
blur = cv2.blur(img, (3, 3))

# 上面的均值滤波也可以用方框滤波实现：normalize=True
# blur = cv2.boxFilter(img, -1, (3, 3), normalize=True)


# 2.高斯滤波
gau_blur = cv2.GaussianBlur(img, (3, 3), 0)

# 三张图片横向叠加对比显示
res = np.hstack((img, blur, gau_blur))
cv2.imshow('res', res)
cv2.waitKey(0)

# 均值滤波vs高斯滤波
img = cv2.imread('gaussian_noise.bmp')
blur = cv2.blur(img, (5, 5))  # 均值滤波
gaussian = cv2.GaussianBlur(img, (5, 5), 1)  # 高斯滤波

res = np.hstack((img, blur, gaussian))
cv2.imshow('gaussian vs average', res)
cv2.waitKey(0)


# 3.均值滤波vs中值滤波
img = cv2.imread('salt_noise.bmp', 0)

blur = cv2.blur(img, (5, 5))  # 均值滤波
median = cv2.medianBlur(img, 5)  # 中值滤波

res = np.hstack((img, blur, median))
cv2.imshow('median vs average', res)
cv2.waitKey(0)


# 4.双边滤波vs高斯滤波
img = cv2.imread('lena.jpg', 0)
gau = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯滤波
blur = cv2.bilateralFilter(img, 5, 75, 75)  # 双边滤波

res = np.hstack((img, gau, blur))
cv2.imshow('res', res)
cv2.waitKey(0)
