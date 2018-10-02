# More: http://ex2tron.top

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('drawing.jpg')

# 1.按照指定的宽度、高度缩放图片
res = cv2.resize(img, (132, 150))
# 按照比例缩放，如x,y轴均放大一倍
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('shrink', res), cv2.imshow('zoom', res2)
cv2.waitKey(0)


# 2.平移图片
rows, cols = img.shape[:2]
# 定义平移矩阵，需要是numpy的float32类型
# x轴平移100，y轴平移50
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('shift', dst)
cv2.waitKey(0)


# 3.45°旋转图片并缩小一半
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotation', dst)
cv2.waitKey(0)


# 4.翻转图片
# 参数2=0：垂直翻转(沿x轴)，参数2>0: 水平翻转(沿y轴)
# 参数2<0: 水平垂直翻转
dst = cv2.flip(img, 1)
# np.hstack: 横向并排，对比显示
cv2.imshow('flip', np.hstack((img, dst)))  # np.hstack: 横向并排，对比显示
cv2.waitKey(0)


# 5.仿射变换
# 变换前的三个点
pts1 = np.float32([[50, 65], [150, 65], [210, 210]])
# 变换后的三个点
pts2 = np.float32([[50, 100], [150, 65], [100, 250]])

# 生成变换矩阵，维数：2*3
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('input')
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.show()
