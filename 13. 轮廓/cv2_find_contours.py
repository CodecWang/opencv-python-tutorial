# ex2tron's blog:
# http://ex2tron.wang

import cv2

img = cv2.imread('handwriting.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 使用Otsu自动阈值，注意用的是cv2.THRESH_BINARY_INV
ret, thresh = cv2.threshold(
    img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 寻找轮廓
image, contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]
cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)

cv2.imshow('contours', img)
cv2.waitKey(0)
