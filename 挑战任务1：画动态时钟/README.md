# [OpenCV-Python教程挑战任务：画动态时钟](http://ex2tron.wang/opencv-python-clock-drawing/)
 
![](http://blog.codec.wang/cv2_draw_clock_dynamic_sample.gif)

挑战任务：使用OpenCV绘制一个随系统时间动态变化的时钟。<!-- more -->

---

## 挑战内容

> **完成如下图所展示的动态时钟，时钟需随系统时间变化，中间显示当前日期。**

![](http://blog.codec.wang/cv2_draw_clock_dynamic_sample.gif)

其实本次任务涉及的OpenCV知识并不多，但有助于提升大家的编程实践能力。

**挑战题不会做也木有关系，但请务必在自行尝试后，再看下面的解答噢，**不然...我也没办法(￣▽￣)"

---

## 挑战解答

### 方案

本次挑战任务旨在提升大家的动手实践能力，解决实际问题，所以我们得先有个解题思路和方案。观察下常见的时钟表盘：

![](http://blog.codec.wang/cv2_draw_clock_actual_clock_sample.jpg)

整个表盘其实只有3根表针在动，所以可以先画出静态表盘，然后获取系统当前时间，根据时间实时动态绘制3根表针就解决了。

### 绘制表盘

表盘上只有60条分/秒刻线和12条小时刻线，当然还有表盘的外部轮廓圆，也就是重点在如何画72根线。先把简单的圆画出来：

```python
import cv2
import math
import datetime
import numpy as np

margin = 5  # 上下左右边距
radius = 220  # 圆的半径
center = (center_x, center_y) = (225, 225)  # 圆心

# 1. 新建一个画板并填充成白色
img = np.zeros((450, 450, 3), np.uint8)
img[:] = (255, 255, 255)

# 2. 画出圆盘
cv2.circle(img, center, radius, (0, 0, 0), thickness=5)
```

![](http://blog.codec.wang/cv2_draw_clock_blank_circle.jpg)

前面我们使用OpenCV画直线的时候，需知道直线的起点和终点坐标，那么画72根线就变成了获取72组坐标。

在平面坐标系下，已知半径和角度的话，A点的坐标可以表示为：
$$
\begin{matrix}
   x=r\times \cos\alpha \newline
   y=r\times \sin\alpha
\end{matrix}
$$
![](http://blog.codec.wang/cv2_draw_clock_center_shift.jpg)

先只考虑将坐标系原点移动到左上角，角度依然是平面坐标系中的逆时针计算，那么新坐标是：

$$
\begin{matrix}
   x=r+r\times \cos\alpha \newline
   y=r+r\times \sin\alpha
\end{matrix}
$$

对于60条分/秒刻线，刻线间的夹角是360°/60=6°，对于小时刻线，角度是360°/12=30°，这样就得到了72组起点坐标，那怎么得到终点坐标呢？其实同样的原理，用一个同心的小圆来计算得到B点：

![](http://blog.codec.wang/cv2_draw_clock_a_b_position.jpg)

通过A/B两点就可以画出直线：

```python
pt1 = []

# 3. 画出60条秒和分钟的刻线
for i in range(60):
    # 最外部圆，计算A点
    x1 = center_x+(radius-margin)*math.cos(i*6*np.pi/180.0)
    y1 = center_y+(radius-margin)*math.sin(i*6*np.pi/180.0)
    pt1.append((int(x1), int(y1)))

    # 同心小圆，计算B点
    x2 = center_x+(radius-15)*math.cos(i*6*np.pi/180.0)
    y2 = center_y+(radius-15)*math.sin(i*6*np.pi/180.0)

    cv2.line(img, pt1[i], (int(x2), int(y2)), (0, 0, 0), thickness=2)

# 4. 画出12条小时的刻线
for i in range(12):
    # 12条小时刻线应该更长一点
    x = center_x+(radius-25)*math.cos(i*30*np.pi/180.0)
    y = center_y+(radius-25)*math.sin(i*30*np.pi/180.0)
    # 这里用到了前面的pt1
    cv2.line(img, pt1[i*5], (int(x), int(y)), (0, 0, 0), thickness=5)

# 到这里基本的表盘图就已经画出来了
```

![](http://blog.codec.wang/cv2_draw_clock_blank_clock.jpg)

### 角度换算

接下来算是一个小难点，首先**时钟的起始坐标在正常二维坐标系的90°方向，其次时钟跟图像一样，都是顺时针计算角度的**，所以三者需要统一下：

![](http://blog.codec.wang/cv2_draw_clock_different_clock_contrast.jpg)

因为角度是完全对称的，顺逆时针没有影响，所以平面坐标系完全不用理会，放在这里只是便于大家理解。对于时钟坐标和图像坐标，时钟0的0°对应图像的270°，时钟15的90°对应图像的360°，时钟30的180°对应图像的450°（360°+90°）...

所以两者之间的关系便是：

```
计算角度 = 时钟角度+270°
计算角度 = 计算角度 if 计算角度<=360° else 计算角度-360°
```

### 同步时间

Python中如何获取当前时间和添加日期文字都比较简单，看代码就行，我就不解释了。代码中角度计算我换了一种方式，其实是一样的，看你能不能看懂(●ˇ∀ˇ●)：

```python
while(1):
    # 不断拷贝表盘图，才能更新绘制，不然会重叠在一起
    temp = np.copy(img)

    # 5. 获取系统时间，画出动态的时-分-秒三条刻线
    now_time = datetime.datetime.now()
    hour, minute, second = now_time.hour, now_time.minute, now_time.second

    # 画秒刻线
    # OpenCV中的角度是顺时针计算的，所以需要转换下
    sec_angle = second*6+270 if second <= 15 else (second-15)*6
    sec_x = center_x+(radius-margin)*math.cos(sec_angle*np.pi/180.0)
    sec_y = center_y+(radius-margin)*math.sin(sec_angle*np.pi/180.0)
    cv2.line(temp, center, (int(sec_x), int(sec_y)), (203, 222, 166), 2)

    # 画分刻线
    min_angle = minute*6+270 if minute <= 15 else (minute-15)*6
    min_x = center_x+(radius-35)*math.cos(min_angle*np.pi/180.0)
    min_y = center_y+(radius-35)*math.sin(min_angle*np.pi/180.0)
    cv2.line(temp, center, (int(min_x), int(min_y)), (186, 199, 137), 8)

    # 画时刻线
    hour_angle = hour*30+270 if hour <= 3 else (hour-3)*30
    hour_x = center_x+(radius-65)*math.cos(hour_angle*np.pi/180.0)
    hour_y = center_y+(radius-65)*math.sin(hour_angle*np.pi/180.0)
    cv2.line(temp, center, (int(hour_x), int(hour_y)), (169, 198, 26), 15)

    # 6. 添加当前日期文字
    font = cv2.FONT_HERSHEY_SIMPLEX
    time_str = now_time.strftime("%d/%m/%Y")
    cv2.putText(img, time_str, (135, 275), font, 1, (0, 0, 0), 2)

    cv2.imshow('clocking', temp)
    if cv2.waitKey(1) == 27:  # 按下ESC键退出
        break
```

![](http://blog.codec.wang/cv2_draw_clock_sample.jpg)

本此挑战旨在锻炼一步步解决实际问题的思路（虽然有点数学知识(￣▽￣)"），大家再接再厉噢！

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E6%8C%91%E6%88%98%E4%BB%BB%E5%8A%A11%EF%BC%9A%E7%94%BB%E5%8A%A8%E6%80%81%E6%97%B6%E9%92%9F)