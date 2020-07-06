import cv2

# 1.读入图片
img = cv2.imread('hierarchy.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(
    img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 2.寻找轮廓 cv2.RETR_TREE
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, 2)

# 3.绘制轮廓
print(len(contours), hierarchy, sep='\n')  # 8条
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

# 4.显示结果
cv2.imshow('contours', img)
cv2.waitKey(0)


# 不同轮廓寻找方式的不同
# cv2.RETR_LIST
_, _, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, 2)
print(hierarchy)
# 结果应该如下：
# [[[1 - 1 - 1 - 1]
#   [2  0 - 1 - 1]
#   [3  1 - 1 - 1]
#   [4  2 - 1 - 1]
#   [5  3 - 1 - 1]
#   [6  4 - 1 - 1]
#   [7  5 - 1 - 1]
#   [-1  6 - 1 - 1]]]


# cv2.RETR_EXTERNAL
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, 2)
print(len(contours), hierarchy, sep='\n')
# 结果应该如下：
# 3
# [[[1 - 1 - 1 - 1]
#   [2  0 - 1 - 1]
#   [-1  1 - 1 - 1]]]


# cv2.RETR_CCOMP
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, 2)
print(hierarchy)
# 结果应该如下：
# [[[1 - 1 - 1 - 1]
#   [2  0 - 1 - 1]
#   [4  1  3 - 1]
#   [-1 - 1 - 1  2]
#   [6  2  5 - 1]
#   [-1 - 1 - 1  4]
#   [7  4 - 1 - 1]
#   [-1  6 - 1 - 1]]]
