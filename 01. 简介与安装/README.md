# [OpenCV-Python教程01：简介与安装](http://ex2tron.wang/opencv-python-introduction-and-installation/)

![](http://blog.codec.wang/cv2_install_opencv-python.jpg)

相信大部分人知道的OpenCV都是用C++来开发的，那为什么我推荐使用Python呢？<!-- more -->

> 本教程翻译自[OpenCV官方英文教程](http://opencv-python-tutroals.readthedocs.io/en/latest/index.html)，我按照使用度和难易度翻译，重新编写了大量原创内容，将不常用和较难的部分写成番外篇，浅显易懂，很easy的辣。每节的源码、图片和练习题答案均可在[引用](#引用)处找到噢(⊙o⊙)

---

## Python照样快！

众所周知，虽然Python语法简洁，编写高效，但相比C/C++运行慢很多。然而Python还有个重要的特性：它是一门胶水语言！Python可以很容易地扩展C/C++。**OpenCV-Python**就是用Python包装了C++的实现，背后实际就是C++的代码在跑，所以代码的运行速度跟原生C/C++速度一样快。

我举两个简单的例子就一目了然了：一个是读入图片，另一个是调整图片的对比度和亮度：

![](http://blog.codec.wang/cv2_python_vs_cplus_speed.jpg)

**可以看到某些情况下Python的运行速度甚至好于C++，代码行数也直接少一半多！**另外，图像是矩阵数据，OpenCV-Python原生支持[Numpy](https://baike.baidu.com/item/numpy)，相当于Python中的Matlab，为矩阵运算、科学计算提供了极大的便利性。

## 人工智能浪潮

近些年，人工智能相关技术的快速发展大家有目共睹，不必多说。在编程语言方面，更多人希望的是具备高效开发效率、跨平台、高度扩展性的语言，尤其是一些AI巨头优先推出支持Python语言的深度学习框架，如Facebook的[PyTorch](https://pytorch.org/)、Google的[Tensorflow](https://tensorflow.google.cn/)等，可以说Python是名副其实的“网红语言”了。

![](http://blog.codec.wang/cv2_ai_ml_dl2.jpg)

从[TIOBE编程语言排行榜](https://www.tiobe.com/tiobe-index/)也可以看到，Python发展迅猛，已经逼近C++的份额。这个排行榜每月更新，我就不截图了，编写时TOP5：Java/C/C++/Python/C#。

## 人生苦短，我用Python

- 如果你搞科研用，果断放弃C++（Matlab？出门左拐）
- 如果你是快速原型开发，验证方案，果断放弃C++
- 如果你懒的配置OpenCV环境，果断放弃C++
- 如果你的程序是在支持Python的较高硬件环境下运行，果断放弃C++
- 如果你担心Python写不了界面，那是你的问题o_o ....
- 除非你的程序是MFC或已经用C++编写其他模块或是嵌入式设备，那就用C++吧

**"人生苦短，我用Python！！！"**

## 安装

> 本教程编写时使用的软件版本是：OpenCV 3.x，Python 3.x。

要安装OpenCV，只需cmd下的一条指令：

``` bash
pip install opencv-python
```

pip是Python的包管理器，如果你还没安装Python，强烈推荐安装[Anaconda](https://www.anaconda.com/download/)，它包含了大量的科学计算包，不用后期一个个安装。即使你已经装了Python也没有影响，Anaconda相当于虚拟环境，互不干扰。

### 安装步骤

进入Anaconda[官网](https://www.anaconda.com/download/)，下载最新版本的安装文件，速度比较慢的话，可以去[清华开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)。

- Windows版下载的是exe文件，双击可以直接安装，安装时记得勾选 `Add Anaconda to my PATH environment variable`，添加到环境变量中。

- Linux版下载的是sh文件，下载完成后，终端切换到下载目录，执行`bash Anaconda3-xx.sh`，Linux版也会提示添加环境变量，记得输yes就行。

### 安装测试

Python安装好之后，可以在cmd中输入`python --version`来查看Python的版本信息。对于OpenCV，打开Python的开发环境，输入`import cv2`，运行没有报错说明一切正常。要查看OpenCV的版本，可以：

``` bash
print(cv2.__version__)  # '3.4.1'
```

> Python开发环境我用的是[Visual Studio Code](http://code.visualstudio.com/)，也可以用[PyCharm](http://www.jetbrains.com/pycharm/)/[Atom](https://atom.io/)/Jupyter Notebook(Anaconda自带)，或者直接在命令行里敲，自己习惯就行。

### 常见问题

1. pip识别不了：环境变量中没有pip的目录，找到pip目录，添加到用户（或系统）变量的path中。
2. 下载速度很慢：可[到此处](https://pypi.org/search/?q=opencv-python)下载离线版。下载完成后，cmd切换到下载目录，输入 `pip install 文件名`安装。

## 学习软件

为了便于学习OpenCV，我写了一个教学款软件[LearnOpenCVEdu](https://github.com/ex2tron/LearnOpenCVEdu)，目前只开发了一部分功能，有兴趣的童鞋可以支持一下噢😊

![大家随手点个Star吧(●ˇ∀ˇ●)](http://blog.codec.wang/cv2_learn_opencv_edu_soft_screenshot.jpg)

> 经验之谈：虽然从一开始我就推荐大家使用OpenCV-Python进行图像处理，但*想要深入理解OpenCV*，C++还是必须的，尤其是**OpenCV源码**！

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/01.%20%E7%AE%80%E4%BB%8B%E4%B8%8E%E5%AE%89%E8%A3%85)

### 网络资料

- [**OpenCV Docs官方文档**](https://docs.opencv.org/)
- [OpenCV 官方Github](https://github.com/opencv/opencv)
- [官方英文教程：OpenCV-Python Tutorials](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
- [LearnOpenCV](http://www.learnopencv.com)、[LearnOpenCV Github](https://github.com/spmallick/learnopencv)
- [Numpy Quickstart Tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
- [OpenCV 中文教程](http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/tutorials.html)

### 书籍

- [Programming Computer Vision with Python](http://programmingcomputervision.com/)、[中文书](https://www.amazon.cn/dp/B00L3Y3NEM/ref=sr_1_1?ie=UTF8&qid=1543929834&sr=8-1&keywords=Python+%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89)
- https://www.pyimagesearch.com/practical-python-opencv/

### 名校视觉研究所/课程

- [卡内基梅隆大学](http://graphics.cs.cmu.edu/)
- [多伦多大学](https://www.cs.toronto.edu/~guerzhoy/320/)