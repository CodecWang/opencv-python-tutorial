# [OpenCV-Python教程拓展挑战：PyQt编写GUI界面](http://ex2tron.wang/opencv-python-using-pyqt5-create-gui/)

![](http://blog.codec.wang/cv2_pyqt_gui_sample.jpg)

拓展挑战：编写GUI图像处理应用程序。<!-- more -->

---

## 挑战内容

前面我们学习的OpenCV内容都是运行在命令行中的，没有界面，所以本次的拓展挑战内容便是：

> **了解Python编写[GUI](https://baike.baidu.com/item/GUI)界面的方法，使用PyQt5编写如下的图像处理应用程序，实现打开摄像头、捕获图片、读取本地图片、灰度化和Otsu自动阈值分割的功能。**

![](http://blog.codec.wang/cv2_pyqt_gui_sample.jpg)

**挑战题不会做也木有关系，但请务必在自行尝试后，再看下面的解答噢，**不然...我也没办法(￣▽￣)"

---

## 挑战解答

### 简介

> 目前我们学的内容都是跑在命令行中的，并没有界面，那么"脚本语言"Python如何搭建GUI界面呢？

其实Python支持多种图形界面库，如[Tk(Tkinter)](https://wiki.python.org/moin/TkInter)、[wxPython](https://www.wxpython.org/)、[PyQt](https://wiki.python.org/moin/PyQt)等，虽然Python自带Tkinter，无需额外安装包，但我更推荐使用PyQt，一是因为它完全基于Qt，跨平台，功能强大，有助于了解Qt的语法，二是Qt提供了Designer设计工具，界面设计上可以拖控件搞定，非常方便，大大节省时间。

- 最新版本：PyQt 5.x
- 官网（可能需要翻墙）：[https://www.riverbankcomputing.com/software/pyqt/](https://www.riverbankcomputing.com/software/pyqt/)

大家感兴趣的话，除去官网，下面是一些可参考的资源：

- [Python Wiki: PyQt](https://wiki.python.org/moin/PyQt)
- [PyQt/Tutorials](https://wiki.python.org/moin/PyQt/Tutorials)
- PyQt5 tutorial：[英文原版](http://zetcode.com/gui/pyqt5/)
- PyQt4 tutorial：[中文版](http://www.qaulau.com/books/PyQt4_Tutorial/index.html)、[英文原版](http://zetcode.com/gui/pyqt4/)
- [Qt5 Documentation](https://doc.qt.io/qt-5/)
- 中文参考书：[PyQt5快速开发与实战](https://www.amazon.cn/dp/B075VWFYFH/ref=sr_1_1?ie=UTF8&qid=1543407852&sr=8-1&keywords=PyQt5%E5%BF%AB%E9%80%9F%E5%BC%80%E5%8F%91%E4%B8%8E%E5%AE%9E%E6%88%98)
- [基于Qt的Python IDE Eric](http://eric-ide.python-projects.org/)

### 安装

```python
pip install pyqt5
```

下载速度慢的话，可以到[PyPI](https://pypi.org/project/PyQt5/#files)上下载离线版安装。另外我推荐使用Qt Designer来设计界面，如果你装的是Anaconda的话，就已经自带了designer.exe，例如我的是在：D:\ProgramData\Anaconda3\Library\bin\，如果是普通的Python环境，则需要自行安装：

```python
pip install pyqt5-tools
```

安装完成后，designer.exe应该在Python安装目录下：xxx\Lib\site-packages\pyqt5_tools\。

可以使用下面的代码生成一个简单的界面：

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Hello World!')
    window.show()

    sys.exit(app.exec_())
```

![](http://blog.codec.wang/cv2_pyqt5_hello_world_sample.jpg)

### 界面设计

根据我们的挑战内容，解决思路是使用Qt Designer来设计界面，使用Python完成代码逻辑。打开designer.exe，会弹出创建新窗体的窗口，我们直接点击“create”：

![](http://blog.codec.wang/cv2_pyqt5_designer_main_ui.jpg)

界面的左侧是Qt的常用控件"Widget Box"，右侧有一个控件属性窗口"Property Editor"，其余暂时用不到。本例中我们只用到了"Push Button"控件和"Label"控件：最上面的三个Label控件用于显示图片，可以在属性窗口调整它的大小，我们统一调整到150×150：

![](http://blog.codec.wang/cv2_pyqt5_main_ui_rough.jpg)

![](http://blog.codec.wang/cv2_pyqt5_designer_property_windows.jpg)

另外，控件上显示的文字"text"属性和控件的名字"objectName"属性需要修改，便于显示和代码调用。可以按照下面我推荐的命名：

|    控件    |  显示内容text  | 控件名objectName |
| :--------: | :------------: | :--------------: |
| PushButton |   打开摄像头   |  btnOpenCamera   |
| PushButton |    捕获图片    |    btnCapture    |
| PushButton |    打开图片    |   btnReadImage   |
| PushButton |     灰度化     |     btnGray      |
| PushButton | 阈值分割(Otsu) |   btnThreshold   |
|   Label    |     摄像头     |   labelCamera    |
|   Label    |     捕获图     |   labelCapture   |
|   Label    |     结果图     |   labelResult    |

这样大致界面就出来了，很简单：

![](http://blog.codec.wang/cv2_pyqt5_main_ui_word.jpg)

### 按钮事件

如果你之前有过一些GUI开发经验，比如MFC，WinForm等，就知道GUI是通过事件驱动的，什么意思呢？比如前面我们已经设计好了界面，接下来就需要实现"打开摄像头"到"阈值分割"这5个按钮的功能，也就是给每个按钮指定一个"函数"，逻辑代码写在这个函数里面。这种函数就称为事件，Qt中称为槽连接。

点击Designer工具栏的"Edit Signals/Slots"按钮，进入槽函数编辑界面，点击旁边的"Edit Widgets"可以恢复正常视图：

![](http://blog.codec.wang/cv2_pyqt5_designer_edit_singals_slots.jpg)

然后点击按钮并拖动，当产生类似于电路中的接地符号时释放鼠标，参看下面动图：

![](http://blog.codec.wang/cv2_pyqt5_how_to_create_slots.gif)

在弹出的配置窗口中，可以看到左侧是按钮的常用事件，我们选择点击事件"clicked()"，然后添加一个名为"btnOpenCamera_Clicked()"的槽函数：

![](http://blog.codec.wang/cv2_pyqt5_how_to_create_slots2.gif)

重复上面的步骤，给五个按钮添加五个槽函数，最终结果如下：

![](http://blog.codec.wang/cv2_pyqt5_main_click_event.jpg)

到此，我们就完成了界面设计的所有工作，按下Ctrl+S保存当前窗口为.ui文件。.ui文件其实是按照XML格式标记的内容，可以用文本编辑器将.ui文件打开看看。

### ui文件转py代码

因为我们是用Designer工具设计出的界面，并不是用Python代码敲出来的，所以要想真正运行，需要使用pyuic5将ui文件转成py文件。pyuic5.exe默认在%\Scripts\下，比如我的是在：D:\ProgramData\Anaconda3\Scripts\。

打开cmd命令行，切换到ui文件的保存目录。Windows下有个小技巧，可以在目录的地址栏输入cmd，一步切换到当前目录：

![](http://blog.codec.wang/cv2_pyqt5_pyuic_quick_cmd.gif)

然后执行这条指令：

```python
pyuic5 -o mainForm.py using_pyqt_create_ui.ui
```

如果出现pyuic5不是内部命令的错误，说明pyuic5的路径没有在环境变量里，添加下就好了。执行正常的话，就会生成mainForm.py文件，里面应该包含一个名为"Ui_MainWindow"的类。

### 编写逻辑代码

> 经验之谈：mainForm.py文件是根据ui文件生成的，也就是说**重新生成会覆盖掉**。所以为了使界面与逻辑分离，我们需要新建一个逻辑文件。

在同一工作目录下新建一个"mainEntry.py"的文件，存放逻辑代码。代码中的每部分我都写得比较独立，没有封装成函数，便于理解。代码看上去很长，但很简单，可以每个模块单独看，有几个需要注意的地方我做了注释：

```python
import sys
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from mainForm import Ui_MainWindow


class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.camera = cv2.VideoCapture(0)
        self.is_camera_opened = False  # 摄像头有没有打开标记

        # 定时器：30ms捕获一帧
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(30)

    def btnOpenCamera_Clicked(self):
        '''
        打开和关闭摄像头
        '''
        self.is_camera_opened = ~self.is_camera_opened
        if self.is_camera_opened:
            self.btnOpenCamera.setText("关闭摄像头")
            self._timer.start()
        else:
            self.btnOpenCamera.setText("打开摄像头")
            self._timer.stop()

    def btnCapture_Clicked(self):
        '''
        捕获图片
        '''
        # 摄像头未打开，不执行任何操作
        if not self.is_camera_opened:
            return

        self.captured = self.frame

        # 后面这几行代码几乎都一样，可以尝试封装成一个函数
        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        # Qt显示图片时，需要先转换成QImgage类型
        QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def btnReadImage_Clicked(self):
        '''
        从本地读取图片
        '''
        # 打开文件选取对话框
        filename,  _ = QFileDialog.getOpenFileName(self, '打开图片')
        if filename:
            self.captured = cv2.imread(str(filename))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv2.cvtColor(self.captured, cv2.COLOR_BGR2RGB)

            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def btnGray_Clicked(self):
        '''
        灰度化
        '''
        # 如果没有捕获图片，则不执行操作
        if not hasattr(self, "captured"):
            return

        self.cpatured = cv2.cvtColor(self.captured, cv2.COLOR_RGB2GRAY)

        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # 灰度图是单通道，所以需要用Format_Indexed8
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def btnThreshold_Clicked(self):
        '''
        Otsu自动阈值分割
        '''
        if not hasattr(self, "captured"):
            return

        _, self.cpatured = cv2.threshold(
            self.cpatured, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # 阈值分割图也是单通道，也需要用Format_Indexed8
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    @QtCore.pyqtSlot()
    def _queryFrame(self):
        '''
        循环捕获图片
        '''
        ret, self.frame = self.camera.read()

        img_rows, img_cols, channels = self.frame.shape
        bytesPerLine = channels * img_cols

        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCamera.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCamera.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec_())
```

![](http://blog.codec.wang/cv2_pyqt_gui_sample2.jpg)

本文只是抛砖引玉，介绍了PyQt5的简单使用，想要深入学习，可以参考本文开头的参考资料噢(●ˇ∀ˇ●)

## 引用

- [本节源码](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E6%8C%91%E6%88%98%E4%BB%BB%E5%8A%A12%EF%BC%9APyQt5%E7%BC%96%E5%86%99GUI%E7%95%8C%E9%9D%A2	)