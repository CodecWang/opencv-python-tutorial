# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

# 载入手写数字图片
img = cv2.imread('handwriting.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)

# 创建出两幅彩色图用于绘制
img_color1 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
img_color2 = np.copy(img_color1)

# 计算数字1的轮廓特征
cnt = contours[1]
cv2.drawContours(img_color1, [cnt], 0, (0, 0, 255), 2)

# 1.轮廓面积
area = cv2.contourArea(cnt)  # 6289.5
print(area)


# 2.轮廓周长
perimeter = cv2.arcLength(cnt, True)  # 527.4041
print(perimeter)


# 3.图像矩
M = cv2.moments(cnt)
print(M)
print(M['m00'])  # 同前面的面积：6289.5
cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']  # 质心
print(cx, cy)

# 4.图像外接矩形和最小外接矩形
x, y, w, h = cv2.boundingRect(cnt)  # 外接矩形
cv2.rectangle(img_color1, (x, y), (x + w, y + h), (0, 255, 0), 2)

rect = cv2.minAreaRect(cnt)  # 最小外接矩形
box = np.int0(cv2.boxPoints(rect))  # 矩形的四个角点并取整
cv2.drawContours(img_color1, [box], 0, (255, 0, 0), 2)

cv2.imshow('contours', img_color1)
cv2.waitKey(0)


# 5.最小外接圆
(x, y), radius = cv2.minEnclosingCircle(cnt)
(x, y, radius) = map(int, (x, y, radius))  # 这也是取整的一种方式噢
cv2.circle(img_color2, (x, y), radius, (0, 0, 255), 2)


# 6.拟合椭圆
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img_color2, ellipse, (0, 255, 0), 2)

cv2.imshow('contours2', img_color2)
cv2.waitKey(0)
