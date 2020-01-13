# [OpenCV-Python教程16：模板匹配](http://ex2tron.wang/opencv-python-template-matching/)

![](http://blog.codec.wang/cv2_understand_template_matching.jpg)

学习使用模板匹配在图像中寻找物体。<!-- more -->图片等可到[源码处](#引用)下载。

------

## 目标

- 使用模板匹配在图像中寻找物体
- OpenCV函数：`cv2.matchTemplate()`, `cv2.minMaxLoc()`

## 教程

### 模板匹配

[模板匹配](https://baike.baidu.com/item/模板匹配)就是用来在大图中找小图，也就是说在一副图像中寻找另外一张模板图像的位置：

![](http://blog.codec.wang/cv2_understand_template_matching.jpg)

用`cv2.matchTemplate()`实现模板匹配。首先我们来读入图片和模板：

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', 0)
template = cv2.imread('face.jpg', 0)
h, w = template.shape[:2]  # rows->h, cols->w
```

匹配函数返回的是一副灰度图，最白的地方表示最大的匹配。使用`cv2.minMaxLoc()`函数可以得到最大匹配值的坐标，以这个点为左上角角点，模板的宽和高画矩形就是匹配的位置了：

```python
# 相关系数匹配方法：cv2.TM_CCOEFF
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

left_top = max_loc  # 左上角
right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
cv2.rectangle(img, left_top, right_bottom, 255, 2)  # 画出矩形位置
```

![](http://blog.codec.wang/cv2_ccoeff_matching_template.jpg)

### 原理

> 这部分可看可不看，不太理解也没关系，还记得前面的方法吗？不懂得就划掉(✿◕‿◕✿)

模板匹配的原理其实很简单，就是不断地在原图中移动模板图像去比较，有6种不同的比较方法，详情可参考：[TemplateMatchModes](https://docs.opencv.org/3.3.1/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d)

- 平方差匹配CV_TM_SQDIFF：用两者的平方差来匹配，最好的匹配值为0
- 归一化平方差匹配CV_TM_SQDIFF_NORMED
- 相关匹配CV_TM_CCORR：用两者的乘积匹配，数值越大表明匹配程度越好
- 归一化相关匹配CV_TM_CCORR_NORMED
- 相关系数匹配CV_TM_CCOEFF：用两者的相关系数匹配，1表示完美的匹配，-1表示最差的匹配
- 归一化相关系数匹配CV_TM_CCOEFF_NORMED

归一化的意思就是将值统一到0~1，这些方法的对比代码可到[源码处](#引用)查看。模板匹配也是应用卷积来实现的：假设原图大小为W×H，模板图大小为w×h，那么生成图大小是(W-w+1)×(H-h+1)，生成图中的每个像素值表示原图与模板的匹配程度。

### 匹配多个物体

前面我们是找最大匹配的点，所以只能匹配一次。我们可以设定一个匹配阈值来匹配多次：

```python
# 1.读入原图和模板
img_rgb = cv2.imread('mario.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('mario_coin.jpg', 0)
h, w = template.shape[:2]

# 2.标准相关模板匹配
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8 

# 3.这边是Python/Numpy的知识，后面解释
loc = np.where(res >= threshold)  # 匹配程度大于%80的坐标y,x
for pt in zip(*loc[::-1]):  # *号表示可选参数
    right_bottom = (pt[0] + w, pt[1] + h)
    cv2.rectangle(img_rgb, pt, right_bottom, (0, 0, 255), 2)
```

![](http://blog.codec.wang/cv2_template_matching_multi.jpg)

第3步有几个Python/Numpy的重要知识，来大致看下：

- [np.where()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html)在这里返回res中值大于0.8的所有坐标，如：

```python
x = np.arange(9.).reshape(3, 3)
print(np.where(x > 5))
# 结果(先y坐标，再x坐标)：(array([2, 2, 2]), array([0, 1, 2]))
```

![](http://blog.codec.wang/cv2_np_where_function.jpg)

- [zip()](https://docs.python.org/3/library/functions.html#zip)函数，功能强大到难以解释，举个简单例子就知道了：

```python
x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))  # [(1, 4), (2, 5), (3, 6)]
```

这样大家就能理解前面代码的用法了吧：因为loc是先y坐标再x坐标，所以用loc[::-1]翻转一下，然后再用zip函数拼接在一起。

## 练习

1. 之前我们有学过形状匹配，不论形状旋转/缩放都可以匹配到。思考一下，图片旋转或缩放的话模板匹配还有作用吗？

## 小结

- 模板匹配用来在大图中找小图。
- `cv2.matchTemplate()`用来进行模板匹配。

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/16.%20%E6%A8%A1%E6%9D%BF%E5%8C%B9%E9%85%8D)
- [Template Matching](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html)
- [模板匹配](http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/imgproc/histograms/template_matching/template_matching.html#template-matching)
- [TemplateMatchModes](https://docs.opencv.org/3.3.1/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d)