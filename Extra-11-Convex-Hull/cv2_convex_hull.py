import cv2
import numpy as np


# 多边形逼近
# 1.先找到轮廓
img = cv2.imread('unregular.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
cnt = contours[0]

# 2.进行多边形逼近，得到多边形的角点
approx = cv2.approxPolyDP(cnt, 3, True)

# 3.画出多边形
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [approx], True, (0, 255, 0), 2)
print(len(approx))  # 角点的个数
cv2.imshow('approxPloyDP', image)
cv2.waitKey(0)


# 凸包
# 1.先找到轮廓
img = cv2.imread('convex.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
cnt = contours[0]

# 2.寻找凸包，得到凸包的角点
hull = cv2.convexHull(cnt)

# 3.绘制凸包
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)
cv2.imshow('convex hull', image)
cv2.waitKey(0)

# 轮廓是否是凸形的
print(cv2.isContourConvex(hull))  # True

# 关于returnPoints的理解：
print(hull[0])  # [[362 184]]（坐标）
hull2 = cv2.convexHull(cnt, returnPoints=False)
print(hull2[0])  # [510]（cnt中的索引）
print(cnt[510])  # [[362 184]]


# 点到轮廓距离(多边形测试)
dist = cv2.pointPolygonTest(cnt, (100, 100), True)  # -3.53
print(dist)
