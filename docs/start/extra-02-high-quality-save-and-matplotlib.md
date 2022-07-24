# 番外篇：无损保存和 Matplotlib

![](http://cos.codec.wang/cv2_matplotlib_show_gray_image.jpg)

了解常用图片格式和 OpenCV 高质量保存图片的方式，学习如何使用 Matplotlib 显示 OpenCV 图像。

## 无损保存

事实上，我们日常看到的大部分图片都是压缩过的，那么都有哪些常见的图片格式呢？

### 常用图片格式

- [bmp](https://baike.baidu.com/item/BMP/35116)
  - 全称：Bitmap
  - **不压缩**
- [jpg](https://baike.baidu.com/item/JPEG)
  - 全称：Joint Photographic Experts Group
  - **有损压缩方式**
- [png](https://baike.baidu.com/item/PNG)
  - 全称：Portable Network Graphics
  - **无损压缩方式**

简单来说，同一个文件保存成不同的格式后，文件大小上 bmp 肯定是最大的，而 png 和 jpg，不同的压缩比结果会有所不同。可以用画图工具新建一副 100×100 的图像，分别保存成这三种格式来验证：

![](http://cos.codec.wang/cv2_high_save_mspaint_format.jpg)

### 高质量保存

用 cv2.imwrite() 保存图片时，可以传入第三个参数，用于控制保存质量：

- `cv2.IMWRITE_JPEG_QUALITY`：jpg 质量控制，取值 0~100，值越大，质量越好，默认为 95
- `cv2.IMWRITE_PNG_COMPRESSION`：png 质量控制，取值 0~9，值越大，压缩比越高，默认为 1

还有诸如`CV_IMWRITE_WEBP_QUALITY`的参量，不常用，请参考：[ImwriteFlags](https://docs.opencv.org/4.0.0/d4/da8/group__imgcodecs.html#ga292d81be8d76901bff7988d18d2b42ac>)。

举例来说，原图 lena.jpg 的分辨率是 350×350，大小 49.7KB。我们把它转成不同格式看下：

```python
import cv2

new_img = cv2.imread('lena.jpg')

# bmp
cv2.imwrite('img_bmp.bmp',new_img) # 文件大小：359KB

# jpg 默认 95% 质量
cv2.imwrite('img_jpg95.jpg',new_img) # 文件大小：52.3KB
# jpg 20% 质量
cv2.imwrite('img_jpg20.jpg',new_img,[int(cv2.IMWRITE_JPEG_QUALITY),20]) # 文件大小：8.01KB
# jpg 100% 质量
cv2.imwrite('img_jpg100.jpg',new_img,[int(cv2.IMWRITE_JPEG_QUALITY),100]) # 文件大小：82.5KB

# png 默认 1 压缩比
cv2.imwrite('img_png1.png',new_img) # 文件大小：240KB
# png 9 压缩比
cv2.imwrite('img_png9.png',new_img,[int(cv2.IMWRITE_PNG_COMPRESSION),9]) # 文件大小：207KB
```

可以看到：

- bmp 文件是最大的，没有任何压缩（1 个像素点 1byte，3 通道的彩色图总大小：350×350×3/1024 ≈ 359 KB）
- jpg/png 本身就有压缩的，所以就算是 100% 的质量保存，体积也比 bmp 小很多
- jpg 的容量优势很明显，这也是它为什么如此流行的原因

> 思考：为什么原图 49.7KB，保存成 bmp 或其他格式反而大了呢？

这是个很有趣的问题，很多童鞋都问过我。这里需要明确的是保存新格式时，**容量大小跟原图的容量没有直接关系，而是取决于原图的分辨率大小和原图本身的内容（压缩方式）**，所以 lena.jpg 保存成不压缩的 bmp 格式时，容量大小就是固定的 350×350×3/1024 ≈ 359 KB；另外，容量变大不代表画质提升噢，不然就逆天了~~~

## Matplotlib

Matplotlib 是 Python 的一个很常用的绘图库，有兴趣的可以去[官网](http://www.matplotlib.org/)学习更多内容。

### 显示灰度图

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg', 0)

# 灰度图显示，cmap(color map) 设置为 gray
plt.imshow(img, cmap='gray')
plt.show()
```

结果如下：

![](http://cos.codec.wang/cv2_matplotlib_show_gray_image.jpg)

### 显示彩色图

**OpenCV 中的图像是以 BGR 的通道顺序存储的**，但 Matplotlib 是以 RGB 模式显示的，所以直接在 Matplotlib 中显示 OpenCV 图像会出现问题，因此需要转换一下：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
img2 = img[:, :, ::-1]
# 或使用
# img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 显示不正确的图
plt.subplot(121),plt.imshow(img)

# 显示正确的图
plt.subplot(122)
plt.xticks([]), plt.yticks([]) # 隐藏 x 和 y 轴
plt.imshow(img2)

plt.show()
```

> `img[:,:,0]`表示图片的蓝色通道，`img[:,:,::-1]`就表示 BGR 翻转，变成 RGB，说明一下：

熟悉 Python 的童鞋应该知道，对一个字符串 s 翻转可以这样写：`s[::-1]`，'abc'变成'cba'，-1 表示逆序。图片是二维的，所以完整地复制一副图像就是：

```python
img2 = img[:,:] # 写全就是：img2 = img[0:height,0:width]
```

而图片是有三个通道，相当于一个长度为 3 的字符串，所以通道翻转与图片复制组合起来便是`img[:,:,::-1]`。

结果如下：

![](http://cos.codec.wang/cv2_matplotlib_show_color_image.jpg)

### 加载和保存图片

不使用 OpenCV，Matplotlib 也可以加载和保存图片：

```python
import matplotlib.image as pli

img = pli.imread('lena.jpg')
plt.imshow(img)

# 保存图片，需放在 show() 函数之前
plt.savefig('lena2.jpg')
plt.show()
```

## 接口文档

- [cv2.imwrite()](https://docs.opencv.org/4.0.0/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce)
- [ImwriteFlags](https://docs.opencv.org/4.0.0/d4/da8/group__imgcodecs.html#ga292d81be8d76901bff7988d18d2b42ac)

## 引用

- [本节源码](https://github.com/codecwang/OpenCV-Python-Tutorial/tree/master/Extra-02-High-Quality-Save-and-Matplotlib)
- [聊一聊几种常用 web 图片格式](https://segmentfault.com/a/1190000013589397)
- [Matplotlib 官网](http://www.matplotlib.org/)
