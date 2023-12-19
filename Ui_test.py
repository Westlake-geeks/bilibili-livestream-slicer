# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # 主窗口和网格布局
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 70, 510, 300))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #输入框左侧的文字
        self.roomLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.roomLabel.setObjectName("roomLabel")
        self.gridLayout.addWidget(self.roomLabel, 0, 0, 1, 1)

        # 输入框
        self.roomEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.roomEdit.setObjectName("roomEdit")
        self.gridLayout.addWidget(self.roomEdit, 0, 1, 1, 1)

        # 垂直布局 用于排列按钮
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # add按钮
        self.addButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)

        # start按钮
        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)

        # stop按钮
        self.stopButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)

        # 按钮下方的占位控件
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # 把垂直布局部署到网格
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        # 直播间列表
        self.logPoster = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.logPoster.setObjectName("logPoster")
        self.gridLayout.addWidget(self.logPoster, 1, 1, 1, 1)

        # 主窗口布局相关设置
        MainWindow.setCentralWidget(self.centralwidget)

        # 并没有用到的顶部菜单栏和底部状态栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 设置文字
        self.retranslateUi(MainWindow)

        # 连接槽
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 设置文字
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LiveStreamSlicer"))
        self.addButton.setText(_translate("MainWindow", "add"))
        self.startButton.setText(_translate("MainWindow", "start all"))
        self.stopButton.setText(_translate("MainWindow", "stop all"))
        self.roomLabel.setText(_translate("MainWindow", "roomnumber:"))
