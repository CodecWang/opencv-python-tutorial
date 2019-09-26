# [OpenCV-Python教程03：打开摄像头](http://ex2tron.wang/opencv-python-open-camera/)

学习打开摄像头捕获照片、播放本地视频、录制视频等。<!-- more -->图片/视频等可到[源码处](#引用)下载。

---

## 目标

- 打开摄像头并捕获照片
- 播放本地视频，录制视频
- OpenCV函数：`cv2.VideoCapture()`, `cv2.VideoWriter()`

## 教程

### 打开摄像头

要使用摄像头，需要使用`cv2.VideoCapture(0)`创建VideoCapture对象，参数0指的是摄像头的编号，如果你电脑上有两个摄像头的话，访问第2个摄像头就可以传入1，依此类推。

``` python
# 打开摄像头并灰度化显示
import cv2

capture = cv2.VideoCapture(0)

while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
```

`capture.read()`函数返回的第1个参数ret(return value缩写)是一个布尔值，表示当前这一帧是否获取正确。`cv2.cvtColor()`用来转换颜色，这里将彩色图转成灰度图。

另外，通过`cap.get(propId)`可以获取摄像头的一些属性，比如捕获的分辨率，亮度和对比度等。propId是从0~18的数字，代表不同的属性，完整的属性列表可以参考：[VideoCaptureProperties](https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d)。也可以使用`cap.set(propId,value)`来修改属性值。比如说，我们在while之前添加下面的代码：

``` python
# 获取捕获的分辨率
# propId可以直接写数字，也可以用OpenCV的符号表示
width, height = capture.get(3), capture.get(4)
print(width, height)

# 以原分辨率的一倍来捕获
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)
```

> 经验之谈：某些摄像头设定分辨率等参数时会无效，因为它有固定的分辨率大小支持，一般可在摄像头的资料页中找到。

### 播放本地视频

跟打开摄像头一样，如果把摄像头的编号换成视频的路径就可以播放本地视频了。回想一下`cv2.waitKey()`，它的参数表示暂停时间，所以这个值越大，视频播放速度越慢，反之，播放速度越快，通常设置为25或30。

```python
# 播放本地视频
capture = cv2.VideoCapture('demo_video.mp4')

while(capture.isOpened()):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(30) == ord('q'):
        break
```

### 录制视频

之前我们保存图片用的是`cv2.imwrite()`，要保存视频，我们需要创建一个`VideoWriter`的对象，需要给它传入四个参数：

- 输出的文件名，如'output.avi'
- 编码方式[FourCC](https://baike.baidu.com/item/fourcc/6168470?fr=aladdin)码
- 帧率[FPS](https://baike.baidu.com/item/FPS/3227416)
- 要保存的分辨率大小

FourCC是用来指定视频编码方式的四字节码，所有的编码可参考[Video Codecs](http://www.fourcc.org/codecs.php)。如MJPG编码可以这样写： `cv2.VideoWriter_fourcc(*'MJPG')`或`cv2.VideoWriter_fourcc('M','J','P','G')`

```python
capture = cv2.VideoCapture(0)

# 定义编码方式并创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
outfile = cv2.VideoWriter('output.avi', fourcc, 25., (640, 480))

while(capture.isOpened()):
    ret, frame = capture.read()

    if ret:
        outfile.write(frame)  # 写入文件
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
```

## 小结

- 使用`cv2.VideoCapture()`创建视频对象，然后在循环中一帧帧显示图像。参数传入数字时，代表打开摄像头，传入本地视频路径时，表示播放本地视频。
- `cap.get(propId)`获取视频属性，`cap.set(propId,value)`设置视频属性。
- `cv2.VideoWriter()`创建视频写入对象，用来录制/保存视频。

## 练习

1. 请先阅读[番外篇：滑动条](/opencv-python-extra-trackbar/)，然后实现一个可以拖动滑块播放视频的功能。（提示：需要用到 `cv2.CAP_PROP_FRAME_COUNT`和`cv2.CAP_PROP_POS_FRAMES`两个属性）。

## 接口文档

- [VideoCapture Object](<https://docs.opencv.org/4.0.0/d8/dfe/classcv_1_1VideoCapture.html>)
- [VideoWriter Object](<https://docs.opencv.org/4.0.0/dd/d9e/classcv_1_1VideoWriter.html>)
- [cv2.cvtColor()](https://docs.opencv.org/4.0.0/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/03.%20%E6%89%93%E5%BC%80%E6%91%84%E5%83%8F%E5%A4%B4)
- [Video Codecs by FOURCC](http://www.fourcc.org/codecs.php)
- [Getting Started with Videos](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html)