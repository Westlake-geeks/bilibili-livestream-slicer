# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

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

        self.roomEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.roomEdit.setObjectName("roomEdit")
        self.gridLayout.addWidget(self.roomEdit, 0, 1, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.addButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)

        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)

        self.stopButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.roomLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.roomLabel.setObjectName("roomLabel")
        self.gridLayout.addWidget(self.roomLabel, 0, 0, 1, 1)
        
        #self.logPoster = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        #self.logPoster.setObjectName("logPoster")
        #self.gridLayout.addWidget(self.logPoster, 1, 1, 1, 1)
        self.logPoster = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.logPoster.setObjectName("logPoster")
        self.gridLayout.addWidget(self.logPoster, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LiveStreamSlicer"))
        self.addButton.setText(_translate("MainWindow", "add"))
        self.startButton.setText(_translate("MainWindow", "start all"))
        self.stopButton.setText(_translate("MainWindow", "stop all"))
        self.roomLabel.setText(_translate("MainWindow", "roomnumber:"))
