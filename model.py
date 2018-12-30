import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PyQt5.QtCore import pyqtSignal, QThread, QObject
import imageio
import time
import tables

import warnings
import re

class VideoModel(QObject):
    """ Wrapper for a video file
        Allows to read frames, set the current frame number, read the start position from the database etc.
    """
    frame = pyqtSignal(np.ndarray)
    framenumber = pyqtSignal(int)
    sliderpos = pyqtSignal(int)

    title_signal = pyqtSignal(str)


    def __init__(self):
        """ Initializes the Video model
            call load manually after connecting slots and signals
        """
        super().__init__()

        self.total_frames = 1
        self.cap = None
        self.filepath = ""
        self.accept_external_control = False

        self.use_opencv = False#To read a frame
        self.title = ""
        self.current_frame = 0

        self.fps = 25.0

        self.video_loader_thread = VideoModel.ImageIOReaderThread(self)
        self.playback_thread = VideoModel.PlaybackThread(self)

    def init_video(self):
        """ Initializes the video. Sets total_framenumber, creates video_reader etc.. """
        self.cap = cv2.VideoCapture(self.filepath)
        self.video_reader = imageio.get_reader(self.filepath)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.keep_playing = True # Finished flag
        self.accept_external_control = True #False during play

    def load(self, filepath):
        """ Changes the videofile that is administered by this VideoModel
            Args:
                dyad: Dyad that specifies the video together with the number of camera
                camera: Number of camera that specifies the video id together with dyad
        """
        self.filepath = filepath
        self.video_loader_thread.start()
        return True

    class ImageIOReaderThread(QThread):
        """ Class for parallel initializing of the VideoModel"""
        signal_done = pyqtSignal(bool)
        def __init__(self, outer_instance):
            super().__init__()
            self.outer_instance = outer_instance

        def run(self):
            self.outer_instance.init_video()
            self.outer_instance.get_frame(True)
            self.outer_instance.set_title()

    class PlaybackThread(QThread):
        def __init__(self, outer_instance):
            super().__init__()
            self.fps = outer_instance.fps
            self.outer_instance = outer_instance

        def run(self):
            self.outer_instance.accept_external_control = False #It is essential to set this here after thread is started!!!
            playback_start = time.time()
            pvrs = 0
            while(self.outer_instance.keep_playing):
                elapsed = time.time() - playback_start
                framenumber = self.outer_instance.playback_start_frame + int((elapsed/(1.0/self.fps)))#Why 600 not 1000?
                if(framenumber > pvrs):
                    self.outer_instance._set_framenumber(framenumber)
                pvrs = framenumber
                #QtCore.QCoreApplication.processEvents()
            self.outer_instance.accept_external_control = True #It is essential to set this here after thread is started!!!


    def start_play(self):
        #self.accept_external_control = False #does not work here has to be in thread
        self.playback_start_frame = self.get_framenumber()
        self.keep_playing = True
        self.playback_thread.start()# Start playback thread
        #self.accept_external_control = True

    def stop_play(self):
        self.keep_playing = False

    def get_camera(self):
        return self.camera

    def get_filepath(self):
        ret = None
        try:
            ret = self.database.dictionary[str(self.dyad)]['video'][str(self.camera)]['path']
        except:
            raise FileNotFoundError("Filepath not found in database")
        return ret


    def set_title(self):
        self.title = "TODO"
        self.title_signal.emit(self.title)

    def get_frame(self, via_emit = False):
        frame = None
        if(self.use_opencv):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES,self.current_frame)
            ret, frame = self.cap.read()
            if(ret == False):
                raise FileNotFoundError("OpenCV couldnt retrive frames")
            else:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            try:
                frame = self.video_reader.get_data(self.current_frame)
            except:
                pass
            if type(frame) == type(None):
                warnings.warn("No frame retrieved")

        if(via_emit):
            if(type(frame) != type(None)):
                self.frame.emit(frame)
        return frame

    def frame_forward(self):
        n = self.get_framenumber()+1
        if(n < self.get_amount_of_frames()):
            self.set_framenumber(n)
        else:
            print("reached end of video")

    def set_framenumber(self, x, inform_slider = True):
        if(self.accept_external_control):
            self._set_framenumber(x, inform_slider)

    def _set_framenumber(self, x, inform_slider = True):
        if(x > self.total_frames):
            self.current_frame = self.total_frames-1
            warnings.warn("x > self.total_frames")
        else:
            self.current_frame = x

        self.framenumber.emit(x)
        if inform_slider:
            self.sliderpos.emit(x)

        try:
            self.video_reader.get_data(self.current_frame)
            self.frame.emit(self.get_frame())
        except Exception as e:
            self.keep_playing = False
            print("couldnt retrieve frame")
            print(e)
        #self.frame.emit(self.video_reader.get_data(self.current_frame))

    def get_framenumber(self):
        return self.current_frame


    def frame_back(self):
        n = self.get_framenumber()-1
        if(n >= 0):
            self.set_framenumber(n)

    def get_amount_of_frames(self):
        return self.total_frames

class DataModel(QObject):
    channeldata = pyqtSignal(np.ndarray)#1d data
    channel_signal = pyqtSignal(int)
    mothistmap = pyqtSignal(np.ndarray)#2d data
    datatype_signal = pyqtSignal(str)#Datatype changed? -> Stacked widget toggles
    pos_in_eeg = pyqtSignal(int)#indicator
    title_signal = pyqtSignal(str)

    def __init__(self):
        """load() must be called by user after signals and slots are connected
            set_filepath() must be called after signals and slots are connected"""

        super().__init__()

        self.data = None
        self.vmrk_path = None
        self.title = ""
        self.channel = None
        self.datatype = None
        self.video_start_in_eeg = None
        self.filepath = None
        self.val_pos_in_eeg = None


    def load(self, filepath = None):
        """ Loads motion or eeg data depending on self.datatype
            emits data (mothistmap or channeldata) and channel in the case of eeg data"""
        if(not self.datatype or not self.filepath):
            if(filepath):
                self.set_filepath(filepath)
            else:
                raise ValueError("Set filepath first or provide it as argument")

        if self.datatype == "eeg":
            self.load_eeg_file()
        elif self.datatype == "motion":
            self.load_motion()
        else:
            raise ValueError("Datatype " + str(self.datatype) + " is not supported")


    def set_filepath(self,filepath):
        """ Sets filepath, datatype and title if path is valid. It is valid if it points to an existant i.e. readable file,
            if it is possible to set the datatype according to the file extension
            and if a vmrk file exists in the case of .eeg files. Throws exceptions otherwise"""

        try:
            with open(filepath) as file:
                pass
        except:
            raise FileNotFoundError("File '" + filepath + "' was not readable/existant")

        if(".eeg" in filepath):
            self.set_datatype("eeg")
        elif(".mot" in filepath):
            self.set_datatype("motion")
        else:
            raise ValueError("Specify a filepath to a .mot or a .eeg file");


        if self.datatype == "eeg": # set title and set vmrk metainfo-file-path. Error when it doesn't exist
            try:
                dir_path = re.match("(.*)/", filepath).group(0)
                filename = re.match(dir_path + "(.*)" + "\..*", filepath).groups()[0]
                vmrk_path = dir_path + filename + ".vmrk"

                self.set_title(filename + "(eeg)")
            except:
                raise NameError("Error occured during parsing of filenames")
            try:
                with open(vmrk_path) as file:
                    pass #open and close to check if file exists
                self.vmrk_path = vmrk_path
            except FileNotFoundError:
                raise FileNotFoundError("Make sure to place the .vmrk file that has the same name as the .eeg file in the same folder\n"
                                        +"file " + vmrk_path + " was not found")


        if self.datatype == "motion":#set title for motion files
            try:
                dir_path = re.match("(.*)/", filepath).group(0)
                print(dir_path)
                filename = re.match(dir_path + "(.*)" + "\..*", filepath).groups()[0]

                self.set_title(filename + "(mot)")
            except:
                raise NameError("Error occured during parsing of filenames")

        self.filepath = filepath

    def set_pos_in_video(self, frame):
        """ Convert position in frames to position in eeg samplepoints. Add offset between start of EEG recording and start of video. """
        if(type(self.video_start_in_eeg) == type(None)):#has to be compared to None if primitive value is stored
            self.set_start_pos()

        pos = 0

        if self.datatype == "eeg":
            pos = self.video_start_in_eeg + (frame/25)*500
        elif self.datatype == "motion":
                pos = frame
        elif type(self.datatype) == type(None):
            raise ValueError("No datatype specified")
        else:
            raise NotImplementedError("Datatype not supported")

        self.val_pos_in_eeg = pos
        self.pos_in_eeg.emit(pos)

    def get_pos_in_eeg():
        if self.val_pos_in_eeg:
            return self.val_pos_in_eeg
        else:
            return 0

    def get_datatype(self):
        return self.datatype

    def set_datatype(self, datatype):
        self.datatype = datatype
        self.datatype_signal.emit(datatype)

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        self.load()#load emits data
        self.channel_signal.emit(channel)

    def set_title(self, title):
        self.title = title
        self.title_signal.emit(title)

    def get_title(self):
        return self.title

    def get_data(self):
        return self.data

    def deleted(self):
        return self.is_deleted

    def change_channel(self, channel):
        assert False
        self.channel = channel
        self.load()


    def load_motion(self):
        try:
            f = tables.open_file(self.filepath, mode='r')
            weighted_hist = np.array(f.root.data, dtype=np.float64)

            weighted_hist = (weighted_hist - np.min(weighted_hist))
            weighted_hist = weighted_hist + 1
            weighted_hist = np.log(weighted_hist)

            #transform to be between 0 and 1
            weighted_hist = (weighted_hist - np.min(weighted_hist)) / (np.max(weighted_hist) - np.min(weighted_hist))

            self.data = weighted_hist
            self.mothistmap.emit(self.data)
        except Exception as e:
            print(e)
        finally:
            f.close()
        return self.data


    def load_eeg_file(self):
        """ Loads eeg file, emits channeldata and channel_signal"""
        if(self.filepath==None):
            print("No filepath set")
            return None

        if(not self.get_channel()):
            self.channel = 0#dont tell anyone yet (see emit below)

        n_channels = 64
        bytes_per_sample = 2 #Because int16

        my_type = np.dtype([("channel"+str(x),np.int16) for x in range(0,n_channels)])
        byte_size = os.path.getsize(self.filepath)

        nFrames =  byte_size // (bytes_per_sample * n_channels);
        data = np.array(np.fromfile(self.filepath,dtype=my_type))["channel"+str(self.get_channel())]

        data = np.array(data, dtype= np.float32)
        data[data==32767] = np.nan
        data[data==-32768] = np.nan
        data[data==-32767] = np.nan

        self.data = data

        self.channeldata.emit(data)
        self.channel_signal.emit(self.get_channel())

    def set_start_pos(self, start_pos_in_datapoints = None):
        """ Computes the beginning of the video measured in datapoints after the start of the eeg-recordings. Saves value in
            self.video_start_in_eeg"""

        if(not type(start_pos_in_datapoints)==type(None)):
            self.video_start_in_eeg = start_pos_in_datapoints
            #self.set_pos_in_video(self.get_framenumber()) # Communicate changes via emit in set_pos_in_video
        else:
            data = self.parse_vmrk(self.vmrk_path)
            #assuming earliest meaningful event is start of video
            pos = data["time"][2]
            self.video_start_in_eeg = int(pos)


        #assert self.video_start_in_eeg

    def parse_vmrk(self, path):
        """ Parses vmrk file and returns a dictionary containing the information.
            The keys denote the kind of data whereas the values are a dictionary
        """

        with open(path) as f:
            content = f.readlines()

        data = {'marker number':[], 'type':[], 'description':[], 'time':[], 'size':[], 'channel':[]}

        entry = 0
        for line in content:
            match = re.match("Mk", line)
            if(match != None):
                markers = re.search("[0-9][0-9]?", line)
                data["marker number"].append(int(markers.group(0)))
                line = line[markers.end():]#use rest of line only next

                markers = re.match("(.*?),",line)
                data["type"].append(markers.group(1)[1:])#Group 1 is exclusive , while group 0 is inclusive ,
                line = line[markers.end():]

                markers = re.search("(.*?),",line)
                data["description"].append(markers.group(1))
                line = line[markers.end():]

                markers = re.search("(.*?),",line)
                data["time"].append('0' + markers.group(1))# '0' + is necessary as some fields are empty
                line = line[markers.end():]

                markers = re.search("(.*?),",line)
                data["size"].append(int('0' + markers.group(1)))
                line = line[markers.end():]

                try:#In the first line there is an additional value we dont want to parse
                    data["channel"].append(int('0' + line))
                except:
                    data["channel"].append(0)
        return data
