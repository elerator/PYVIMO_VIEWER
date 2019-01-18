# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roiselector.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ROISelector(object):
    def setupUi(self, ROISelector):
        ROISelector.setObjectName("ROISelector")
        ROISelector.resize(1171, 554)
        ROISelector.setMaximumSize(QtCore.QSize(1171, 554))
        self.centralwidget = QtWidgets.QWidget(ROISelector)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = VideoPlot(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(960, 540))
        self.frame.setMaximumSize(QtCore.QSize(960, 540))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.coordinates1 = QtWidgets.QLineEdit(self.groupBox)
        self.coordinates1.setObjectName("coordinates1")
        self.horizontalLayout_2.addWidget(self.coordinates1)
        self.coordinates2 = QtWidgets.QLineEdit(self.groupBox)
        self.coordinates2.setObjectName("coordinates2")
        self.horizontalLayout_2.addWidget(self.coordinates2)
        self.coordinates3 = QtWidgets.QLineEdit(self.groupBox)
        self.coordinates3.setObjectName("coordinates3")
        self.horizontalLayout_2.addWidget(self.coordinates3)
        self.coordinates4 = QtWidgets.QLineEdit(self.groupBox)
        self.coordinates4.setObjectName("coordinates4")
        self.horizontalLayout_2.addWidget(self.coordinates4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/frame_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/frame_forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/frames_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/frames_forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.groupBox)
        ROISelector.setCentralWidget(self.centralwidget)

        self.retranslateUi(ROISelector)
        QtCore.QMetaObject.connectSlotsByName(ROISelector)

    def retranslateUi(self, ROISelector):
        _translate = QtCore.QCoreApplication.translate
        ROISelector.setWindowTitle(_translate("ROISelector", "Motion ROI Selector"))
        self.groupBox.setTitle(_translate("ROISelector", "Region of interest (ROI)"))
        self.label.setText(_translate("ROISelector", "Coordinates:"))
        self.label_3.setText(_translate("ROISelector", "Current frame:"))
        self.label_2.setText(_translate("ROISelector", "Comment (optional):"))
        self.label_4.setText(_translate("ROISelector", "Video controls:"))
        self.label_6.setText(_translate("ROISelector", "Frames to skip via (>>) and (<<):"))
        self.lineEdit_6.setText(_translate("ROISelector", "10"))
        self.label_5.setText(_translate("ROISelector", "Save current selection:"))
        self.pushButton.setText(_translate("ROISelector", "Save current selection"))
        self.pushButton_7.setText(_translate("ROISelector", "Load ROIs "))
        self.pushButton_8.setText(_translate("ROISelector", "Save ROI as ..."))
        self.pushButton_2.setText(_translate("ROISelector", "Save ROI"))

from videoplot import VideoPlot