# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_roiselector.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ROISelector(object):
    def setupUi(self, ROISelector):
        ROISelector.setObjectName("ROISelector")
        ROISelector.resize(1171, 554)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ROISelector.sizePolicy().hasHeightForWidth())
        ROISelector.setSizePolicy(sizePolicy)
        ROISelector.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(ROISelector)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = VideoPlot(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(960, 540))
        self.frame.setMaximumSize(QtCore.QSize(960, 540))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setObjectName("frame1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.coordinates1 = QtWidgets.QLineEdit(self.frame1)
        self.coordinates1.setObjectName("coordinates1")
        self.horizontalLayout_2.addWidget(self.coordinates1)
        self.coordinates2 = QtWidgets.QLineEdit(self.frame1)
        self.coordinates2.setObjectName("coordinates2")
        self.horizontalLayout_2.addWidget(self.coordinates2)
        self.coordinates3 = QtWidgets.QLineEdit(self.frame1)
        self.coordinates3.setObjectName("coordinates3")
        self.horizontalLayout_2.addWidget(self.coordinates3)
        self.coordinates4 = QtWidgets.QLineEdit(self.frame1)
        self.coordinates4.setObjectName("coordinates4")
        self.horizontalLayout_2.addWidget(self.coordinates4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.current_frame = QtWidgets.QLineEdit(self.frame1)
        self.current_frame.setObjectName("current_frame")
        self.verticalLayout.addWidget(self.current_frame)
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comment = QtWidgets.QTextEdit(self.frame1)
        self.comment.setObjectName("comment")
        self.verticalLayout.addWidget(self.comment)
        self.line_2 = QtWidgets.QFrame(self.frame1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.frame_back = QtWidgets.QPushButton(self.frame1)
        self.frame_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/frame_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frame_back.setIcon(icon)
        self.frame_back.setObjectName("frame_back")
        self.verticalLayout.addWidget(self.frame_back)
        self.frame_forward = QtWidgets.QPushButton(self.frame1)
        self.frame_forward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/frame_forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frame_forward.setIcon(icon1)
        self.frame_forward.setObjectName("frame_forward")
        self.verticalLayout.addWidget(self.frame_forward)
        self.frames_back = QtWidgets.QPushButton(self.frame1)
        self.frames_back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/frames_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frames_back.setIcon(icon2)
        self.frames_back.setObjectName("frames_back")
        self.verticalLayout.addWidget(self.frames_back)
        self.frames_forward = QtWidgets.QPushButton(self.frame1)
        self.frames_forward.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/frames_forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frames_forward.setIcon(icon3)
        self.frames_forward.setObjectName("frames_forward")
        self.verticalLayout.addWidget(self.frames_forward)
        self.label_6 = QtWidgets.QLabel(self.frame1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.skip_thismany = QtWidgets.QLineEdit(self.frame1)
        self.skip_thismany.setObjectName("skip_thismany")
        self.verticalLayout.addWidget(self.skip_thismany)
        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.frame1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.save_current_selection = QtWidgets.QPushButton(self.frame1)
        self.save_current_selection.setObjectName("save_current_selection")
        self.verticalLayout.addWidget(self.save_current_selection)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.save_roi_as = QtWidgets.QPushButton(self.frame1)
        self.save_roi_as.setObjectName("save_roi_as")
        self.verticalLayout.addWidget(self.save_roi_as)
        self.save_roi = QtWidgets.QPushButton(self.frame1)
        self.save_roi.setObjectName("save_roi")
        self.verticalLayout.addWidget(self.save_roi)
        self.horizontalLayout.addWidget(self.frame1)
        ROISelector.setCentralWidget(self.centralwidget)

        self.retranslateUi(ROISelector)
        QtCore.QMetaObject.connectSlotsByName(ROISelector)

    def retranslateUi(self, ROISelector):
        _translate = QtCore.QCoreApplication.translate
        ROISelector.setWindowTitle(_translate("ROISelector", "Motion ROI Selector"))
        self.label.setText(_translate("ROISelector", "Coordinates:"))
        self.label_3.setText(_translate("ROISelector", "Current frame:"))
        self.label_2.setText(_translate("ROISelector", "Comment (optional):"))
        self.label_4.setText(_translate("ROISelector", "Video controls:"))
        self.label_6.setText(_translate("ROISelector", "Frames to skip via (>>) and (<<):"))
        self.skip_thismany.setText(_translate("ROISelector", "10"))
        self.label_5.setText(_translate("ROISelector", "Save current selection:"))
        self.save_current_selection.setText(_translate("ROISelector", "Save current selection"))
        self.pushButton_7.setText(_translate("ROISelector", "Load ROIs "))
        self.save_roi_as.setText(_translate("ROISelector", "Save ROI as ..."))
        self.save_roi.setText(_translate("ROISelector", "Save ROI"))

from videoplot import VideoPlot
