# [OpenCV-Python教程04：图像基本操作](http://ex2tron.wang/opencv-python-basic-operations/)

![](http://blog.codec.wang/cv2_lena_face_roi_crop.jpg)

学习获取和修改像素点的值，ROI感兴趣区域，通道分离合并等基本操作。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 目标

- 访问和修改图片像素点的值
- 获取图片的宽、高、通道数等属性
- 了解感兴趣区域ROI
- 分离和合并图像通道

## 教程

### 获取和修改像素点值

我们先读入一张图片：

``` python
import cv2

img = cv2.imread('lena.jpg')
```

通过行列的坐标来获取某像素点的值，对于彩色图，结果是B,G,R三个值的列表，对于灰度图或单通道图，只有一个值：

```python
px = img[100, 90]
print(px)  # [103 98 197]

# 只获取蓝色blue通道的值
px_blue = img[100, 90, 0]
print(px_blue)  # 103
```

还记得吗？行对应y，列对应x，所以其实是`img[y, x]`，需要注意噢(●ˇ∀ˇ●)。容易混淆的话，可以只记行和列，行在前，列在后。

修改像素的值也是同样的方式：

```python
img[100, 90] = [255, 255, 255]
print(img[100, 90])  # [255 255 255]
```

> 经验之谈：还有一种性能更好的方式，获取：`img.item(100,100,0)`，修改：`img.itemset((100,100,0),255)`，但这种方式只能B,G,R逐一进行。

注意：这步操作只是内存中的img像素点值变了，因为没有保存，所以原图并没有更改。

### 图片属性

`img.shape`获取图像的形状，图片是彩色的话，返回一个包含**行数（高度）、列数（宽度）和通道数**的元组，灰度图只返回行数和列数：

```python
print(img.shape)  # (263, 247, 3)
# 形状中包括行数、列数和通道数
height, width, channels = img.shape
# img是灰度图的话：height, width = img.shape
```

`img.dtype`获取图像数据类型：

```python
print(img.dtype)  # uint8
```

> 经验之谈：多数错误是因为数据类型不对导致的，所以健壮的代码应该对这个属性加以判断。

`img.size`获取图像总像素数：

```python
print(img.size)  # 263*247*3=194883
```

### ROI

[ROI](https://baike.baidu.com/item/ROI/1125333#viewPageContent)：Region of Interest，感兴趣区域。什么意思呢？比如我们要检测眼睛，因为眼睛肯定在脸上，所以我们感兴趣的只有脸这部分，其他都不care，所以可以单独把脸截取出来，这样就可以大大节省计算量，提高运行速度。

![只关心脸( ╯□╰ )](http://blog.codec.wang/cv2_lena_face_roi_crop.jpg)

截取ROI非常简单，指定图片的范围即可（后面我们学了特征后，就可以自动截取辣，(ง •_•)ง）：

```python
# 截取脸部ROI
face = img[100:200, 115:188]
cv2.imshow('face', face)
cv2.waitKey(0)
```

### 通道分割与合并

彩色图的BGR三个通道是可以分开单独访问的，也可以将单独的三个通道合并成一副图像。分别使用`cv2.split()`和`cv2.merge()`：

```python
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
```

`split()`函数比较耗时，**更高效的方式是用numpy中的索引**，如提取B通道：

```python
b = img[:, :, 0]
cv2.imshow('blue', b)
cv2.waitKey(0)
```

## 小结

- `img[y,x]`获取/设置像素点值，`img.shape`：图片的形状（行数、列数、通道数）,`img.dtype`：图像的数据类型。
- `img[y1:y2,x1:x2]`进行ROI截取，`cv2.split()/cv2.merge()`通道分割/合并。更推荐的获取单通道方式：`b = img[:, :, 0]`。

## 练习

1. 打开lena.jpg，将帽子部分（高：25~120，宽：50~220）的红色通道截取出来并显示。

## 接口文档

- [cv2.split()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga0547c7fed86152d7e9d0096029c8518a)
- [cv2.merge()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga7d7b4d6c6ee504b30a20b1680029c7b4)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/04.%20%E5%9B%BE%E5%83%8F%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C)
- [Basic Operations on Images](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#basic-ops)