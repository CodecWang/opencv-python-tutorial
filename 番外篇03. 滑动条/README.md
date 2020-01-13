# [OpenCV-Python教程番外篇3：滑动条](http://ex2tron.wang/opencv-python-extra-trackbar/)

![](http://blog.codec.wang/cv2_track_bar_rgb.jpg)

学习使用滑动条动态调整参数。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 滑动条的使用

首先我们需要创建一个滑动条，如`cv2.createTrackbar('R','image',0,255,call_back)`，其中

- 参数1：滑动条的名称
- 参数2：所在窗口的名称
- 参数3：当前的值
- 参数4：最大值
- 参数5：回调函数名称，回调函数默认有一个表示当前值的参数

创建好之后，可以在回调函数中获取滑动条的值，也可以用：`cv2.getTrackbarPos()`得到，其中，参数1是滑动条的名称，参数2是窗口的名称。

## RGB调色板

下面我们实现一个RGB的调色板，理解下滑动条的用法：

```python
import cv2
import numpy as np

# 回调函数，x表示滑块的位置，本例暂不使用
def nothing(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# 创建RGB三个滑动条
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break

    # 获取滑块的值
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    # 设定img的颜色
    img[:] = [b, g, r]
```

![](http://blog.codec.wang/cv2_track_bar_rgb.jpg)

## 小结

- `cv2.createTrackbar()`用来创建滑动条，可以在回调函数中或使用`cv2.getTrackbarPos()`得到滑块的位置

## 接口文档

- [cv2.createTrackbar()](https://docs.opencv.org/4.0.0/d7/dfc/group__highgui.html#gaf78d2155d30b728fc413803745b67a9b)
- [cv2.getTrackbarPos()](https://docs.opencv.org/4.0.0/d7/dfc/group__highgui.html#ga122632e9e91b9ec06943472c55d9cda8)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E7%95%AA%E5%A4%96%E7%AF%8703.%20%E6%BB%91%E5%8A%A8%E6%9D%A1)
- [Trackbar as the Color Palette](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html)