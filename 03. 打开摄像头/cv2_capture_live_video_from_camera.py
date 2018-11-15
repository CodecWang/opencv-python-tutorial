# ex2tron's blog:
# http://ex2tron.wang

import cv2

# 1.打开摄像头
capture = cv2.VideoCapture(2)

# 2.获取捕获的分辨率
width, height = capture.get(3), capture.get(4)
print(width, height)
# 以原分辨率的一倍来捕获，
# 参数1可以直接写数字，或者OpenCV符号表示
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)

while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
