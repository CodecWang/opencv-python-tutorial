import cv2
import numpy as np

drawing = False  # 是否开始画图
mode = True  # True：画矩形，False：画圆
start = (-1, -1)


def mouse_event(event, x, y, flags, param):
    global start, drawing, mode

    # 左键按下：开始画图
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    # 鼠标移动，画图
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    # 左键释放：结束画图
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)

while(True):
    cv2.imshow('image', img)
    # 按下m切换模式
    if cv2.waitKey(1) == ord('m'):
        mode = not mode
    # 按下ESC退出
    elif cv2.waitKey(1) == 27:
        break
