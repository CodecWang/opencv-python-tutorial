# [OpenCV-Python教程番外篇6：鼠标绘图](http://ex2tron.wang/opencv-python-extra-drawing-with-mouse/)

![](http://blog.codec.wang/cv2_live_draw_rectangle.gif)

学习如何用鼠标实时绘图。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 目标

- 捕获鼠标事件
- OpenCV函数：`cv2.setMouseCallback()`

## 教程

### 知道鼠标在哪儿

OpenCV中，我们需要创建一个鼠标的回调函数来获取鼠标当前的位置、当前的事件如左键按下/左键释放或是右键单击等等，然后执行相应的功能。

使用`cv2.setMouseCallback()`来创建鼠标的回调函数，比如我们在左键单击的时候，打印出当前鼠标的位置：

```python
import cv2
import numpy as np

# 鼠标的回调函数
def mouse_event(event, x, y, flags, param):
    # 通过event判断具体是什么事件，这里是左键按下
    if event == cv2.EVENT_LBUTTONDOWN:
        print((x, y))

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
# 定义鼠标的回调函数
cv2.setMouseCallback('image', mouse_event)

while(True):
    cv2.imshow('image', img)
    # 按下ESC键退出
    if cv2.waitKey(20) == 27:
        break
```

上面的代码先定义鼠标的回调函数`mouse_event()`，然后在回调函数中判断是否是左键单击事件 `EVENT_LBUTTONDOWN`，是的话就打印出坐标。需要注意的是，回调函数的参数格式是固定的，不要随意更改。

那除了左键单击之外，还有哪些事件呢？可以用下面的代码打印出来：

```python
# 获取所有的事件
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
```

### 综合实例

现在我们来实现一个综合的例子，这个实例会帮助你理解图像交互的一些思想：

在图像上用鼠标画图，可以画圆或矩形，按m键在两种模式下切换。左键按下时开始画图，移动到哪儿画到哪儿，左键释放时结束画图。听上去很复杂，是吗？一步步来看：

- 用鼠标画图：需要定义鼠标的回调函数mouse_event
- 画圆或矩形：需要定义一个画图的模式mode
- 左键单击、移动、释放：需要捕获三个不同的事件
- 开始画图，结束画图：需要定义一个画图的标记位drawing

好，开始coding吧：

```python
import cv2
import numpy as np

drawing = False  # 是否开始画图
mode = True  # True：画矩形，False：画圆
start = (-1, -1)

def mouse_event(event, x, y, flags, param):
    global start, drawing, mode

    # 左键按下：开始画图
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    # 鼠标移动，画图
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    # 左键释放：结束画图
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)

while(True):
    cv2.imshow('image', img)
    # 按下m切换模式
    if cv2.waitKey(1) == ord('m'):
        mode = not mode
    elif cv2.waitKey(1) == 27:
        break
```

效果应该如下图所示：

![](http://blog.codec.wang/cv2_mouse_drawing_rectangle_circle.jpg)

## 小结

- 要用鼠标绘图，需要用`cv2.setMouseCallback()`定义回调函数，然后在回调函数中根据不同的event事件，执行不同的功能。

## 练习

1.（选做）实现用鼠标画矩形，跟实例差不多，但只实时画一个，类似下面动图：

![实时画一个矩形](http://blog.codec.wang/cv2_live_draw_rectangle.gif)

2.（选做）做一个在白色面板上绘图的简单程序，可用滑动条调整颜色和笔刷大小。

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E7%95%AA%E5%A4%96%E7%AF%8706.%20%E9%BC%A0%E6%A0%87%E7%BB%98%E5%9B%BE)
- [Mouse as a Paint-Brush](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html)