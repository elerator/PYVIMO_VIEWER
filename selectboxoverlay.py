from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy as np

class SelectBoxOverlay(QObject):
    coordinates = pyqtSignal(QRect)

    def __init__(self, w, parent = None):
        QObject.__init__(self, parent)
        self.overlay = SelectBoxOverlay.Overlay(self, w)

    def eventFilter(self, w, event):
        if event.type() == QEvent.Resize:
            self.overlay.setGeometry(w.geometry())

        if event.type() == QEvent.MouseButtonPress:
            self.overlay.mousePressEvent(event)

        if event.type() == QEvent.MouseMove:
            self.overlay.mouseMoveEvent(event)

        if event.type() == QEvent.MouseButtonRelease:
            self.overlay.mouseReleaseEvent(event)
        return False

    class Overlay(QWidget):
        def __init__(self, outer_instance,parent = None):
            QWidget.__init__(self, parent)
            self.begin = QtCore.QPoint(0,0)
            self.end = QtCore.QPoint(0,0)

            self.box_begin = QtCore.QPoint(0,0)#For the final selection
            self.box_end = QtCore.QPoint(0,0)
            self.parent = parent
            self.outer_instance = outer_instance

        def get_box_coordinates(self):
            """ returns the coordinates of the current selection"""
            return QRect(self.box_begin,self.box_end)

        def paintEvent(self, event):
            qp = QPainter(self)
            br = QBrush(QColor(100, 100, 100, 100))
            qp.setBrush(br)
            qp.drawRect(QRect(self.begin,self.end))

        def mousePressEvent(self, event):
            """ Resets coordinates of the select box. Sets beginning point to mouse pos.
                Args:
                    event: GUI event
            """
            self.begin = event.pos()
            self.end = event.pos()
            self.update()

        def mouseMoveEvent(self, event):
            """ Sets end point to mouse pos. Updates the select_box overlay.
                Args:
                    event: GUI event
            """
            self.end = event.pos()
            self.update()

        def mouseReleaseEvent(self, event):
            """ Copies the current coordinates to respective attributes.
                If permanent_show is set to false, deletes select_box view.
                Args:
                    event: GUI event
            """
            self.box_begin = self.begin
            self.box_end = event.pos()
            self.begin = event.pos()
            self.end = event.pos()

            self.outer_instance.coordinates.emit(self.get_box_coordinates())
