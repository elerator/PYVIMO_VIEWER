from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy as np
import sip


class SelectBoxOverlay(QObject):
    coordinates = pyqtSignal(QRect)

    def __init__(self, w, parent = None):
        QObject.__init__(self, parent)
        self.overlay = SelectBoxOverlay.Overlay(self, w)

        self.other_overlay = None

    def eventFilter(self, w, event):
        if event.type() == QEvent.Resize:
            self.overlay.setGeometry(w.geometry())

        if event.type() == QEvent.MouseButtonPress:
            self.overlay.mousePressEvent(event)

        if event.type() == QEvent.MouseMove:
            self.overlay.mouseMoveEvent(event)

        if event.type() == QEvent.MouseButtonRelease:
            self.overlay.mouseReleaseEvent(event)

        if event.type() == QEvent.Paint:
            #if paintEvent is due to overlay having updated recently: update static display as well (the other one disappears)
            if self.overlay.data_has_changed:
                self.overlay.data_has_changed = False
                if self.other_overlay:
                    sip.delete(self.other_overlay)
                self.other_overlay = SelectBoxOverlay.StaticDisplayOverlay(self.overlay.begin,self.overlay.end,w)
                self.other_overlay.setGeometry(w.geometry())
                self.other_overlay.show()
        return False

    class StaticDisplayOverlay(QWidget):
        def __init__(self, begin, end,parent = None):
            QWidget.__init__(self, parent)
            self.begin = begin
            self.end = end

        def paintEvent(self, event):
            qp = QPainter(self)
            br = QBrush(QColor(100, 100, 100, 100))
            qp.setBrush(br)
            qp.drawRect(QRect(  QtCore.QPoint(self.begin.x()-10,self.begin.y()-10),
                                QtCore.QPoint(self.end.x()-10,self.end.y()-10)))

    class Overlay(QWidget):
        def __init__(self, outer_instance,parent = None):
            QWidget.__init__(self, parent)
            self.begin = QtCore.QPoint(0,0)
            self.end = QtCore.QPoint(0,0)

            self.box_begin = QtCore.QPoint(0,0)#For the final selection
            self.box_end = QtCore.QPoint(0,0)
            self.parent = parent
            self.outer_instance = outer_instance

            self.data_has_changed = True
            self.update()

        def get_box_coordinates(self):
            """ returns the coordinates of the current selection"""
            return QRect(self.box_begin,self.box_end)

        def paintEvent(self, event):
            qp = QPainter(self)
            br = QBrush(QColor(100, 100, 100, 100))
            qp.setBrush(br)
            qp.drawRect(QRect(  QtCore.QPoint(self.begin.x()-10,self.begin.y()-10),
                                QtCore.QPoint(self.end.x()-10,self.end.y()-10)))

        def mousePressEvent(self, event):
            """ Resets coordinates of the select box. Sets beginning point to mouse pos.
                Args:
                    event: GUI event
            """
            self.begin =  event.pos()
            self.end =  event.pos()
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
            self.begin = self.begin
            self.end = event.pos()

            self.data_has_changed = True
            self.outer_instance.coordinates.emit(self.get_box_coordinates())
            self.update()
