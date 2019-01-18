from ui_roiselector import Ui_ROISelector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *

from selectboxoverlay import *

class ROISelectorController:
    def __init__(self, parent = None):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ROISelector()
        self.ui.setupUi(self.window)

        self.box = SelectBoxOverlay(self.ui.frame)

        self.ui.frame.installEventFilter(self.box)

    def show(self):
        self.window.show()


    def make_connections(self, video, model):
        ui = self.ui
        box = self.box

        video.frame.connect(ui.frame.update)#video changes position -> show new frame

        box.coordinates.connect(self.update_coordinates)#display currently selected coordina

    def update_coordinates(self, coordinates):
        self.ui.coordinates1.setText(str(coordinates.top()*2))
        self.ui.coordinates2.setText(str(coordinates.left()*2))
        self.ui.coordinates3.setText(str(coordinates.bottom()*2))
        self.ui.coordinates4.setText(str(coordinates.right()*2))
