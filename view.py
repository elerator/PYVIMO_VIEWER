# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyvimo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PYVIMO(object):
    def setupUi(self, PYVIMO):
        PYVIMO.setObjectName("PYVIMO")
        PYVIMO.resize(909, 614)
        PYVIMO.setMinimumSize(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(PYVIMO)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = VideoPlot(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame1 = QtWidgets.QFrame(self.widget)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.select_roi = QtWidgets.QPushButton(self.frame1)
        self.select_roi.setObjectName("select_roi")
        self.verticalLayout_3.addWidget(self.select_roi)
        self.load = QtWidgets.QPushButton(self.frame1)
        self.load.setObjectName("load")
        self.verticalLayout_3.addWidget(self.load)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.jump_to_end = QtWidgets.QPushButton(self.frame1)
        self.jump_to_end.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/jump_to_end.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jump_to_end.setIcon(icon)
        self.jump_to_end.setObjectName("jump_to_end")
        self.verticalLayout_3.addWidget(self.jump_to_end)
        self.pushButton = QtWidgets.QPushButton(self.frame1)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/jump_to_start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.frame_back = QtWidgets.QPushButton(self.frame1)
        self.frame_back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/frame_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frame_back.setIcon(icon2)
        self.frame_back.setObjectName("frame_back")
        self.verticalLayout_3.addWidget(self.frame_back)
        self.frame_forward = QtWidgets.QPushButton(self.frame1)
        self.frame_forward.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/frame_forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frame_forward.setIcon(icon3)
        self.frame_forward.setObjectName("frame_forward")
        self.verticalLayout_3.addWidget(self.frame_forward)
        self.stop_play = QtWidgets.QPushButton(self.frame1)
        self.stop_play.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_play.setIcon(icon4)
        self.stop_play.setObjectName("stop_play")
        self.verticalLayout_3.addWidget(self.stop_play)
        self.play = QtWidgets.QPushButton(self.frame1)
        self.play.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon5)
        self.play.setObjectName("play")
        self.verticalLayout_3.addWidget(self.play)
        self.horizontalLayout.addWidget(self.frame1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.scrollArea = DataListView(self.splitter)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.QScrollAreaContent = QtWidgets.QWidget()
        self.QScrollAreaContent.setGeometry(QtCore.QRect(0, 0, 893, 50))
        self.QScrollAreaContent.setObjectName("QScrollAreaContent")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.QScrollAreaContent)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.add_datadisplay = QtWidgets.QPushButton(self.QScrollAreaContent)
        self.add_datadisplay.setObjectName("add_datadisplay")
        self.verticalLayout_4.addWidget(self.add_datadisplay)
        self.scrollArea.setWidget(self.QScrollAreaContent)
        self.verticalLayout_2.addWidget(self.splitter)
        PYVIMO.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PYVIMO)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 17))
        self.menubar.setObjectName("menubar")
        PYVIMO.setMenuBar(self.menubar)

        self.retranslateUi(PYVIMO)
        QtCore.QMetaObject.connectSlotsByName(PYVIMO)

    def retranslateUi(self, PYVIMO):
        _translate = QtCore.QCoreApplication.translate
        PYVIMO.setWindowTitle(_translate("PYVIMO", "MainWindow"))
        self.select_roi.setText(_translate("PYVIMO", "Select ROI"))
        self.load.setText(_translate("PYVIMO", "Load ..."))
        self.add_datadisplay.setText(_translate("PYVIMO", "+"))

from datalistview import DataListView
from videoplot import VideoPlot
