# 01: 简介与安装

相信大部分人知道的 OpenCV 都是用 C++ 来开发的，那为什么我推荐使用 Python 呢？

:::tip

本教程基础内容来自 [OpenCV 官方英文教程](https://docs.opencv.org/)，我按照使用度和难易度翻译，重新编写了大量原创内容，将不常用和较难的部分写成番外篇，浅显易懂，很 easy 的辣。每节的源码、图片和练习题答案均可在引用处找到噢\(⊙o⊙\)

:::

## Python 照样快！

众所周知，虽然 Python 语法简洁、编写高效，但相比 C/C++运行慢很多。然而 Python 还有个重要的特性：它是一门胶水语言！Python 可以很容易地扩展 C/C++。OpenCV-Python 就是用 Python 包装了 C++ 的实现，背后实际就是 C++ 的代码在跑，运行速度非常接近原生。

比如我分别用 Python 和 C++实现读入图片和调整图片的亮度对比度，结果如下：

![](http://cos.codec.wang/cv2_python_vs_cplus_speed.jpg)

**可以看到某些情况下 Python 的运行速度甚至好于 C++，代码行数也直接少一半多！**

另外，图像是矩阵数据，OpenCV-Python 原生支持 [Numpy](https://baike.baidu.com/item/numpy)，相当于 Python 中的 Matlab，为矩阵运算、科学计算提供了极大的便利性。

## 人工智能浪潮

近些年，人工智能 AI 相关技术的快速发展大家有目共睹。在编程语言方面，更多人希望的是具备高效开发效率、跨平台、高度扩展性的语言，尤其是一些 AI 巨头优先推出支持 Python 语言的深度学习框架，如 Facebook 的[PyTorch](https://pytorch.org/)、Google 的[Tensorflow](https://tensorflow.google.cn/)等，可以说 Python 是名副其实的“网红语言”了。

![](http://cos.codec.wang/cv2_ai_ml_dl2.jpg)

从[TIOBE 编程语言排行榜](https://www.tiobe.com/tiobe-index/)也可以看到，Python 发展迅猛，已经逼近 C++的份额。这个排行榜每月更新，就不截图了，我编写时的 TOP5：Java/C/C++/Python/C\#。

## 人生苦短，我用 Python

- 如果你搞科研用，果断放弃 C++（Matlab？出门左拐）
- 如果你是快速原型开发，验证方案，果断放弃 C++
- 如果你懒的配置 OpenCV 环境，果断放弃 C++
- 如果你的程序是在支持 Python 的较高硬件环境下运行，果断放弃 C++
- 如果你担心 Python 写不了界面，那是你的问题 o_o ....
- 除非你的程序是 MFC 或已经用 C++编写其他模块或是嵌入式设备，那就用 C++吧

**"人生苦短，我用 Python！！！"**

## 安装

> 本教程编写时使用的相关版本是：OpenCV 4.x，Python 3.x。

### opencv-python

只需终端下的一条指令：

```bash
pip install opencv-python
```

pip 是 Python 的包管理器，如果你还没安装 Python，强烈推荐安装[Anaconda](https://www.anaconda.com/download/)，它包含了大量的科学计算包，不用后期一个个安装。

### Anaconda 安装

进入 Anaconda[官网](https://www.anaconda.com/download/)，下载最新版本的安装文件，速度比较慢的话，可以去[清华开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)。

- Windows 版是 exe 文件，双击直接安装，安装时记得勾选 `Add Anaconda to my PATH environment variable`，添加到环境变量。
- Linux 版是 sh 文件，执行`bash Anaconda3-xx.sh`，Linux 版也会提示添加到环境变量，记得输 yes 就行。
- MAC 版是 pkg 文件，同样直接双击安装即可。

### 安装测试

Python 的版本可以在终端中输入`python --version`来查看。对于 OpenCV，打开 Python 的开发环境，输入`import cv2`，运行没有报错说明一切正常。要查看 OpenCV 的版本，可以：

```bash
print(cv2.__version__)
```

> 编辑器我习惯用 [Visual Studio Code](http://code.visualstudio.com/)，也可以用 [PyCharm](http://www.jetbrains.com/pycharm/)/[Atom](https://atom.io/)/Jupyter Notebook\(Anaconda 自带\)。

### 常见问题

1. pip 识别不了：pip 的目录没有添加到环境变量中，添加到用户\(或系统\) 变量的 path 中。
2. 下载速度很慢：可到[此处](https://pypi.org/search/?q=opencv-python)下载离线版，完成后在终端输入`pip install 文件名`安装。

## 学习软件

为了便于学习 OpenCV，我编写了一款 Windows 平台的教学软件[LearnOpenCVEdu](https://github.com/codecwang/LearnOpenCVEdu)，目前只开发了一部分功能，欢迎 Star 支持:smiley:。

![](http://cos.codec.wang/cv2_learn_opencv_edu_soft_screenshot.jpg)

:::tip
虽然我推荐大家使用 OpenCV-Python 进行图像处理，但想要深入理解 OpenCV，C++是必须的，尤其是**OpenCV 源码**！
:::

## 引用

- [本节源码](https://github.com/codecwang/OpenCV-Python-Tutorial/tree/master/01-Introduction-and-Installation)

### 网络资料

- [OpenCV Docs 官方文档](https://docs.opencv.org/)
- [OpenCV 源码](https://github.com/opencv/opencv)
- [官方英文教程：OpenCV-Python Tutorials](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
- [LearnOpenCV](http://www.learnopencv.com)、[LearnOpenCV Github](https://github.com/spmallick/learnopencv)
- [OpenCV 中文教程](http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/tutorials.html)

### 书籍

- [Programming Computer Vision with Python](http://programmingcomputervision.com/)、[中文书](https://www.amazon.cn/dp/B00L3Y3NEM/ref=sr_1_1?ie=UTF8&qid=1543929834&sr=8-1&keywords=Python+%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89)
- [Practical Python and OpenCV](https://www.pyimagesearch.com/practical-python-opencv/)

### 名校视觉研究所/课程

- [卡内基梅隆大学](http://graphics.cs.cmu.edu/)
- [多伦多大学](https://www.cs.toronto.edu/~guerzhoy/320/)
