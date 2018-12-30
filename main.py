from PyQt5 import QtCore, QtGui, QtWidgets
from view import*
from model import*
from datacontroller import DataController
from filedialog import FileDialog

def connect(ui, video, model):
    """ Make connections of Main Window UI Elements and respective models or controllers"""
    ui.load.clicked.connect(lambda msg: FileDialog.load(video))
    video.frame.connect(ui.frame.update)

    ui.play.clicked.connect(video.start_play)
    ui.stop_play.clicked.connect(video.stop_play)
    ui.frame_forward.clicked.connect(video.frame_forward)
    ui.frame_back.clicked.connect(video.frame_back)

    ui.horizontalSlider.valueChanged.connect(lambda pos: video.set_framenumber(int((pos/1000)*video.total_frames), inform_slider = False))
    video.sliderpos.connect(lambda frame: ui.horizontalSlider.setValue(int((frame/video.total_frames)*1000)))
    #video.framenumber.connect(lambda frame: print(frame))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PYVIMO = QtWidgets.QMainWindow()
    ui = Ui_PYVIMO()
    ui.setupUi(PYVIMO)

    model = DataModel()
    video = VideoModel()
    c = DataController(ui.add_datadisplay, ui.verticalLayout_4, videomodel = video)#Add controller such that DataViews may be added to ScrollArea
    connect(ui, video, model)

    PYVIMO.show()
    sys.exit(app.exec_())
