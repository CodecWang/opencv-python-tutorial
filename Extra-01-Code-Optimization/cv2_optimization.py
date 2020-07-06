import cv2
import numpy as np

# 性能对比优化

start = cv2.getTickCount()
x = 10
y = x * x * x
end = cv2.getTickCount()
print((end - start) / cv2.getTickFrequency())

start = cv2.getTickCount()
x = 10
y = x**3
end = cv2.getTickCount()
print((end - start) / cv2.getTickFrequency())

start = cv2.getTickCount()
x = np.uint8([10])
y = x * x * x  # 最慢
end = cv2.getTickCount()
print((end - start) / cv2.getTickFrequency())
