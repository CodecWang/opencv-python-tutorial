import cv2
import numpy as np


def nothing(x):
    '''
    ### 回调函数，暂时无用
    '''
    pass


img = cv2.imread('lena.jpg')
cv2.namedWindow('image')

# 创建两个滑块
cv2.createTrackbar('brightness', 'image', 0, 100, nothing)
cv2.createTrackbar('contrast', 'image', 100, 300, nothing)

temp = img.copy()
rows, cols = img.shape[:2]

while(True):
    cv2.imshow('image', temp)
    if cv2.waitKey(1) == 27:
        break

    # 得到两个滑块的值
    brightness = cv2.getTrackbarPos('brightness', 'image')
    contrast = cv2.getTrackbarPos('contrast', 'image') * 0.01
    # 进行对比度和亮度调整
    temp = np.uint8(np.clip(contrast * img + brightness, 0, 255))
