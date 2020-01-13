# [OpenCV-Python教程番外篇8：卷积基础(图片边框)](http://ex2tron.wang/opencv-python-extra-padding-and-convolution/)

![](http://blog.codec.wang/cv2_understand_padding.jpg)

了解卷积/滤波的基础知识，给图片添加边框。<!-- more -->如果你已了解相关理论，请直接跳到[添加边框](#添加边框)部分。

卷积的概念其实很好理解，下面我就给大家做个最简单的解释，绝对轻松加愉快的辣o(*￣▽￣*)o

---

## 卷积

什么是二维卷积呢？看下面一张图就一目了然：

![](http://blog.codec.wang/cv2_understand_convolution.jpg)

卷积就是循环对**图像跟一个核逐个元素相乘再求和得到另外一副图像的操作**，比如结果图中第一个元素5是怎么算的呢？原图中3×3的区域与3×3的核逐个元素相乘再相加：
$$
5=1\times1+2\times0+1\times0+0\times0+1\times0+1\times0+3\times0+0\times0+2\times2
$$
算完之后，整个框再往右移一步继续计算，横向计算完后，再往下移一步继续计算……网上有一副很经典的动态图，方便我们理解卷积：

![](http://blog.codec.wang/cv2_understand_cnn.gif)

## padding

不难发现，前面我们用3×3的核对一副6×6的图像进行卷积，得到的是4×4的图，图片缩小了！那怎么办呢？我们可以**把原图扩充一圈，再卷积，这个操作叫填充padding**。

> 事实上，原图为n×n，卷积核为f×f，最终结果图大小为(n-f+1) × (n-f+1)。

![](http://blog.codec.wang/cv2_understand_padding.jpg)

那么扩展的这一层应该填充什么值呢？OpenCV中有好几种填充方式，都使用`cv2.copyMakeBorder()`函数实现，一起来看看。

## 添加边框

`cv2.copyMakeBorder()`用来给图片添加边框，它有下面几个参数：

- src：要处理的原图
- top, bottom, left, right：上下左右要扩展的像素数
- **borderType**：边框类型，这个就是需要关注的填充方式，详情请参考：[BorderTypes](https://docs.opencv.org/3.3.1/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5)

其中默认方式和固定值方式最常用，我们详细说明一下：

### 固定值填充

顾名思义，`cv2.BORDER_CONSTANT`这种方式就是边框都填充成一个固定的值，比如下面的程序都填充0：

```python
img = cv2.imread('6_by_6.bmp', 0)
print(img)

# 固定值边框，统一都填充0也称为zero padding
cons = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
print(cons)
```

![](http://blog.codec.wang/cv2_zero_padding_output.jpg)

### 默认边框类型

默认边框`cv2.BORDER_DEFAULT`其实是取镜像对称的像素填充，比较拗口，一步步解释：

```python
default = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
print(default)
```

首先进行上下填充，填充成与原图像边界对称的值，如下图：

![](http://blog.codec.wang/cv2_up_down_padding_first.jpg)

同理再进行左右两边的填充，最后把四个顶点补充上就好了：

![](http://blog.codec.wang/cv2_right_left_padding_second2.jpg)

> 经验之谈：一般情况下默认方式更加合理，因为边界的像素值更加接近。具体应视场合而定。

## OpenCV进行卷积

OpenCV中用`cv2.filter2D()`实现卷积操作，比如我们的核是下面这样（3×3区域像素的和除以10）：

$$
M = \frac{1}{10}\left[
 \begin{matrix}
   1 & 1 & 1 \newline
   1 & 1 & 1 \newline
   1 & 1 & 1
  \end{matrix}
  \right] \tag{3}
$$

```python
img = cv2.imread('lena.jpg')
# 定义卷积核
kernel = np.ones((3, 3), np.float32) / 10
# 卷积操作，-1表示通道数与原图相同
dst = cv2.filter2D(img, -1, kernel)
```

![](http://blog.codec.wang/cv2_convolution_kernel_3_3.jpg)

可以看到这个核对图像进行了模糊处理，这是卷积的众多功能之一。当然卷积还有很多知识没有学到，后面我们再继续深入。

## 练习

1. 尝试给"lena.jpg"添加几种不同的边框类型，对比下效果。

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E7%95%AA%E5%A4%96%E7%AF%8708.%20%E5%8D%B7%E7%A7%AF%E5%9F%BA%E7%A1%80(%E5%9B%BE%E7%89%87%E8%BE%B9%E6%A1%86)
- [Basic Operations on Images](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html)
- [图像卷积与滤波的一些知识点](http://blog.csdn.net/zouxy09/article/details/49080029)