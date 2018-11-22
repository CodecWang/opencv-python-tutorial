# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

# HSV中
# Blue：[[[120 255 255]]]
# Green：[[[ 60 255 255]]]
# Red：[[[  0 255 255]]]

capture = cv2.VideoCapture(1)

# 蓝色的范围
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

# 绿色的范围
lower_green = np.array([40, 90, 90])
upper_green = np.array([70, 255, 255])

# 红色的范围
lower_red = np.array([160, 120, 120])
upper_red = np.array([179, 255, 255])

while(True):
    # 1.捕获视频中的一帧
    ret, frame = capture.read()

    # 2.从BGR转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # 3.将所有的mask相加，就可以同时显示了
    mask = mask_blue + mask_green + mask_red

    # 4.保留原图中的三种颜色部分
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q'):
        break
