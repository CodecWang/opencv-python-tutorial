# [OpenCV-Python教程番外篇9：图像梯度](http://ex2tron.wang/opencv-python-extra-image-gradients/)

![](http://blog.codec.wang/cv2_horizen_vertical_edge_detection.jpg)

了解图像梯度和边缘检测的相关概念。<!-- more -->图片等可到[源码处](#引用)下载。

还记得前面[平滑图像](/opencv-python-smoothing-images/)中提到的滤波与模糊的区别吗？我们说低通滤波器是模糊，高通滤波器是锐化，这节我们就来看看高通滤波器。

---

## [图像梯度](https://baike.baidu.com/item/图像梯度/8528837?fr=aladdin)

如果你还记得高数中用一阶导数来求极值的话，就很容易理解了：把图片想象成连续函数，因为边缘部分的像素值是与旁边像素明显有区别的，所以对图片局部求极值，就可以得到整幅图片的边缘信息了。不过图片是二维的离散函数，导数就变成了差分，这个差分就称为图像的梯度。

当然，大部分人应该是早忘记高数了(￣▽￣)"，所以看不懂的话，就把上面的解释划掉，我们重新从卷积的角度来看看。

### 垂直边缘提取

滤波是应用卷积来实现的，卷积的关键就是卷积核，我们来考察下面这个卷积核：

$$
k1 = \left[
 \begin{matrix}
   -1 & 0 & 1 \newline
   -2 & 0 & 2 \newline
   -1 & 0 & 1
  \end{matrix}
  \right]
$$

这个核是用来提取图片中的垂直边缘的，怎么做到的呢？看下图：

![](http://blog.codec.wang/cv2_understand_sobel_edge_detection.jpg)

当前列左右两侧的元素进行差分，由于边缘的值明显小于（或大于）周边像素，所以边缘的差分结果会明显不同，这样就提取出了垂直边缘。同理，把上面那个矩阵转置一下，就是提取水平边缘。这种差分操作就称为图像的梯度计算：

$$
k2 = \left[
 \begin{matrix}
   -1 & -2 & -1 \newline
   0 & 0 & 0 \newline
   1 & 2 & 1
  \end{matrix}
  \right]
$$

![垂直和水平边缘提取](http://blog.codec.wang/cv2_horizen_vertical_edge_detection.jpg)

> 还记得滤波函数`cv2.filter2D()`吗？（[番外篇：卷积基础](/opencv-python-extra-padding-and-convolution/)）我们来手动实现上面的功能：

```python
img = cv2.imread('sudoku.jpg', 0)

# 自己进行垂直边缘提取
kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)
dst_v = cv2.filter2D(img, -1, kernel)
# 自己进行水平边缘提取
dst_h = cv2.filter2D(img, -1, kernel.T)
# 横向并排对比显示
cv2.imshow('edge', np.hstack((img, dst_v, dst_h)))
cv2.waitKey(0)
```

### Sobel算子

上面的这种差分方法就叫[Sobel算子](https://baike.baidu.com/item/Sobel%E7%AE%97%E5%AD%90/11000092?fr=aladdin)，它先在垂直方向计算梯度$ G_x=k_1×src $，再在水平方向计算梯度$ G_y=k_2×src $，最后求出总梯度：\\(G=\sqrt{Gx^2+Gy^2}\\)

我们可以把前面的代码用Sobel算子更简单地实现：

```python
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)  # 只计算x方向
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)  # 只计算y方向
```

> 经验之谈：很多人疑问，Sobel算子的卷积核这几个值是怎么来的呢？事实上，并没有规定，你可以用你自己的。

比如，最初只利用领域间的原始差值来检测边缘的[Prewitt算子](https://baike.baidu.com/item/Prewitt%E7%AE%97%E5%AD%90/8415245?fr=aladdin)：

$$
K = \left[
 \begin{matrix}
   -1 & 0 & 1 \newline
   -1 & 0 & 1 \newline
   -1 & 0 & 1
  \end{matrix}
  \right]
$$

还有比Sobel更好用的**Scharr算子**，大家可以了解下：

$$
K = \left[
 \begin{matrix}
   -3 & 0 & 3 \newline
   -10 & 0 & 10 \newline
   -3 & 0 & 3
  \end{matrix}
  \right]
$$

这些算法都是一阶边缘检测的代表，网上也有算子之间的对比资料，有兴趣的可参考[引用](#引用)。

### [Laplacian算子]((https://baike.baidu.com/item/Laplacian%E7%AE%97%E5%AD%90)

高数中用一阶导数求极值，在这些极值的地方，二阶导数为0，所以也可以通过求二阶导计算梯度：$ dst=\frac{\partial^2 f}{\partial x^2}+\frac{\partial^2 f}{\partial y^2} $

一维的一阶和二阶差分公式分别为：
$$
\frac{\partial f}{\partial x}=f(x+1)-f(x)
$$

$$
\frac{\partial^2 f}{\partial x^2}=f(x+1)+f(x-1)-2f(x)
$$

提取前面的系数，那么一维的Laplacian滤波核是：
$$
K=\left[
 \begin{matrix}
   1 & -2 & 1
  \end{matrix}
  \right]
$$
而对于二维函数f(x,y)，两个方向的二阶差分分别是：

$$
\frac{\partial^2 f}{\partial x^2}=f(x+1,y)+f(x-1,y)-2f(x,y)
$$

$$
\frac{\partial^2 f}{\partial y^2}=f(x,y+1)+f(x,y-1)-2f(x,y)
$$

合在一起就是：

$$
\triangledown^2 f(x,y)=f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)-4f(x,y)
$$

同样提取前面的系数，那么二维的Laplacian滤波核就是：

$$
K = \left[
 \begin{matrix}
   0 & 1 & 0 \newline
   1 & -4 & 1 \newline
   0 & 1 & 0
  \end{matrix}
  \right]
$$

这就是Laplacian算子的图像卷积模板，有些资料中在此基础上考虑斜对角情况，将卷积核拓展为：

$$
K = \left[
 \begin{matrix}
   1 & 1 & 1 \newline
   1 & -8 & 1 \newline
   1 & 1 & 1
  \end{matrix}
  \right]
$$

OpenCV中直接使用`cv2.Laplacian()`函数：

```python
laplacian = cv2.Laplacian(img, -1)  # 使用Laplacian算子
```

![](http://blog.codec.wang/cv2_laplacian.jpg)

Laplacian算子是二阶边缘检测的典型代表，一/二阶边缘检测各有优缺点，大家可自行了解。

## 练习

1. （选做）同志们有空补补高数~~姿势~~（知识）呗！(✿◕‿◕✿)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E7%95%AA%E5%A4%96%E7%AF%8709.%20%E5%9B%BE%E5%83%8F%E6%A2%AF%E5%BA%A6)
- [Image Gradients](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html)
- [Sobel导数](http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/imgproc/imgtrans/sobel_derivatives/sobel_derivatives.html#sobel-derivatives)
- [维基百科：边缘检测](https://zh.wikipedia.org/wiki/%E8%BE%B9%E7%BC%98%E6%A3%80%E6%B5%8B)
- [数字图像 - 边缘检测原理 - Sobel, Laplace, Canny算子](https://www.jianshu.com/p/2334bee37de5)