from model import DataModel
from dataview import DataView

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from filedialog import FileDialog

import sip

class DataController:
    def __init__(self, add_button, layout, videomodel, datamodels =[]):
        self.add_button = add_button#
        self.layout = layout

        self.add_button.clicked.connect(self.add_data_display)
        print("DataListController init")


        self.videomodel = videomodel
        self.datamodels = datamodels#Use self.add_data_display() tQtGui.QListWidget(self.centralwidget)o append
        self.dataviews = []

        for model in datamodels:
            self.add_data_display(model)

    def set_start_pos_adapter(self, msg, model):
        """ Converts the string entered in a lineEdit to an int if possible and sets the start position of the video relative to the EEG accordingly.
            Used in add_data_display(...) below.
        """
        try:
            pos = int(msg)
            model.set_start_pos(pos)
        except:
            pass

    def add_data_display(self, model = None):
        """ Adds datadisplay
            Args:
                model: Model to be added to centralwidget as well as to list of models
        """
        print("add_data_display")

        #Create new MODEL and append it to self.models
        if type(model) != type(DataModel()):#Via button (+) press some message (False) arrives
            model = DataModel()

        self.datamodels.append(model)

        #Create VIEW and add it (widget) to layout
        optiondisplay = DataView()
        self.dataviews.append(optiondisplay)
        self.layout.addWidget(optiondisplay)

        optiondisplay.close.clicked.connect(lambda msg: self.delete(optiondisplay, self.layout) )
        optiondisplay.load.clicked.connect(lambda msg: FileDialog.load(model))
        optiondisplay.close_1.clicked.connect(lambda msg: self.delete(optiondisplay, self.layout) )
        optiondisplay.load_1.clicked.connect(lambda msg: FileDialog.load(model))

        optiondisplay.lineEdit.textChanged.connect(lambda msg: self.set_start_pos_adapter(msg, model))



        #Subscribe
        #self.videomodel.eeg_pos.connect(optiondisplay.data_plot.update)
        #self.videomodel.framenumber.connect(optiondisplay.mothist_plot.update)
        model.channeldata.connect(optiondisplay.graphicsView.print_data)#TODO rename to dataplot and also in designer

        self.videomodel.framenumber.connect(model.set_pos_in_video)#triggers pos in eeg
        model.pos_in_eeg.connect(optiondisplay.graphicsView.update_indicator)
        #model.mothistmap.connect(optiondisplay.mothist_plot.print_data)

        self.redraw_button()

    def delete(self, widget, layout):
        """ Deletes a model from the widget (by reinitializing the centralwidget) and the list of models  """
        #child_layout = widget.findChildren(QLayout, options = Qt.FindDirectChildrenOnly)
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
        layout.removeWidget(widget)
        sip.delete(widget)#calls c++ delete
        del self.dataviews[self.dataviews.index(widget)]


    def redraw_button(self):
        """ Adds button at end of list that may be used to add additional DataDisplays """
        #if len(self.datamodels) == 0:#In this case the button is deleted completely as there is no reference to it
        #    self.add_button = QtGui.QPushButton(self) #Draw (+) button to add data displays
        #    self.add_button.setText("+")
        #    self.addDataDisplays.clicked.connect(self.add_data_display)
        self.layout.removeWidget(self.add_button)
        self.layout.addWidget(self.add_button)
