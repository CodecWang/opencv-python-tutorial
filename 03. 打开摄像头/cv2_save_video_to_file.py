# ex2tron's blog:
# http://ex2tron.wang

import cv2

capture = cv2.VideoCapture(0)

# 定义编码方式并创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
outfile = cv2.VideoWriter('output.avi', fourcc, 25., (640, 480))

while(capture.isOpened()):
    ret, frame = capture.read()

    if ret:
        # 写入文件
        outfile.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
