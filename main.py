from PyQt5 import QtCore, QtGui, QtWidgets
from view import*
import sys
from datamodel import DataModel
from videomodel import VideoModel
from datacontroller import DataController
from filedialog import FileDialog
from roiselector_controller import ROISelectorController

class MainWindowController:
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PYVIMO()
        self.ui.setupUi(self.window)
        self.c = DataController(self.ui.add_datadisplay, self.ui.verticalLayout_4, videomodel = video)#Add controller such that DataViews may be added to Layout (ScrollArea)


    def make_connections(self, video, model, roiselector):
        """ Make connections of Main Window UI Elements and respective models or controllers"""
        ui = self.ui
        ui.load.clicked.connect(lambda msg: FileDialog.load(video))
        video.frame.connect(ui.frame.update)

        ui.select_roi.clicked.connect(roiselector.show)
        ui.play.clicked.connect(video.start_play)
        ui.stop_play.clicked.connect(video.stop_play)
        ui.frame_forward.clicked.connect(video.frame_forward)
        ui.frame_back.clicked.connect(video.frame_back)

        ui.horizontalSlider.valueChanged.connect(lambda pos: video.set_framenumber(int((pos/1000)*video.total_frames), inform_slider = False))
        video.sliderpos.connect(lambda frame: ui.horizontalSlider.setValue(int((frame/video.total_frames)*1000)))
        #video.framenumber.connect(lambda frame: print(frame))

    def show(self):
        self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    model = DataModel()
    video = VideoModel()
    mw = MainWindowController()
    roi = ROISelectorController(parent = mw.window)


    roi.make_connections(video,model)
    mw.make_connections(video,model,roi)

    mw.show()
    sys.exit(app.exec_())
