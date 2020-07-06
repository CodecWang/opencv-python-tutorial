import cv2
import numpy as np

new_img = cv2.imread('lena.jpg')
# new_img = np.zeros((100,100,3)) # 新建一副纯黑色图

# bmp
cv2.imwrite('img_bmp.bmp', new_img)  # 文件大小：359KB

# jpg 默认95%质量
cv2.imwrite('img_jpg95.jpg', new_img)  # 文件大小：52.3KB
# jpg 20%质量
cv2.imwrite('img_jpg20.jpg', new_img, [
            int(cv2.IMWRITE_JPEG_QUALITY), 20])  # 文件大小：8.01KB
# jpg 100%质量
cv2.imwrite('img_jpg100.jpg', new_img, [
            int(cv2.IMWRITE_JPEG_QUALITY), 100])  # 文件大小：82.5KB

# png 默认1压缩比
cv2.imwrite('img_png1.png', new_img)  # 文件大小：240KB
# png 9压缩比
cv2.imwrite('img_png9.png', new_img, [
            int(cv2.IMWRITE_PNG_COMPRESSION), 9])  # 文件大小：207KB
