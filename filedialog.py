from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from datamodel import DataModel
from videomodel import VideoModel

class FileDialog():
    @staticmethod
    def load(file):
        if isinstance(file, DataModel):
            FileDialog.load_data(file)
        elif isinstance(file, VideoModel):
            FileDialog.load_video(file)

    @staticmethod
    def load_video(video):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "",
                                                  "Mp4 Video (*.mp4);; AVI Video (*.avi);; MOV Video files (*.mov);; MPEG Video files (*.mpeg);;",
                                                  options=options)
        if fileName:
            video.load(fileName)

    @staticmethod
    def load_data(model):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "",
                                                  "EEG files (*.eeg);;Motion files(*.mot);;Motion files(*.hdf5);;",
                                                  options=options)
        if fileName:
            model.load(fileName)
