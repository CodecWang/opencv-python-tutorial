import cv2
import matplotlib.image as pli
import matplotlib.pyplot as plt

# 1.显示灰度图
img = cv2.imread('lena.jpg', 0)
plt.imshow(img, cmap='gray')
plt.show()

# 2.显示彩色图
img = cv2.imread('lena.jpg')
# 通道翻转：b/g/r -> r/g/b
img2 = img[:, :, ::-1]
# 或使用
# img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 显示不正确的图
plt.subplot(121), plt.imshow(img)
# 显示正确的图
plt.subplot(122)
plt.xticks([]), plt.yticks([])  # 隐藏x和y轴
plt.imshow(img2)

plt.show()


# 3.加载和保存图片

img = pli.imread('lena.jpg')
plt.imshow(img)

# 保存图片，需放在show()函数之前
plt.savefig('lena2.jpg')
plt.show()
