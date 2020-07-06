import cv2
import numpy as np

# 1.读入圆环
img = cv2.imread('circle_ring.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(
    img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 2.使用cv2.RETR_CCOMP寻找轮廓
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, 2)

# 3.找到内层轮廓并填充
# hierarchy的形状为(1,6,4)，使用np.squeeze压缩一维数据，变成(6,4)
hierarchy = np.squeeze(hierarchy)

for i in range(len(contours)):
    # 存在父轮廓，说明是里层
    if(hierarchy[i][3] != -1):
        cv2.drawContours(img, contours, i, (180, 215, 215), -1)

# 4.显示结果
cv2.imshow('fill', img)
cv2.waitKey(0)
