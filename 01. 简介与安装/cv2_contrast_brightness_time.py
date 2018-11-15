# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

# 开始计时
start = cv2.getTickCount()

# 读入一张图片并调整对比度和亮度
img = cv2.imread('lena.jpg')
res = np.uint8(np.clip((0.8 * img + 80), 0, 255))

# 停止计时
end = cv2.getTickCount()

# 单位：s
print((end - start) / cv2.getTickFrequency())
