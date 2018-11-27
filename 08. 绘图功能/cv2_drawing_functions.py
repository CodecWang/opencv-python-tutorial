# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

# 创建一副黑色的图片
img = np.zeros((512, 512, 3), np.uint8)
# 1.画一条线宽为5的蓝色直线，参数2：起点，参数3：终点
cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)


# 2.画一个绿色边框的矩形，参数2：左上角坐标，参数3：右下角坐标
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)


# 3.画一个填充红色的圆，参数2：圆心坐标，参数3：半径
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)


# 4.在图中心画一个填充的半圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)


# 5.画一个闭合的四边形
# 定义四个顶点坐标
pts = np.array([[10, 5],  [50, 10], [70, 20], [20, 30]], np.int32)
# 顶点个数：4，矩阵变成顶点数*1*2维（注意numpy中-1的用法）
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))

# 使用cv2.polylines()画多条直线
line1 = np.array([[100, 20],  [300, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60],  [300, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100],  [300, 100]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [line1, line2, line3], True, (0, 255, 255))


# 6.添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'ex2tron', (10, 500), font,
            4, (255, 255, 255), 2, lineType=cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
