#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from python_speech_features import mfcc
import scipy.io.wavfile as wav

from recording import *


class VoiceTrainer(VoiceRecorder):

    def __init__(self,folders,record_times,centroid_path,chunk=1024,frmt=pyaudio.paInt16,rate=44100,channels=1,threshold=500):

        VoiceRecorder.__init__(self,chunk,frmt,rate,channels,threshold)

        self.__folders = folders
        self.__record_times = record_times
        self.__centroid_path = centroid_path
        self.__mfccs = [None] * record_times
        self.__dist = [[0]*record_times for x in range(record_times)]

        if (not os.path.exists(centroid_path)):
            os.mkdir(centroid_path)
        self.record_environment_sound(3)
        self.create_folders(folders)
        self.create_database(folders,record_times)

    def create_folders(self,folders):
        for folder in folders:
            if (not os.path.exists(folder)):
                os.mkdir(folder)

    def create_database(self,folders,record_times):
        for folder in folders:
            for i in range(record_times):
                record_path = folder + "/" + folder + str(i) + ".wav"
                self.record_to_file(record_path)

    def generate_centroid_files(self):
        for folder in self.__folders:
            for k in range(self.__record_times):
                record = folder+"/"+folder+str(k)+".wav"
                (rate,sig) = wav.read(record)
                self.__mfccs[k] = mfcc(sig,rate)
            for i in range(self.__record_times):
                for j in range(i,self.__record_times):
                    distance, path = fastdtw(self.__mfccs[i],self.__mfccs[j], dist=euclidean)
                    self.__dist[i][j] = distance
                    self.__dist[j][i] = distance
            sum = [0] * self.__record_times
            min_index = None
            min_value = math.inf
            max_value = 0
            for i in range(self.__record_times):
                for j in range(self.__record_times):
                    sum[i]+=self.__dist[i][j]
                    if (max_value < self.__dist[i][j]):
                        max_value = self.__dist[i][j]
                if(min_value>=sum[i]):
                    min_value = sum[i]
                    min_index = i

            centroid = self.__mfccs[min_index]
            file = open(self.__centroid_path+"/"+folder+".ctrd","w")
            file.write(str(max_value))
            for i in range(len(centroid)):
                file.write("\n")
                for j in range(len(centroid[i])):
                    if(j!=len(centroid[i])-1):
                        file.write(str(centroid[i][j])+" ")
                    else:
                        file.write(str(centroid[i][j]))


