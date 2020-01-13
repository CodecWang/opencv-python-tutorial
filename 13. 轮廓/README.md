# [OpenCV-Python教程13：轮廓](http://ex2tron.wang/opencv-python-contours/)

![](http://blog.codec.wang/cv2_understand_contours.jpg)

学习如何寻找并绘制轮廓。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 目标

- 了解轮廓概念
- 寻找并绘制轮廓
- OpenCV函数：`cv2.findContours()`, `cv2.drawContours()`

## 教程

### 啥叫轮廓

轮廓是一系列相连的点组成的曲线，代表了物体的基本外形。

谈起轮廓不免想到边缘，它们确实很像。简单的说，**轮廓是连续的，边缘并不全都连续**（下图）。其实边缘主要是作为图像的特征使用，比如可以用边缘特征可以区分脸和手，而轮廓主要用来分析物体的形态，比如物体的周长和面积等，可以说边缘包括轮廓。

![边缘和轮廓的区别](http://blog.codec.wang/cv2_understand_contours.jpg)

寻找轮廓的操作一般用于二值化图，所以通常会使用阈值分割或Canny边缘检测先得到二值图。

> 经验之谈：**寻找轮廓是针对白色物体的**，一定要保证物体是白色，而背景是黑色，**不然很多人在寻找轮廓时会找到图片最外面的一个框**。

### 寻找轮廓

使用`cv2.findContours()`寻找轮廓：

```python
import cv2

img = cv2.imread('handwriting.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 寻找二值化图中的轮廓
image, contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))  # 结果应该为2
```

- 参数2：轮廓的查找方式，一般使用cv2.RETR_TREE，表示提取所有的轮廓并建立轮廓间的层级。更多请参考：[RetrievalModes](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga819779b9857cc2f8601e6526a3a5bc71)
- 参数3：轮廓的近似方法。比如对于一条直线，我们可以存储该直线的所有像素点，也可以只存储起点和终点。使用cv2.CHAIN_APPROX_SIMPLE就表示用尽可能少的像素点表示轮廓。更多请参考：[ContourApproximationModes](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga4303f45752694956374734a03c54d5ff)
- 简便起见，这两个参数也可以直接用真值3和2表示。

函数有3个返回值，image还是原来的二值化图片，hierarchy是轮廓间的层级关系（[番外篇：轮廓层级](/opencv-python-extra-contours-hierarchy/)），这两个暂时不用理会。我们主要看contours，它就是找到的轮廓了，以数组形式存储，记录了每条轮廓的所有像素点的坐标(x,y)。

![](http://blog.codec.wang/cv2_find_contours_contours.jpg)

### 绘制轮廓

轮廓找出来后，为了方便观看，可以像前面图中那样用红色画出来：`cv2.drawContours()`

```python
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
```

其中参数2就是得到的contours，参数3表示要绘制哪一条轮廓，-1表示绘制所有轮廓，参数4是颜色（B/G/R通道，所以(0,0,255)表示红色），参数5是线宽，之前在绘制图形中介绍过。

> 经验之谈：很多人画图时明明用了彩色，但没有效果，请检查你是在哪个图上画，画在灰度图和二值图上显然是没有彩色的(⊙o⊙)。

一般情况下，我们会首先获得要操作的轮廓，再进行轮廓绘制及分析：

```python
cnt = contours[1]
cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)
```

## 小结

- 轮廓特征非常有用，使用`cv2.findContours()`寻找轮廓，`cv2.drawContours()`绘制轮廓。

## 接口文档

- [cv2.findContours()](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0)
- [cv2.RetrievalModes](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga819779b9857cc2f8601e6526a3a5bc71)
- [cv2.ContourApproximationModes](https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#ga4303f45752694956374734a03c54d5ff)
- [cv2.drawContours()](https://docs.opencv.org/4.0.0/d6/d6e/group__imgproc__draw.html#ga746c0625f1781f1ffc9056259103edbc)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/13.%20%E8%BD%AE%E5%BB%93)
- [Contours : Getting Started](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html)