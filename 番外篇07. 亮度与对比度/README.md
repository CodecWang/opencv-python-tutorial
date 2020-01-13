# [OpenCV-Python教程番外篇7：亮度与对比度](http://ex2tron.wang/opencv-python-extra-contrast-brightness/)

![](http://blog.codec.wang/cv2_contrast_brightness.jpg)

学习如何调整图片的亮度和对比度。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 亮度与对比度

亮度调整是将图像像素的强度整体变大/变小，对比度调整指的是图像暗处的像素强度变低，亮出的变高，从而拓宽某个区域内的显示精度。

OpenCV中亮度和对比度应用这个公式来计算：<span class="mrow" id="MathJax-Span-2"><span class="mi" id="MathJax-Span-3" style="font-family: MathJax_Math-italic;">g<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span class="mo" id="MathJax-Span-4" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-5" style="font-family: MathJax_Math-italic;">x</span><span class="mo" id="MathJax-Span-6" style="font-family: MathJax_Main;">)</span><span class="mo" id="MathJax-Span-7" style="font-family: MathJax_Main; padding-left: 0.281em;">=</span><span class="mi" id="MathJax-Span-8" style="font-family: MathJax_Math-italic; padding-left: 0.281em;">α</span><span class="mi" id="MathJax-Span-9" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.058em;"></span></span><span class="mo" id="MathJax-Span-10" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-11" style="font-family: MathJax_Math-italic;">x</span><span class="mo" id="MathJax-Span-12" style="font-family: MathJax_Main;">)</span><span class="mo" id="MathJax-Span-13" style="font-family: MathJax_Main; padding-left: 0.225em;">+</span><span class="mi" id="MathJax-Span-14" style="font-family: MathJax_Math-italic; padding-left: 0.225em;">β<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span></span>，其中：α(>0)、β常称为增益与偏置值，分别控制图片的对比度和亮度。

> 经验之谈：此处对α/β控制对比度和亮度有争议，具体请参考：[OpenCV关于对比度和亮度的误解](http://blog.csdn.net/abc20002929/article/details/40474807)。

```python
import cv2
import numpy as np

img = cv2.imread('lena.jpg')
# 此处需注意，请参考后面的解释
res = np.uint8(np.clip((1.5 * img + 10), 0, 255))
tmp = np.hstack((img, res))  # 两张图片横向合并（便于对比显示）

cv2.imshow('image', tmp)
cv2.waitKey(0)
```

还记得图像混合那一节中numpy对数据溢出的取模处理吗？`250+10 = 260 => 260%256=4`，它并不适用于我们的图像处理，所以用[np.clip()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.clip.html#numpy.clip)函数将数据限定：`a<0 => a=0, a>255 => a=255`。

![亮度与对比度调整](http://blog.codec.wang/cv2_contrast_brightness.jpg)

## 练习

1. 创建两个滑动条分别调整对比度和亮度（对比度范围：0~0.3，亮度：0~100）。提示：因为滑动条没有小数，所以可以设置为0~300，然后乘以0.01。

2. 亮度/对比度用C++实现也很有趣，推荐阅读：[OpenCV改变图像亮度和对比度以及优化](http://blog.csdn.net/u013139259/article/details/52145377)。

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E7%95%AA%E5%A4%96%E7%AF%8707.%20%E4%BA%AE%E5%BA%A6%E4%B8%8E%E5%AF%B9%E6%AF%94%E5%BA%A6)
- [numpy.clip()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.clip.html#numpy.clip)
- [OpenCV关于对比度和亮度的误解](http://blog.csdn.net/abc20002929/article/details/40474807)
- [OpenCV改变图像亮度和对比度以及优化](http://blog.csdn.net/u013139259/article/details/52145377)
- [Mat::convertTo](https://docs.opencv.org/3.1.0/d3/d63/classcv_1_1Mat.html#a3f356665bb0ca452e7d7723ccac9a810)
