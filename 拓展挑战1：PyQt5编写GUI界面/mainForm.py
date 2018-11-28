# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'using_pyqt_create_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenCamera.setGeometry(QtCore.QRect(20, 220, 75, 23))
        self.btnOpenCamera.setObjectName("btnOpenCamera")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setGeometry(QtCore.QRect(30, 40, 150, 150))
        self.labelCamera.setObjectName("labelCamera")
        self.labelCapture = QtWidgets.QLabel(self.centralwidget)
        self.labelCapture.setGeometry(QtCore.QRect(230, 40, 150, 150))
        self.labelCapture.setObjectName("labelCapture")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(430, 40, 150, 150))
        self.labelResult.setObjectName("labelResult")
        self.btnCapture = QtWidgets.QPushButton(self.centralwidget)
        self.btnCapture.setGeometry(QtCore.QRect(120, 220, 75, 23))
        self.btnCapture.setObjectName("btnCapture")
        self.btnReadImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnReadImage.setGeometry(QtCore.QRect(220, 220, 75, 23))
        self.btnReadImage.setObjectName("btnReadImage")
        self.btnGray = QtWidgets.QPushButton(self.centralwidget)
        self.btnGray.setGeometry(QtCore.QRect(320, 220, 75, 23))
        self.btnGray.setObjectName("btnGray")
        self.btnThreshold = QtWidgets.QPushButton(self.centralwidget)
        self.btnThreshold.setGeometry(QtCore.QRect(420, 220, 101, 23))
        self.btnThreshold.setObjectName("btnThreshold")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnCapture.clicked.connect(MainWindow.btnCapture_Clicked)
        self.btnReadImage.clicked.connect(MainWindow.btnReadImage_Clicked)
        self.btnGray.clicked.connect(MainWindow.btnGray_Clicked)
        self.btnThreshold.clicked.connect(MainWindow.btnThreshold_Clicked)
        self.btnOpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOpenCamera.setText(_translate("MainWindow", "打开摄像头"))
        self.labelCamera.setText(_translate("MainWindow", "摄像头"))
        self.labelCapture.setText(_translate("MainWindow", "捕获图"))
        self.labelResult.setText(_translate("MainWindow", "结果图"))
        self.btnCapture.setText(_translate("MainWindow", "捕获图片"))
        self.btnReadImage.setText(_translate("MainWindow", "打开图片"))
        self.btnGray.setText(_translate("MainWindow", "灰度化"))
        self.btnThreshold.setText(_translate("MainWindow", "阈值分割(Otsu)"))

