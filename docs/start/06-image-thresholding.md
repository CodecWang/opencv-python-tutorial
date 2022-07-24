# 06: 阈值分割

![](http://cos.codec.wang/cv2_threshold_binary_demo.jpg)

学习使用不同的阈值方法"二值化"图像。图片等可到文末引用处下载。

## 目标

- 使用固定阈值、自适应阈值和 Otsu 阈值法"二值化"图像
- OpenCV 函数：`cv2.threshold()`, `cv2.adaptiveThreshold()`

## 教程

### 固定阈值分割

固定阈值分割很直接，一句话说就是像素点值大于阈值变成一类值，小于阈值变成另一类值。

![](http://cos.codec.wang/cv2_threshold_binary_demo.jpg)

```python
import cv2

# 灰度图读入
img = cv2.imread('gradient.jpg', 0)

# 阈值分割
ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', th)
cv2.waitKey(0)
```

`cv2.threshold()`用来实现阈值分割，ret 代表当前的阈值，暂时不用理会。函数有 4 个参数：

- 参数 1：要处理的原图，**一般是灰度图**
- 参数 2：设定的阈值
- 参数 3：对于`THRESH_BINARY`、`THRESH_BINARY_INV`阈值方法所选用的最大阈值，一般为 255
- 参数 4：阈值的方式，主要有 5 种，详情：[ThresholdTypes](https://docs.opencv.org/4.0.0/d7/d1b/group__imgproc__misc.html#gaa9e58d2860d4afa658ef70a9b1115576)

下面结合代码理解下这 5 种阈值方式：

```python
import matplotlib.pyplot as plt

# 应用 5 种不同的阈值方法
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

# 使用 Matplotlib 显示
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴

plt.show()
```

![5 种不同的阈值方式结果](http://cos.codec.wang/cv2_different_threshold_demo.jpg)

:::tip
很多人误以为阈值分割就是 [二值化](https://baike.baidu.com/item/%E4%BA%8C%E5%80%BC%E5%8C%96)。从上图中可以发现，两者并不等同，阈值分割结果是两类值，而不是两个值，所以教程开头我把二值化加了引号。
:::

![](http://cos.codec.wang/cv2_different_thresholds_theory.jpg)

### 自适应阈值

看得出来固定阈值是在整幅图片上应用一个阈值进行分割，_它并不适用于明暗分布不均的图片_。 `cv2.adaptiveThreshold()`自适应阈值会每次取图片的一小部分计算阈值，这样图片不同区域的阈值就不尽相同。它有 5 个参数，其实很好理解，先看下效果：

```python
# 自适应阈值对比固定阈值
img = cv2.imread('sudoku.jpg', 0)

# 固定阈值
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 自适应阈值
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)

titles = ['Original', 'Global(v = 127)', 'Adaptive Mean', 'Adaptive Gaussian']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()
```

![自适应阈值对比固定阈值](http://cos.codec.wang/cv2_adaptive_vs_global_thresholding.jpg)

- 参数 1：要处理的原图
- 参数 2：最大阈值，一般为 255
- 参数 3：小区域阈值的计算方式
  - `ADAPTIVE_THRESH_MEAN_C`：小区域内取均值
  - `ADAPTIVE_THRESH_GAUSSIAN_C`：小区域内加权求和，权重是个高斯核
- 参数 4：阈值方法，只能使用`THRESH_BINARY`、`THRESH_BINARY_INV`，具体见前面所讲的阈值方法
- 参数 5：小区域的面积，如 11 就是 11\*11 的小块
- 参数 6：最终阈值等于小区域计算出的阈值再减去此值

如果你没看懂上面的参数也不要紧，暂时会用就行，当然我建议你调整下参数看看不同的结果。

### Otsu 阈值

在前面固定阈值中，我们是随便选了一个阈值如 127，那如何知道我们选的这个阈值效果好不好呢？答案是：不断尝试，所以这种方法在很多文献中都被称为经验阈值。[Otsu 阈值法](https://baike.baidu.com/item/otsu/16252828)就提供了一种自动高效的二值化方法，不过我们直方图还没学，这里暂时略过。

好吧，我知道我激起了你的兴趣，~ o\(_￣ ▽ ￣_\)o，有能力的童鞋可以看下[练习题](#练习)。

## 小结

- `cv2.threshold()`用来进行固定阈值分割。固定阈值不适用于光线不均匀的图片，所以用 `cv2.adaptiveThreshold()`进行自适应阈值分割。
- 二值化跟阈值分割并不等同。针对不同的图片，可以采用不同的阈值方法。

## 练习

1. Otsu 阈值是一种高效的二值化算法，请阅读[番外篇：Otsu 阈值法](./extra-04-otsu-thresholding/)。

## 接口文档

- [cv2.threshold\(\)](https://docs.opencv.org/4.0.0/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57)
- [cv2.adaptiveThreshold\(\)](https://docs.opencv.org/4.0.0/d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3)
- [cv2.ThresholdTypes\(\)](https://docs.opencv.org/4.0.0/d7/d1b/group__imgproc__misc.html#gaa9e58d2860d4afa658ef70a9b1115576)

## 引用

- [本节源码](https://github.com/codecwang/OpenCV-Python-Tutorial/tree/master/06-Image-Thresholding)
- [Image Thresholding](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html)
