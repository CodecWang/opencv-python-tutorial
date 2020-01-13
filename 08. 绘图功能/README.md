# [OpenCV-Python教程08：绘图功能](http://ex2tron.wang/opencv-python-drawing-function/)

![](http://blog.codec.wang/cv2_drawing_functions.jpg)

学习画线、圆和矩形等多种几何形状，给图片添加文字。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 目标

- 绘制各种几何形状、添加文字
- OpenCV函数：`cv2.line()`, `cv2.circle()`, `cv2.rectangle()`, `cv2.ellipse()`, `cv2.putText()`

## 教程

### 参数说明

绘制形状的函数有一些共同的参数，提前在此说明一下：

- img：要绘制形状的图片
- color：绘制的颜色
  - 彩色图就传入BGR的一组值，如蓝色就是(255,0,0)
  - 灰度图，传入一个灰度值就行
- thickness：线宽，默认为1；**对于矩形/圆之类的封闭形状而言，传入-1表示填充形状**

需要导入的模块和显示图片的通用代码：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

cv2.imshow('img', img)
cv2.waitKey(0)
```

![绘制各种几何形状](http://blog.codec.wang/cv2_drawing_functions.jpg)

上图就是本教程绘制的最终效果，下面一步步来看：

### 画线

画直线只需指定起点和终点的坐标就行：

```python
# 创建一副黑色的图片
img = np.zeros((512, 512, 3), np.uint8)
# 画一条线宽为5的蓝色直线，参数2：起点，参数3：终点
cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)
```

> 经验之谈：所有绘图函数均会直接影响原图片，这点要注意。

### 画矩形

画矩形需要知道左上角和右下角的坐标：

```python
# 画一个绿色边框的矩形，参数2：左上角坐标，参数3：右下角坐标
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
```

### 画圆

画圆需要指定圆心和半径，注意下面的例子中线宽=-1代表填充：

```python
# 画一个填充红色的圆，参数2：圆心坐标，参数3：半径
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
```

### 画椭圆

画椭圆需要的参数比较多，请对照后面的代码理解这几个参数：

- 参数2：椭圆中心(x,y)
- 参数3：x/y轴的长度
- 参数4：angle---椭圆的旋转角度
- 参数5：startAngle---椭圆的起始角度
- 参数6：endAngle---椭圆的结束角度

> 经验之谈：OpenCV中原点在左上角，所以这里的角度是以顺时针方向计算的。

```python
# 在图中心画一个填充的半圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)
```

### 画多边形

画多边形需要指定一系列多边形的顶点坐标，相当于从第一个点到第二个点画直线，再从第二个点到第三个点画直线....

OpenCV中需要先将多边形的顶点坐标需要变成顶点数×1×2维的矩阵，再来绘制：

```python
# 定义四个顶点坐标
pts = np.array([[10, 5],  [50, 10], [70, 20], [20, 30]], np.int32)
# 顶点个数：4，矩阵变成4*1*2维
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))
```

`cv2.polylines()`的参数3如果是False的话，多边形就不闭合。

> 经验之谈：如果需要绘制多条直线，使用cv2.polylines()要比cv2.line()高效很多，例如：

```python
# 使用cv2.polylines()画多条直线
line1 = np.array([[100, 20],  [300, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60],  [300, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100],  [300, 100]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [line1, line2, line3], True, (0, 255, 255))
```

### 添加文字

使用`cv2.putText()`添加文字，它的参数也比较多，同样请对照后面的代码理解这几个参数：

- 参数2：要添加的文本
- 参数3：文字的起始坐标（左下角为起点）
- 参数4：字体
- 参数5：文字大小（缩放比例）

```python
# 添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'ex2tron', (10, 500), font,
            4, (255, 255, 255), 2, lineType=cv2.LINE_AA)
```

字体可参考：[HersheyFonts](https://docs.opencv.org/4.0.0/d6/d6e/group__imgproc__draw.html#ga0f9314ea6e35f99bb23f29567fc16e11)。另外，这里有个线型lineType参数，LINE_AA表示抗锯齿线型，具体可见[LineTypes](https://docs.opencv.org/3.3.1/d0/de1/group__core.html#gaf076ef45de481ac96e0ab3dc2c29a777)

## 小结

- `cv2.line()`画直线，`cv2.circle()`画圆，`cv2.rectangle()`画矩形，`cv2.ellipse()`画椭圆，`cv2.polylines()`画多边形，`cv2.putText()`添加文字。
- 画多条直线时，`cv2.polylines()`要比`cv2.line()`高效很多。

## 练习

1. 你能用已学的绘图功能画出OpenCV的logo吗？(提示：椭圆和圆)

![OpenCV logo](http://blog.codec.wang/cv2_draw_opencv_logo.jpg)

## 接口文档

- [cv2.line()](https://docs.opencv.org/4.0.0/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2)
- [cv2.circle()](https://docs.opencv.org/4.0.0/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670)
- [cv2.rectangle()](https://docs.opencv.org/4.0.0/d6/d6e/group__imgproc__draw.html#ga07d2f74cadcf8e305e810ce8eed13bc9)
- [cv2.ellipse()](https://docs.opencv.org/4.0.0/d6/d6e/group__imgproc__draw.html#ga28b2267d35786f5f890ca167236cbc69)
- [cv2.putText()](https://docs.opencv.org/4.0.0/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576)
- [cv2.polylines()](https://docs.opencv.org/4.0.0/d6/d6e/group__imgproc__draw.html#ga1ea127ffbbb7e0bfc4fd6fd2eb64263c)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/08.%20%E7%BB%98%E5%9B%BE%E5%8A%9F%E8%83%BD)
- [LineTypes](https://docs.opencv.org/3.3.1/d0/de1/group__core.html#gaf076ef45de481ac96e0ab3dc2c29a777)
- [Drawing Functions in OpenCV](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html)