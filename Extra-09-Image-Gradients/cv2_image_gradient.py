import cv2
import numpy as np

img = cv2.imread('sudoku.jpg', 0)

# 1.自己进行垂直边缘提取
kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)
dst_v = cv2.filter2D(img, -1, kernel)
# 自己进行水平边缘提取
dst_h = cv2.filter2D(img, -1, kernel.T)

cv2.imshow('edge', np.hstack((img, dst_v, dst_h)))
cv2.waitKey(0)


# 2.使用Sobel算子
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)  # 只计算x方向
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)  # 只计算y方向

cv2.imshow('edge', np.hstack((img, sobelx, sobely)))
cv2.waitKey(0)


# 3.使用Laplacian算子
laplacian = cv2.Laplacian(img, -1)  # 使用Laplacian算子

cv2.imshow('edge', np.hstack((img, laplacian)))
cv2.waitKey(0)
