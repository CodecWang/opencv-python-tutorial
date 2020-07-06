import cv2
import numpy as np


def nothing(x):
    '''
    ### 回调函数，x表示滑块的位置，本例暂不使用
    '''
    pass


def mouse_event(event, x, y, flags, param):
    '''
    ### 鼠标回调函数
    '''
    global brush_size, brush_color, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), brush_size, brush_color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), brush_size, brush_color, -1)


img = np.zeros((300, 512, 3), np.uint8)
img[:] = (255, 255, 255)  # 定义画板为白色
cv2.namedWindow('painting')

# 定义默认的笔刷尺寸和颜色
brush_size, brush_color = 8, (0, 0, 0)
drawing = False

# 创建rgb三个滑动条
cv2.createTrackbar('r', 'painting', 0, 255, nothing)
cv2.createTrackbar('g', 'painting', 0, 255, nothing)
cv2.createTrackbar('b', 'painting', 0, 255, nothing)
# 创建笔刷大小滑动条
cv2.createTrackbar('brush size', 'painting', 8, 15, nothing)
# 定义鼠标回调函数
cv2.setMouseCallback('painting', mouse_event)

while(True):
    cv2.imshow('painting', img)
    if cv2.waitKey(1) == 27:
        break

    r = cv2.getTrackbarPos('r', 'painting')
    g = cv2.getTrackbarPos('g', 'painting')
    b = cv2.getTrackbarPos('b', 'painting')
    brush_color = (b, g, r)
    brush_size = cv2.getTrackbarPos('brush size', 'painting')
