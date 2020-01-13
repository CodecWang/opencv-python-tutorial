# [OpenCV-Python教程挑战任务：车道检测](http://ex2tron.wang/opencv-python-lane-road-detection/)

![](http://blog.codec.wang/cv2_lane_detection_result_sample.jpg)

挑战任务：实际公路的车道线检测。<!-- more -->图片等可到[源码处](#引用)下载。

---

## 挑战内容

> **1. 在所提供的公路图片上检测出车道线并标记：**

![](http://blog.codec.wang/cv2_lane_detection_result_sample.jpg)

> **2. 在所提供的公路视频上检测出车道线并标记：**

<video id="video" controls=""  <source id="mp4" src="http://blog.codec.wang/cv2_white_lane_green_mark.mp4" type="video/mp4">
</video>
本次挑战内容来自Udacity自动驾驶纳米学位课程，素材中车道保持不变，车道线清晰明确，易于检测，是车道检测的基础版本，网上也有很多针对复杂场景的高级实现，感兴趣的童鞋可以自行了解。

**挑战题不会做也木有关系，但请务必在自行尝试后，再看下面的解答噢，**不然...我也没办法(￣▽￣)"

---

## 挑战解答

### 方案

要检测出当前车道，就是要检测出左右两条车道直线。由于无人车一直保持在当前车道，那么无人车上的相机拍摄的视频中，车道线的位置应该基本固定在某一个范围内：

![](http://blog.codec.wang/cv2_lane_detection_roi_sample.jpg)

如果我们手动把这部分ROI区域抠出来，就会排除掉大部分干扰。接下来检测直线肯定是用霍夫变换，但ROI区域内的边缘直线信息还是很多，考虑到只有左右两条车道线，一条斜率为正，一条为负，可将所有的线分为两组，每组再通过均值或最小二乘法拟合的方式确定唯一一条线就可以完成检测。总体步骤如下：

1. 灰度化
2. 高斯模糊
3. Canny边缘检测
4. 不规则ROI区域截取
5. 霍夫直线检测
6. 车道计算

对于视频来说，只要一幅图能检查出来，合成下就可以了，问题不大。

### 图像预处理

灰度化和滤波操作是大部分图像处理的必要步骤。灰度化不必多说，因为不是基于色彩信息识别的任务，所以没有必要用彩色图，可以大大减少计算量。而滤波会削弱图像噪点，排除干扰信息。另外，根据前面学习的知识，边缘提取是基于图像梯度的，梯度对噪声很敏感，所以平滑滤波操作必不可少。

![原图 vs 灰度滤波图](http://blog.codec.wang/cv2_lane_detection_gray_blur_result.jpg)

这次的代码我们分模块来写，规范一点。其中`process_an_image()`是主要的图像处理流程：

```python
import cv2
import numpy as np

# 高斯滤波核大小
blur_ksize = 5
# Canny边缘检测高低阈值
canny_lth = 50
canny_hth = 150

def process_an_image(img):
    # 1. 灰度化、滤波和Canny
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 1)
    edges = cv2.Canny(blur_gray, canny_lth, canny_hth)

if __name__ == "__main__":
    img = cv2.imread('test_pictures/lane.jpg')
    result = process_an_image(img)
    cv2.imshow("lane", np.hstack((img, result)))
    cv2.waitKey(0)
```

![边缘检测结果图](http://blog.codec.wang/cv2_lane_detection_canny_result.jpg)

### ROI截取

按照前面描述的方案，只需保留边缘图中的红线部分区域用于后续的霍夫直线检测，其余都是无用的信息：

![](http://blog.codec.wang/cv2_lane_detection_canny_roi_reserve.jpg)

如何实现呢？还记得图像混合中的这张图吗？

![](http://blog.codec.wang/cv2_understand_mask.jpg)

 我们可以创建一个梯形的mask掩膜，然后与边缘检测结果图混合运算，掩膜中白色的部分保留，黑色的部分舍弃。梯形的四个坐标需要手动标记：

![掩膜mask](http://blog.codec.wang/cv2_lane_detection_mask_sample.jpg)

```python
def process_an_image(img):
    # 1. 灰度化、滤波和Canny

    # 2. 标记四个坐标点用于ROI截取
    rows, cols = edges.shape
    points = np.array([[(0, rows), (460, 325), (520, 325), (cols, rows)]])
    # [[[0 540], [460 325], [520 325], [960 540]]]
    roi_edges = roi_mask(edges, points)
    
def roi_mask(img, corner_points):
    # 创建掩膜
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, corner_points, 255)

    masked_img = cv2.bitwise_and(img, mask)
    return masked_img
```

这样，结果图"roi_edges"应该是：

![只保留关键区域的边缘检测图](http://blog.codec.wang/cv2_lane_detection_masked_roi_edges.jpg)

### 霍夫直线提取

为了方便后续计算直线的斜率，我们使用统计概率霍夫直线变换（因为它能直接得到直线的起点和终点坐标）。霍夫变换的参数比较多，可以放在代码开头，便于修改：

```python
# 霍夫变换参数
rho = 1
theta = np.pi / 180
threshold = 15
min_line_len = 40
max_line_gap = 20

def process_an_image(img):
    # 1. 灰度化、滤波和Canny

    # 2. 标记四个坐标点用于ROI截取

    # 3. 霍夫直线提取
    drawing, lines = hough_lines(roi_edges, rho, theta, threshold, min_line_len, max_line_gap)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    # 统计概率霍夫直线变换
    lines = cv2.HoughLinesP(img, rho, theta, threshold, minLineLength=min_line_len, maxLineGap=max_line_gap)

    # 新建一副空白画布
    drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    # draw_lines(drawing, lines)     # 画出直线检测结果

    return drawing, lines

def draw_lines(img, lines, color=[0, 0, 255], thickness=1):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)
```

`draw_lines()`是用来画直线检测的结果，后面我们会接着处理直线，所以这里注释掉了，可以取消注释看下效果：

![霍夫变换结果图](http://blog.codec.wang/cv2_lane_detection_hough_lines_direct_result.jpg)

对本例的这张测试图来说，如果打印出直线的条数`print(len(lines))`，应该是有16条。

### 车道计算

这部分应该算是本次挑战任务的核心内容了：前面通过霍夫变换得到了多条直线的起点和终点，我们的目的是通过某种算法只得到左右两条车道线。

**第一步、根据斜率正负划分某条线是左车道还是右车道。**
$$
斜率=\frac{y_2-y_1}{x_2-x_1}(\leq0:左,>0:右)
$$

> 经验之谈：再次强调，斜率计算是在图像坐标系下，所以斜率正负/左右跟平面坐标有区别。

**第二步、迭代计算各直线斜率与斜率均值的差，排除掉差值过大的异常数据。**

注意这里迭代的含义，意思是第一次计算完斜率均值并排除掉异常值后，再在剩余的斜率中取均值，继续排除……这样迭代下去。

**第三步、最小二乘法拟合左右车道线。**

经过第二步的筛选，就只剩下可能的左右车道线了，这样只需从多条直线中拟合出一条就行。拟合方法有很多种，最常用的便是最小二乘法，它通过最小化误差的平方和来寻找数据的最佳匹配函数。

具体来说，假设目前可能的左车道线有6条，也就是12个坐标点，包括12个x和12个y，我们的目的是拟合出这样一条直线：
$$
f(x_i) = ax_i+b
$$
使得误差平方和最小：
$$
E=\sum(f(x_i)-y_i)^2
$$

Python中可以直接使用`np.polyfit()`进行最小二乘法拟合。

```python
def process_an_image(img):
    # 1. 灰度化、滤波和Canny

    # 2. 标记四个坐标点用于ROI截取

    # 3. 霍夫直线提取

    # 4. 车道拟合计算
    draw_lanes(drawing, lines)

    # 5. 最终将结果合在原图上
    result = cv2.addWeighted(img, 0.9, drawing, 0.2, 0)

    return result

def draw_lanes(img, lines, color=[255, 0, 0], thickness=8):
    # a. 划分左右车道
    left_lines, right_lines = [], []
    for line in lines:
        for x1, y1, x2, y2 in line:
            k = (y2 - y1) / (x2 - x1)
            if k < 0:
                left_lines.append(line)
            else:
                right_lines.append(line)

    if (len(left_lines) <= 0 or len(right_lines) <= 0):
        return

    # b. 清理异常数据
    clean_lines(left_lines, 0.1)
    clean_lines(right_lines, 0.1)

    # c. 得到左右车道线点的集合，拟合直线
    left_points = [(x1, y1) for line in left_lines for x1, y1, x2, y2 in line]
    left_points = left_points + [(x2, y2) for line in left_lines for x1, y1, x2, y2 in line]
    right_points = [(x1, y1) for line in right_lines for x1, y1, x2, y2 in line]
    right_points = right_points + [(x2, y2) for line in right_lines for x1, y1, x2, y2 in line]

    left_results = least_squares_fit(left_points, 325, img.shape[0])
    right_results = least_squares_fit(right_points, 325, img.shape[0])

    # 注意这里点的顺序
    vtxs = np.array([[left_results[1], left_results[0], right_results[0], right_results[1]]])
    # d. 填充车道区域
    cv2.fillPoly(img, vtxs, (0, 255, 0))

    # 或者只画车道线
    # cv2.line(img, left_results[0], left_results[1], (0, 255, 0), thickness)
    # cv2.line(img, right_results[0], right_results[1], (0, 255, 0), thickness)
    
def clean_lines(lines, threshold):
    # 迭代计算斜率均值，排除掉与差值差异较大的数据
    slope = [(y2 - y1) / (x2 - x1) for line in lines for x1, y1, x2, y2 in line]
    while len(lines) > 0:
        mean = np.mean(slope)
        diff = [abs(s - mean) for s in slope]
        idx = np.argmax(diff)
        if diff[idx] > threshold:
            slope.pop(idx)
            lines.pop(idx)
        else:
            break
            
def least_squares_fit(point_list, ymin, ymax):
    # 最小二乘法拟合
    x = [p[0] for p in point_list]
    y = [p[1] for p in point_list]

    # polyfit第三个参数为拟合多项式的阶数，所以1代表线性
    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)  # 获取拟合的结果

    xmin = int(fit_fn(ymin))
    xmax = int(fit_fn(ymax))

    return [(xmin, ymin), (xmax, ymax)]
```

这段代码比较多，请每个步骤单独来看。最后得到的是左右两条车道线的起点和终点坐标，可以选择画出车道线，这里我直接填充了整个区域：

![](http://blog.codec.wang/cv2_lane_detection_result_sample.jpg)

### 视频处理

搞定了一张图，视频也就没什么问题了，关键就是视频帧的提取和合成，为此，我们要用到Python的视频编辑包[moviepy](https://pypi.org/project/moviepy/#files)：

```python
pip install moviepy
```

另外还需要ffmpeg，首次运行moviepy时会自动下载，也可[手动](https://github.com/imageio/imageio-binaries/tree/master/ffmpeg)下载。

只需在开头导入moviepy，然后将主函数改掉就可以了，其余代码不需要更改：

```python
# 开头导入moviepy
from moviepy.editor import VideoFileClip

# 主函数更改为：
if __name__ == "__main__":
    output = 'test_videos/output.mp4'
    clip = VideoFileClip("test_videos/cv2_white_lane.mp4")
    out_clip = clip.fl_image(process_an_image)
    out_clip.write_videofile(output, audio=False)
```

本文实现了车道检测的基础版本，如果你感兴趣的话，可以自行搜索或参考引用部分了解更多。

## 引用

- [图片和视频素材](http://blog.codec.wang/cv2_lane_detection_material.zip)
- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E6%8C%91%E6%88%98%E4%BB%BB%E5%8A%A13%EF%BC%9A%E8%BD%A6%E9%81%93%E6%A3%80%E6%B5%8B)
- [从零开始学习无人驾驶技术 --- 车道检测](https://zhuanlan.zhihu.com/p/25354571)
- [无人驾驶之高级车道线检测](https://blog.csdn.net/u010665216/article/details/80152458)

