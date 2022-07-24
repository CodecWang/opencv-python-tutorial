# 11: 边缘检测

![](http://cos.codec.wang/cv2_canny_edge_detection_threshold.jpg)

学习使用 Canny 获取图像的边缘。图片等可到文末引用处下载。

> [Canny J . A Computational Approach To Edge Detection\[J\]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 1986, PAMI-8\(6\):679-698.](https://www.computer.org/cms/Computer.org/Transactions%20Home%20Pages/TPAMI/PDFs/top_ten_6.pdf)

## 目标

- Canny 边缘检测的简单概念
- OpenCV 函数：`cv2.Canny()`

## 教程

Canny 边缘检测方法常被誉为边缘检测的最优方法，废话不多说，先看个例子：

```python
import cv2
import numpy as np

img = cv2.imread('handwriting.jpg', 0)
edges = cv2.Canny(img, 30, 70)  # canny 边缘检测

cv2.imshow('canny', np.hstack((img, edges)))
cv2.waitKey(0)
```

![](http://cos.codec.wang/cv2_canny_edge_detection.jpg)

`cv2.Canny()`进行边缘检测，参数 2、3 表示最低、高阈值，下面来解释下具体原理。

:::tip
之前我们用低通滤波的方式模糊了图片，那反过来，想得到物体的边缘，就需要用到高通滤波。推荐先阅读：[番外篇：图像梯度](./extra-09-image-gradients/)。
:::

### Canny 边缘检测

Canny 边缘提取的具体步骤如下：

1，使用 5×5 高斯滤波消除噪声：

边缘检测本身属于锐化操作，对噪点比较敏感，所以需要进行平滑处理。高斯滤波的具体内容参考前一篇：[平滑图像](./smoothing-images)

$$
K=\frac{1}{256}\left[
 \begin{matrix}
   1 & 4 & 6 & 4 & 1 \newline
   4 & 16 & 24 & 16 & 4  \newline
   6 & 24 & 36 & 24 & 6  \newline
   4 & 16 & 24 & 16 & 4  \newline
   1 & 4 & 6 & 4 & 1
  \end{matrix}
  \right]
$$

2，计算图像梯度的方向：

首先使用 Sobel 算子计算两个方向上的梯度$G_x$和$G_y$，然后算出梯度的方向：

$$
\theta=\arctan(\frac{G_y}{G_x})
$$

保留这四个方向的梯度：0°/45°/90°/135°，有什么用呢？我们接着看。

3，取局部极大值：

梯度其实已经表示了轮廓，但为了进一步筛选，可以在上面的四个角度方向上再取局部极大值：

![](http://cos.codec.wang/cv2_understand_canny_direction.jpg)

比如，A 点在 45° 方向上大于 B/C 点，那就保留它，把 B/C 设置为 0。

4，滞后阈值：

经过前面三步，就只剩下 0 和可能的边缘梯度值了，为了最终确定下来，需要设定高低阈值：

![](http://cos.codec.wang/cv2_understand_canny_max_min_val.jpg)

- 像素点的值大于最高阈值，那肯定是边缘（上图 A）
- 同理像素值小于最低阈值，那肯定不是边缘
- 像素值介于两者之间，如果与高于最高阈值的点连接，也算边缘，所以上图中 C 算，B 不算

Canny 推荐的高低阈值比在 2:1 到 3:1 之间。

### 先阈值分割后检测

其实很多情况下，阈值分割后再检测边缘，效果会更好：

```python
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30, 70)

cv2.imshow('canny', np.hstack((img, thresh, edges)))
cv2.waitKey(0)
```

代码中我用了[番外篇：Otsu 阈值法](../start/extra-04-otsu-thresholding/)中的自动阈值分割，如果你不太了解，大可以使用传统的方法，不过如果是下面这种图片，推荐用 Otsu 阈值法。另外 Python 中某个值不用的话，就写个下划线'\_'。

![](http://cos.codec.wang/cv2_canny_edge_detection_threshold.jpg)

## 练习

1. （选做）如果你不太理解高低阈值的效果，创建两个滑动条来调节它们的值看看：

![](http://cos.codec.wang/cv2_trackbar_maxval_minval_canny.gif)

## 小结

- Canny 是用的最多的边缘检测算法，用`cv2.Canny()`实现。

## 接口文档

- [cv2.Canny()](https://docs.opencv.org/4.0.0/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de)

## 引用

- [本节源码](https://github.com/codecwang/OpenCV-Python-Tutorial/tree/master/11-Edge-Detection)
- [Canny Edge Detection](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html)
- [Canny 边缘检测](http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html)
- [Canny J . A Computational Approach To Edge Detection\[J\]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 1986, PAMI-8\(6\):679-698.](https://www.computer.org/cms/Computer.org/Transactions%20Home%20Pages/TPAMI/PDFs/top_ten_6.pdf)
