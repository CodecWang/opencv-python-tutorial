# 07: 图像几何变换

![](http://cos.codec.wang/cv2_perspective_transformations_inm.jpg)

学习如何旋转、平移、缩放和翻转图片。图片等可到文末引用处下载。

## 目标

- 实现旋转、平移和缩放图片
- OpenCV 函数：`cv2.resize()`, `cv2.flip()`, `cv2.warpAffine()`

## 教程

> 图像的几何变换从原理上看主要包括两种：基于 2×3 矩阵的仿射变换（平移、缩放、旋转和翻转等）、基于 3×3 矩阵的透视变换，感兴趣的小伙伴可参考 [番外篇：仿射变换与透视变换](./extra-05-warpaffine-warpperspective/)。

### 缩放图片

缩放就是调整图片的大小，使用`cv2.resize()`函数实现缩放。可以按照比例缩放，也可以按照指定的大小缩放：

```python
import cv2

img = cv2.imread('drawing.jpg')

# 按照指定的宽度、高度缩放图片
res = cv2.resize(img, (132, 150))
# 按照比例缩放，如 x,y 轴均放大一倍
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

其中，参数 2 = 0：垂直翻转 (沿 x 轴)，参数 2 &gt; 0: 水平翻转 (沿 y 轴)，参数 2 &lt; 0: 水平垂直翻转。

![](http://cos.codec.wang/cv2_flip_image_sample.jpg)

### 平移图片

要平移图片，我们需要定义下面这样一个矩阵，tx,ty 是向 x 和 y 方向平移的距离：

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

# 定义平移矩阵，需要是 numpy 的 float32 类型
# x 轴平移 100，y 轴平移 50
M = np.float32([[1, 0, 100], [0, 1, 50]])
# 用仿射变换实现平移
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('shift', dst)
cv2.waitKey(0)
```

![](http://cos.codec.wang/cv2_translation_100_50.jpg)

### 旋转图片

旋转同平移一样，也是用仿射变换实现的，因此也需要定义一个变换矩阵。OpenCV 直接提供了 `cv2.getRotationMatrix2D()`函数来生成这个矩阵，该函数有三个参数：

- 参数 1：图片的旋转中心
- 参数 2：旋转角度 (正：逆时针，负：顺时针)
- 参数 3：缩放比例，0.5 表示缩小一半

```python
# 45°旋转图片并缩小一半
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotation', dst)
cv2.waitKey(0)
```

![逆时针旋转 45°并缩放](http://cos.codec.wang/cv2_rotation_45_degree.jpg)

## 小结

- `cv2.resize()`缩放图片，可以按指定大小缩放，也可以按比例缩放。
- `cv2.flip()`翻转图片，可以指定水平/垂直/水平垂直翻转三种方式。
- 平移/旋转是靠仿射变换`cv2.warpAffine()`实现的。

## 接口文档

- [cv2.resize\(\)](https://docs.opencv.org/4.0.0/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)
- [cv2.filp\(\)](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#gaca7be533e3dac7feb70fc60635adf441)
- [cv2.warpAffine\(\)](https://docs.opencv.org/4.0.0/da/d54/group__imgproc__transform.html#ga0203d9ee5fcd28d40dbc4a1ea4451983)
- [cv2.getRotationMatrix2D\(\)](https://docs.opencv.org/4.0.0/da/d54/group__imgproc__transform.html#gafbbc470ce83812914a70abfb604f4326)

## 引用

- [本节源码](https://github.com/codecwang/OpenCV-Python-Tutorial/tree/master/07-Image-Geometric-Transformation)
- [Geometric Transformations of Images](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html)
