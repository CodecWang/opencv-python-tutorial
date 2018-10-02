# More: http://ex2tron.top

import cv2

img = cv2.imread('lena.jpg')

# 1.获取像素的值
px = img[100, 100]
print(px)  # [119 108 201]

# 只获取蓝色blue通道的值
px_blue = img[100, 100, 0]
print(px_blue)  # 119


# 2.修改像素的值
img[100, 100] = [255, 255, 255]
print(img[100, 100])  # [255 255 255]


# 3.图片形状
print(img.shape)  # (263, 263, 3)
# 形状中包括高度、宽度和通道数
height, width, channels = img.shape
# img是灰度图的话：height, width = img.shape

# 总像素数
print(img.size)  # 263*263*3=207507
# 数据类型
print(img.dtype)  # uint8


# 4.ROI截取
face = img[100:200, 115:188]
cv2.imshow('face', face)
cv2.waitKey(0)


# 5.通道分割与合并
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# 更推荐的获取某一通道方式
b = img[:, :, 0]
cv2.imshow('b', b)
cv2.waitKey(0)
