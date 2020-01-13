# [OpenCV-Python教程番外篇11：凸包及更多轮廓特征](http://ex2tron.wang/opencv-python-extra-convex-hull/)

![](http://blog.codec.wang/cv2_understand_convex.jpg)

计算凸包及更多轮廓特征。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 多边形逼近

前面我们学习过最小外接矩和最小外接圆，那么可以用一个最小的多边形包围物体吗？当然可以：

 ```python
import cv2
import numpy as np

# 1.先找到轮廓
img = cv2.imread('unregular.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
cnt = contours[0]

# 2.进行多边形逼近，得到多边形的角点
approx = cv2.approxPolyDP(cnt, 3, True)

# 3.画出多边形
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [approx], True, (0, 255, 0), 2)
 ```

其中`cv2.approxPolyDP()`的参数2(epsilon)是一个距离值，表示多边形的轮廓接近实际轮廓的程度，值越小，越精确；参数3表示是否闭合。

![](http://blog.codec.wang/cv2_understand_approxpoly.jpg)

## 凸包

[凸包](https://baike.baidu.com/item/%E5%87%B8%E5%8C%85/179150?fr=aladdin)跟多边形逼近很像，只不过它是物体最外层的"凸"多边形：集合A内连接任意两个点的直线都在A的内部，则称集合A是凸形的。如下图，红色的部分为手掌的凸包，双箭头部分表示凸缺陷(Convexity Defects)，凸缺陷常用来进行手势识别等：

![](http://blog.codec.wang/cv2_understand_convex.jpg)

```python
# 1.先找到轮廓
img = cv2.imread('convex.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
cnt = contours[0]

# 2.寻找凸包，得到凸包的角点
hull = cv2.convexHull(cnt)

# 3.绘制凸包
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)
```

![](http://blog.codec.wang/cv2_convex_hull.jpg)

其中函数`cv2.convexHull()`有个可选参数returnPoints，默认是True，代表返回角点的x/y坐标；如果为False的话，表示返回轮廓中是凸包角点的索引，比如说：

```python
print(hull[0])  # [[362 184]]（坐标）
hull2 = cv2.convexHull(cnt, returnPoints=False)
print(hull2[0])  # [510]（cnt中的索引）
print(cnt[510])  # [[362 184]]
```

当使用`cv2.convexityDefects()`计算凸包缺陷时，returnPoints需为False，详情可参考：[Convexity Defects](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html#contours-more-functions)

另外可以用下面的语句来判断轮廓是否是凸形的：

```python
print(cv2.isContourConvex(hull))  # True
```

## 点到轮廓距离

`cv2.pointPolygonTest()`函数计算点到轮廓的最短距离（也就是垂线），又称多边形测试：

```python
dist = cv2.pointPolygonTest(cnt, (100, 100), True)  # -3.53
```

其中参数3为True时表示计算距离值：点在轮廓外面值为负，点在轮廓上值为0，点在轮廓里面值为正；参数3为False时，只返回-1/0/1表示点相对轮廓的位置，不计算距离。

更多轮廓特征，如当量直径、平均强度等，我目前也没用到过，以后用到再写吧，感兴趣的可以参看：[Contour Properties](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_properties/py_contour_properties.html)、[Contours Hierarchy](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_hierarchy/py_contours_hierarchy.html)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E7%95%AA%E5%A4%96%E7%AF%8711.%20%E5%87%B8%E5%8C%85%E5%8F%8A%E6%9B%B4%E5%A4%9A%E8%BD%AE%E5%BB%93%E7%89%B9%E5%BE%81)
- [Convexity Defects](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html#contours-more-functions)
- [Contour Properties](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_properties/py_contour_properties.html)
- [Contours Hierarchy](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_hierarchy/py_contours_hierarchy.html)