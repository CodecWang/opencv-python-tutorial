import cv2
import numpy as np

start, end = (0, 0), (0, 0)
drawing = False


def mouse_event(event, x, y, flags, param):
    global start, drawing, end, temp

    # 鼠标按下，开始画图：记录下起点
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    # 实时移动的位置作为矩形终点（右下角点）
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end = (x, y)
    # 鼠标释放后，停止绘图
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, start, (x, y), (0, 255, 0), 2)
        start = end = (0, 0)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)

while(True):
    # 下面这句话很关键，拷贝出原图，这样才可以实时画一个矩形
    temp = np.copy(img)
    if(drawing and end != (0, 0)):
        cv2.rectangle(temp, start, end, (255, 0, 0), 2)

    cv2.imshow('image', temp)
    if cv2.waitKey(20) == 27:
        break
