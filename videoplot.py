from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np

class VideoPlot(QLabel):
    """ Displays a video-frame as a QLabel
        Drawing is relaized such that the aspect-ratio is kept constant
        and the image fills up all the available space in the layout the VideoPlot is contained in"""
    def __init__(self, video, parent=None, centered = True):
        super(VideoPlot, self).__init__(parent)

        self.video = None

        #set background to black and border to 0
        self.setStyleSheet("background-color: rgb(0,0,0); margin:0px; border:0px solid rgb(0, 255, 0); ")

        self.setMinimumSize(320, 180)#Set minimum size
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)# Set size policy to expanding
        self.setAlignment(Qt.AlignCenter)
        self.update()

    def set_video(video):
        self.video = video

    def resizeEvent(self, event):
        """ Rescales the Pixmap that contains the image when QLabel changes size
            Args:
                event: QEvent
        """
        size = self.size()
        size = QSize(int(size.width()),int(size.height()))
        scaledPix = self.pixmap.scaled(size, Qt.KeepAspectRatio, transformMode = Qt.FastTransformation )
        self.setPixmap(scaledPix)

    def update(self, frame = None):
        """ Upates the pixmap when a new frame is to be displays. Triggers the Qt eventpipeline.
        """

        if type(frame) == type(None):#Init blank frame if no video is set yet
            frame = np.ndarray((9,16,3), dtype = np.byte)
            frame.fill(100)

        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.pixmap = QPixmap(image)
        size = self.size()
        scaledPix = self.pixmap.scaled(size, Qt.KeepAspectRatio, transformMode = Qt.FastTransformation)
        self.setPixmap(scaledPix)

        #QCoreApplication.processEvents()
