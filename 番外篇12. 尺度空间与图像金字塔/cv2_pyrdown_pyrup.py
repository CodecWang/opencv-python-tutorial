# ex2tron's blog:
# http://ex2tron.wang

import cv2

img = cv2.imread('lena.jpg')
lower = cv2.pyrDown(img)  # 向下采样一级
higher = cv2.pyrUp(img)  # 向上采样一级


cv2.imshow('origin', img)
cv2.imshow('lower', lower)
cv2.imshow('higher', higher)
cv2.waitKey(0)
