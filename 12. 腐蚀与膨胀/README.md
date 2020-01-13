# [OpenCV-Python教程12：腐蚀与膨胀](http://ex2tron.wang/opencv-python-erode-and-dilate/)

![](http://blog.codec.wang/cv2_understand_morphological.jpg)

学习常用形态学操作：腐蚀膨胀，开运算和闭运算。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 目标

- 了解形态学操作的概念
- 学习膨胀、腐蚀、开运算和闭运算等形态学操作
- OpenCV函数：`cv2.erode()`, `cv2.dilate()`, `cv2.morphologyEx()`

## 教程

### 啥叫形态学操作

形态学操作其实就是**改变物体的形状**，比如腐蚀就是"变瘦"，膨胀就是"变胖"，看下图就明白了：

![](http://blog.codec.wang/cv2_understand_morphological.jpg)

> 经验之谈：形态学操作一般作用于二值化图，来连接相邻的元素或分离成独立的元素。**腐蚀和膨胀是针对图片中的白色部分！**

### 腐蚀

腐蚀的效果是把图片"变瘦"，其原理是在原图的小区域内取局部最小值。因为是二值化图，只有0和255，所以小区域内有一个是0该像素点就为0：

![](http://blog.codec.wang/cv2_understand_erosion.jpg)

这样原图中边缘地方就会变成0，达到了瘦身目的（小胖福利(●ˇ∀ˇ●)）

OpenCV中用`cv2.erode()`函数进行腐蚀，只需要指定核的大小就行：

```python
import cv2
import numpy as np

img = cv2.imread('j.bmp', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel)  # 腐蚀
```

> 这个核也叫结构元素，因为形态学操作其实也是应用卷积来实现的。结构元素可以是矩形/椭圆/十字形，可以用`cv2.getStructuringElement()`来生成不同形状的结构元素，比如：

```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 椭圆结构
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 十字形结构
```

![](http://blog.codec.wang/cv2_morphological_struct_element.jpg)

### 膨胀

膨胀与腐蚀相反，取的是局部最大值，效果是把图片"变胖"：

```python
dilation = cv2.dilate(img, kernel)  # 膨胀
```

### 开/闭运算

先腐蚀后膨胀叫开运算（因为先腐蚀会分开物体，这样容易记住），其作用是：分离物体，消除小区域。这类形态学操作用`cv2.morphologyEx()`函数实现：

```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定义结构元素

img = cv2.imread('j_noise_out.bmp', 0)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # 开运算
```

闭运算则相反：先膨胀后腐蚀（先膨胀会使白色的部分扩张，以至于消除/"闭合"物体里面的小黑洞，所以叫闭运算）

```python
img = cv2.imread('j_noise_in.bmp', 0)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # 闭运算
```

![](http://blog.codec.wang/cv2_morphological_opening_closing.jpg)

> 经验之谈：很多人对开闭运算的作用不是很清楚（好吧，其实是比较容易混◑﹏◐），但看上图↑，不用怕：如果我们的目标物体外面有很多无关的小区域，就用开运算去除掉；如果物体内部有很多小黑洞，就用闭运算填充掉。

接下来的3种形态学操作并不常用，大家有兴趣可以看看（因为较短，没有做成番外篇）：

### 其他形态学操作

- 形态学梯度：膨胀图减去腐蚀图，`dilation - erosion`，这样会得到物体的轮廓：

```python
img = cv2.imread('school.bmp', 0)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
```

![](http://blog.codec.wang/cv2_morphological_gradient.jpg)

- 顶帽：原图减去开运算后的图：`src - opening`

```python
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
```

- 黑帽：闭运算后的图减去原图：`closing - src`

```python
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
```

## 小结

- 形态学操作就是改变物体的形状，如腐蚀使物体"变瘦"，膨胀使物体"变胖"。
- 先腐蚀后膨胀会分离物体，所以叫开运算，常用来去除小区域物体。
- 先膨胀后腐蚀会消除物体内的小洞，所以叫闭运算。开/闭理解了之后很容易记忆噢(⊙o⊙)。

## 接口文档

- [cv2.erode()](https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#gaeb1e0c1033e3f6b891a25d0511362aeb)
- [cv2.getStructuringElement()](https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#gac342a1bb6eabf6f55c803b09268e36dc)
- [cv2.dilate()](https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga4ff0f3318642c4f469d0e11f242f3b6c)
- [cv2.MorphShapes](https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#gac2db39b56866583a95a5680313c314ad)
- [cv2.morphologyEx()](https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)
- [cv2.MorphTypes](https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga7be549266bad7b2e6a04db49827f9f32)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/12.%20%E8%85%90%E8%9A%80%E4%B8%8E%E8%86%A8%E8%83%80)
- [Morphological Operations](http://homepages.inf.ed.ac.uk/rbf/HIPR2/morops.htm)
- [Computer Vision: Algorithms and Applications](http://szeliski.org/Book/)