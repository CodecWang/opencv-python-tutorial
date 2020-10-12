import cv2

# 开始计时
start = cv2.getTickCount()

# 读入一张图片
# You should use Flag here so that it will read colored or grey 
img = cv2.imread('lena.jpg', 0)

# 停止计时
end = cv2.getTickCount()

# 单位：s
print((end - start) / cv2.getTickFrequency())
