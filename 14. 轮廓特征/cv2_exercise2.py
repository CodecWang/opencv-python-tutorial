# ex2tron's blog:
# http://ex2tron.wang

import cv2

# 载入原图
img = cv2.imread('abc.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
# 找到ABC的轮廓
b, c, a = contours[0], contours[3], contours[4]

# 载入标准模板图
img_a = cv2.imread('template_a.jpg', 0)
_, th = cv2.threshold(img_a, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(th, 3, 2)
# 字母A的轮廓
template_a = contours[0]

print(cv2.matchShapes(a, template_a, 1, 0.0))  # 0.02557(最相似)
print(cv2.matchShapes(b, template_a, 1, 0.0))  # 0.80585
print(cv2.matchShapes(c, template_a, 1, 0.0))  # 3.26050
