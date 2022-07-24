# 05: 颜色空间转换

![](http://cos.codec.wang/cv2_exercise_tracking_three_colors.jpg)

学习如何进行图片的颜色空间转换，视频中追踪特定颜色的物体。图片等可到文末引用处下载。

## 目标

- 颜色空间转换，如 BGR↔Gray，BGR↔HSV 等
- 追踪视频中特定颜色的物体
- OpenCV 函数：`cv2.cvtColor()`, `cv2.inRange()`

## 教程

### 颜色空间转换

```python
import cv2

img = cv2.imread('lena.jpg')
# 转换为灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)
```

`cv2.cvtColor()`用来进行颜色模型转换，参数 1 是要转换的图片，参数 2 是转换模式， `COLOR_BGR2GRAY`表示 BGR→Gray，可用下面的代码显示所有的转换模式：

```python
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
```

:::tip
颜色转换其实是数学运算，如灰度化最常用的是：`gray=R*0.299+G*0.587+B*0.114`。
:::

### 视频中特定颜色物体追踪

[HSV](https://baike.baidu.com/item/HSV/547122)是一个常用于颜色识别的模型，相比 BGR 更易区分颜色，转换模式用`COLOR_BGR2HSV`表示。

:::tip
OpenCV 中色调 H 范围为\[0,179\]，饱和度 S 是\[0,255\]，明度 V 是\[0,255\]。虽然 H 的理论数值是 0°~360°，但 8 位图像像素点的最大值是 255，所以 OpenCV 中除以了 2，某些软件可能使用不同的尺度表示，所以同其他软件混用时，记得归一化。
:::

现在，我们实现一个使用 HSV 来只显示视频中蓝色物体的例子，步骤如下：

1. 捕获视频中的一帧
2. 从 BGR 转换到 HSV
3. 提取蓝色范围的物体
4. 只显示蓝色物体

![](http://cos.codec.wang/cv2_blue_object_tracking.jpg)

```python
import numpy as np

capture = cv2.VideoCapture(0)

# 蓝色的范围，不同光照条件下不一样，可灵活调整
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

while(True):
    # 1.捕获视频中的一帧
    ret, frame = capture.read()

    # 2.从 BGR 转换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 3.inRange()：介于 lower/upper 之间的为白色，其余黑色
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 4.只保留原图中的蓝色部分
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q'):
        break
```

其中，`bitwise_and()`函数暂时不用管，后面会讲到。那蓝色的 HSV 值的上下限 lower 和 upper 范围是怎么得到的呢？其实很简单，我们先把标准蓝色的 BGR 值用`cvtColor()`转换下：

```python
blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)  # [[[120 255 255]]]
```

结果是\[120, 255, 255\]，所以，我们把蓝色的范围调整成了上面代码那样。

:::tip
[Lab](https://baike.baidu.com/item/Lab/1514615) 颜色空间也经常用来做颜色识别，有兴趣的同学可以了解下。
:::

## 小结

- `cv2.cvtColor()`函数用来进行颜色空间转换，常用 BGR↔Gray，BGR↔HSV。
- HSV 颜色模型常用于颜色识别。要想知道某种颜色在 HSV 下的值，可以将它的 BGR 值用`cvtColor()`转换得到。

## 练习

1. 尝试在视频中同时提取红色、蓝色、绿色的物体。（效果如下）

![](http://cos.codec.wang/cv2_exercise_tracking_three_colors.jpg)

## 接口文档

- [cv2.cvtColor\(\)](https://docs.opencv.org/4.0.0/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab)
- [cv2.inRange\(\)](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga48af0ab51e36436c5d04340e036ce981)
- [cv2.bitwise_and\(\)](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14)

## 引用

- [本节源码](https://github.com/codecwang/OpenCV-Python-Tutorial/tree/master/05-Changing-Colorspaces)
- [Changing Colorspaces](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html)
