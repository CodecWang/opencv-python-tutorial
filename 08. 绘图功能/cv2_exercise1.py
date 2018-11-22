# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

img = np.zeros((200, 200, 3), np.uint8)

# 画OpenCV的logo，其实很简单
# 1.先画一个0°到300°的圆
# 2.再在中心画一个跟背景颜色一样的小圆
# 3.重复前两部，并且旋转一定的角度即可

# 画绿色的部分
cv2.ellipse(img, (43, 125), (45, 45), 0, 0, 300,
            (0, 255, 0), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (43, 125), 15, (0, 0, 0), -1, lineType=cv2.LINE_AA)

# 画红色的部分
cv2.ellipse(img, (90, 40), (45, 45), 120, 0, 300,
            (0, 0, 255), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (90, 40), 15, (0, 0, 0), -1, lineType=cv2.LINE_AA)

# 画蓝色的部分
cv2.ellipse(img, (137, 125), (45, 45), -60, 0, 300,
            (255, 0, 0), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (137, 125), 15, (0, 0, 0), -1, lineType=cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
