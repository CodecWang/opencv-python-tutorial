# [OpenCV-Python教程07：图像几何变换](http://ex2tron.wang/opencv-python-image-geometric-transformation/)

![](http://blog.codec.wang/cv2_perspective_transformations_inm.jpg)

学习如何旋转、平移、缩放和翻转图片。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 目标

- 实现旋转、平移和缩放图片
- OpenCV函数：`cv2.resize()`, `cv2.flip()`, `cv2.warpAffine()`

## 教程

> 图像的几何变换从原理上看主要包括两种：基于2×3矩阵的仿射变换（平移、缩放、旋转和翻转等）、基于3×3矩阵的透视变换，感兴趣的小伙伴可参考[番外篇：仿射变换与透视变换](/opencv-python-extra-warpaffine-warpperspective/)。

### 缩放图片

缩放就是调整图片的大小，使用`cv2.resize()`函数实现缩放。可以按照比例缩放，也可以按照指定的大小缩放：

```python
import cv2

img = cv2.imread('drawing.jpg')

# 按照指定的宽度、高度缩放图片
res = cv2.resize(img, (132, 150))
# 按照比例缩放，如x,y轴均放大一倍
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('shrink', res), cv2.imshow('zoom', res2)
cv2.waitKey(0)
```

我们也可以指定缩放方法`interpolation`，更专业点叫插值方法，默认是`INTER_LINEAR`，全部可以参考：[InterpolationFlags](https://docs.opencv.org/4.0.0/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121)

### 翻转图片

镜像翻转图片，可以用`cv2.flip()`函数：

```python
dst = cv2.flip(img, 1)
```

其中，参数2 = 0：垂直翻转(沿x轴)，参数2 > 0: 水平翻转(沿y轴)，参数2 < 0: 水平垂直翻转。

![](http://blog.codec.wang/cv2_flip_image_sample.jpg)

### 平移图片

要平移图片，我们需要定义下面这样一个矩阵，tx,ty是向x和y方向平移的距离：

$$
 M = \left[
 \begin{matrix}
   1 & 0 & t_x \newline
   0 & 1 & t_y 
  \end{matrix}
  \right] 
$$

平移是用仿射变换函数`cv2.warpAffine()`实现的：

```python
# 平移图片
import numpy as np

rows, cols = img.shape[:2]

# 定义平移矩阵，需要是numpy的float32类型
# x轴平移100，y轴平移50
M = np.float32([[1, 0, 100], [0, 1, 50]])
# 用仿射变换实现平移
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('shift', dst)
cv2.waitKey(0)
```

![](http://blog.codec.wang/cv2_translation_100_50.jpg)

### 旋转图片

旋转同平移一样，也是用仿射变换实现的，因此也需要定义一个变换矩阵。OpenCV直接提供了 `cv2.getRotationMatrix2D()`函数来生成这个矩阵，该函数有三个参数：

- 参数1：图片的旋转中心
- 参数2：旋转角度(正：逆时针，负：顺时针)
- 参数3：缩放比例，0.5表示缩小一半

```python
# 45°旋转图片并缩小一半
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotation', dst)
cv2.waitKey(0)
```

![逆时针旋转45°并缩放](http://blog.codec.wang/cv2_rotation_45_degree.jpg)


## 小结

- `cv2.resize()`缩放图片，可以按指定大小缩放，也可以按比例缩放。
- `cv2.flip()`翻转图片，可以指定水平/垂直/水平垂直翻转三种方式。
- 平移/旋转是靠仿射变换`cv2.warpAffine()`实现的。

## 接口文档

- [cv2.resize()](https://docs.opencv.org/4.0.0/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)
- [cv2.filp()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#gaca7be533e3dac7feb70fc60635adf441)
- [cv2.warpAffine()](https://docs.opencv.org/4.0.0/da/d54/group__imgproc__transform.html#ga0203d9ee5fcd28d40dbc4a1ea4451983)
- [cv2.getRotationMatrix2D()](https://docs.opencv.org/4.0.0/da/d54/group__imgproc__transform.html#gafbbc470ce83812914a70abfb604f4326)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/07.%20%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2)
- [Geometric Transformations of Images](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html)