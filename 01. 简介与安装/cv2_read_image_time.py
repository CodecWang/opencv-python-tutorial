# ex2tron's blog:
# http://ex2tron.wang

import cv2

# 开始计时
start = cv2.getTickCount()

# 读入一张图片
img = cv2.imread('lena.jpg')

# 停止计时
end = cv2.getTickCount()

# 单位：s
print((end - start) / cv2.getTickFrequency())
