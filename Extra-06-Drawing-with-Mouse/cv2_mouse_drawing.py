import cv2
import numpy as np


def mouse_event(event, x, y, flags, param):
    '''
    ### 鼠标的回调函数
    '''
    # 通过event判断具体是什么事件，这里是左键按下
    if event == cv2.EVENT_LBUTTONDOWN:
        print((x, y))


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
# 定义鼠标的回调函数
cv2.setMouseCallback('image', mouse_event)

while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(20) == 27:
        break

# 获取所有的事件
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
