# [OpenCV-Python教程14：轮廓特征](http://ex2tron.wang/opencv-python-contour-features/)

![](http://blog.codec.wang/cv2_min_rect_rect_bounding.jpg)

学习计算轮廓特征，如面积、周长、最小外接矩形等。<!-- more -->图片等可到[源码处](#引用)下载。

------

## 目标

- 计算物体的周长、面积、质心、最小外接矩形等
- OpenCV函数：`cv2.contourArea()`, `cv2.arcLength()`, `cv2.approxPolyDP()` 等

## 教程

在计算轮廓特征之前，我们先用上一节的代码把轮廓找到：

![](http://blog.codec.wang/cv2_31_handwriting_sample.jpg)

```python
import cv2
import numpy as np

img = cv2.imread('handwriting.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)

# 以数字3的轮廓为例
cnt = contours[0]
```

为了便于绘制，我们创建出两幅彩色图，并把轮廓画在第一幅图上：

```python
img_color1 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
img_color2 = np.copy(img_color1)
cv2.drawContours(img_color1, [cnt], 0, (0, 0, 255), 2)
```

### 轮廓面积

```python
area = cv2.contourArea(cnt)  # 4386.5
```

注意轮廓特征计算的结果并不等同于像素点的个数，而是根据几何方法算出来的，所以有小数。

> 如果统计二值图中像素点个数，应尽量避免循环，**可以使用`cv2.countNonZero()`**，更加高效。

### 轮廓周长

```python
perimeter = cv2.arcLength(cnt, True)  # 585.7
```

参数2表示轮廓是否封闭，显然我们的轮廓是封闭的，所以是True。

### 图像矩

矩可以理解为图像的各类几何特征，详情请参考：[[Image Moments](http://en.wikipedia.org/wiki/Image_moment)]

```python
M = cv2.moments(cnt)
```

M中包含了很多轮廓的特征信息，比如M['m00']表示轮廓面积，与前面`cv2.contourArea()`计算结果是一样的。质心也可以用它来算：

```python
cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']  # (205, 281)
```

### 外接矩形

形状的外接矩形有两种，如下图，绿色的叫外接矩形，表示不考虑旋转并且能包含整个轮廓的矩形。蓝色的叫最小外接矩，考虑了旋转：

![](http://blog.codec.wang/cv2_min_rect_rect_bounding.jpg)

```python
x, y, w, h = cv2.boundingRect(cnt)  # 外接矩形
cv2.rectangle(img_color1, (x, y), (x + w, y + h), (0, 255, 0), 2)
```

```python
rect = cv2.minAreaRect(cnt)  # 最小外接矩形
box = np.int0(cv2.boxPoints(rect))  # 矩形的四个角点取整
cv2.drawContours(img_color1, [box], 0, (255, 0, 0), 2)
```

其中np.int0(x)是把x取整的操作，比如377.93就会变成377，也可以用x.astype(np.int)。

### 最小外接圆

外接圆跟外接矩形一样，找到一个能包围物体的最小圆：

```python
(x, y), radius = cv2.minEnclosingCircle(cnt)
(x, y, radius) = np.int0((x, y, radius))  # 圆心和半径取整
cv2.circle(img_color2, (x, y), radius, (0, 0, 255), 2)
```

![](http://blog.codec.wang/cv2_min_enclosing_circle.jpg)

### 拟合椭圆

我们可以用得到的轮廓拟合出一个椭圆：

```python
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img_color2, ellipse, (255, 255, 0), 2)
```

![](http://blog.codec.wang/cv2_fitting_ellipse.jpg)

### 形状匹配

`cv2.matchShapes()`可以检测两个形状之间的相似度，返回**值越小，越相似**。先读入下面这张图片：

![](http://blog.codec.wang/cv2_match_shape_shapes.jpg)

```python
img = cv2.imread('shapes.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
img_color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)  # 用于绘制的彩色图
```

图中有3条轮廓，我们用A/B/C表示：

```python
cnt_a, cnt_b, cnt_c = contours[0], contours[1], contours[2]
print(cv2.matchShapes(cnt_b, cnt_b, 1, 0.0))  # 0.0
print(cv2.matchShapes(cnt_b, cnt_c, 1, 0.0))  # 2.17e-05
print(cv2.matchShapes(cnt_b, cnt_a, 1, 0.0))  # 0.418
```

可以看到BC相似程度比AB高很多，并且图形的旋转或缩放并没有影响。其中，参数3是匹配方法，详情可参考：[ShapeMatchModes](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gaf2b97a230b51856d09a2d934b78c015f)，参数4是OpenCV的预留参数，暂时没有实现，可以不用理会。

形状匹配是通过图像的Hu矩来实现的(`cv2.HuMoments()`)，大家如果感兴趣，可以参考：[Hu-Moments](http://en.wikipedia.org/wiki/Image_moment#Rotation_invariant_moments)

## 练习

1. 前面我们是对图片中的数字3进行轮廓特征计算的，大家换成数字1看看。
2. （选做）用形状匹配比较两个字母或数字（这相当于很简单的一个[OCR](https://baike.baidu.com/item/%E5%85%89%E5%AD%A6%E5%AD%97%E7%AC%A6%E8%AF%86%E5%88%AB/4162921?fr=aladdin&fromid=25995&fromtitle=OCR)噢）。

## 小结

常用的轮廓特征：

- `cv2.contourArea()`算面积，`cv2.arcLength()`算周长，`cv2.boundingRect()`算外接矩。
- `cv2.minAreaRect()`算最小外接矩，`cv2.minEnclosingCircle()`算最小外接圆。
- `cv2.matchShapes()`进行形状匹配。

## 接口文档

- [cv2.contourArea()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga2c759ed9f497d4a618048a2f56dc97f1)
- [cv2.arcLength()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga8d26483c636be6b35c3ec6335798a47c)
- [cv2.moments()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga556a180f43cab22649c23ada36a8a139)
- [cv2.boundingRect()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga103fcbda2f540f3ef1c042d6a9b35ac7)
- [cv2.minAreaRect()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga3d476a3417130ae5154aea421ca7ead9)
- [cv2.minEnclosingCircle()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga8ce13c24081bbc7151e9326f412190f1)
- [cv2.fitEllipse()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gaf259efaad93098103d6c27b9e4900ffa)
- [cv2.matchShapes()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gaadc90cb16e2362c9bd6e7363e6e4c317)
- [cv2.ShapeMatchModes](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gaf2b97a230b51856d09a2d934b78c015f)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/14.%20%E8%BD%AE%E5%BB%93%E7%89%B9%E5%BE%81)
- [Contour Features](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html)
- [Contours : More Functions](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html)