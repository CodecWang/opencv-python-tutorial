# [OpenCV-Python教程09：图像混合](http://ex2tron.wang/opencv-python-image-blending/)

![](http://blog.codec.wang/cv2_image_blending_6_4.jpg)

学习图片间的数学运算，图像混合。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 目标

- 图片间的数学运算，如相加、按位运算等
- OpenCV函数：`cv2.add()`, `cv2.addWeighted()`, `cv2.bitwise_and()`

## 教程

> 首先恭喜你已经完成了入门篇的学习噢，接下来我们学习一些OpenCV的基础内容，加油(ง •_•)ง

### 图片相加

要叠加两张图片，可以用`cv2.add()`函数，相加两幅图片的形状（高度/宽度/通道数）必须相同。numpy中可以直接用res = img + img1相加，但这两者的结果并不相同：

```python
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))  # 250+10 = 260 => 255
print(x + y)  # 250+10 = 260 % 256 = 4
```

如果是二值化图片（只有0和255两种值），两者结果是一样的（用numpy的方式更简便一些）。

### 图像混合

图像混合`cv2.addWeighted()`也是一种图片相加的操作，只不过两幅图片的权重不一样，γ相当于一个修正值：

$$
dst = \alpha\times img1+\beta\times img2 + \gamma
$$

```python
img1 = cv2.imread('lena_small.jpg')
img2 = cv2.imread('opencv-logo-white.png')
res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
```

![图像混合](http://blog.codec.wang/cv2_image_blending_6_4.jpg)

> 经验之谈：α和β都等于1时，就相当于图片相加。

### 按位操作

按位操作包括按位与/或/非/异或操作，有什么用途呢？比如说我们要实现下图的效果：

![](http://blog.codec.wang/cv2_bitwise_operations_demo.jpg)

如果将两幅图片直接相加会改变图片的颜色，如果用图像混合，则会改变图片的透明度，所以我们需要用按位操作。首先来了解一下[掩膜](https://baike.baidu.com/item/%E6%8E%A9%E8%86%9C/8544392?fr=aladdin)（mask）的概念：掩膜是用一副二值化图片对另外一幅图片进行局部的遮挡，看下图就一目了然了：

![掩膜概念](http://blog.codec.wang/cv2_understand_mask.jpg)

所以我们的思路就是把原图中要放logo的区域抠出来，再把logo放进去就行了：

```python
img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('opencv-logo-white.png')

# 把logo放在左上角，所以我们只关心这一块区域
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]

# 创建掩膜
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 保留除logo外的背景
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
dst = cv2.add(img1_bg, img2)  # 进行融合
img1[:rows, :cols] = dst  # 融合后放在原图上
```

> 经验之谈：掩膜的概念在图像混合/叠加的场景下使用较多，可以多多练习噢！

## 小结

- `cv2.add()`用来叠加两幅图片，`cv2.addWeighted()`也是叠加两幅图片，但两幅图片的权重不一样。
- `cv2.bitwise_and()`, `cv2.bitwise_not()`, `cv2.bitwise_or()`, `cv2.bitwise_xor()`分别执行按位与/或/非/异或运算。掩膜就是用来对图片进行全局或局部的遮挡。

## 接口文档

- [cv2.add()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga10ac1bfb180e2cfda1701d06c24fdbd6)
- [cv2.addWeighted()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#gafafb2513349db3bcff51f54ee5592a19)
- [cv2.bitwise_and()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14)
- [cv2.bitwise_not()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga0002cf8b418479f4cb49a75442baee2f)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/09.%20%E5%9B%BE%E5%83%8F%E6%B7%B7%E5%90%88)
- [掩膜](https://baike.baidu.com/item/%E6%8E%A9%E8%86%9C/8544392?fr=aladdin)
- [Arithmetic Operations on Images](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html)