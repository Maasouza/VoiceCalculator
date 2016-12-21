from recording import *

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from python_speech_features import mfcc

import scipy.io.wavfile as wav
import math



class VoiceRecognizer(VoiceRecorder):

    def __init__(self,words,centroid_path,chunk=512,frmt=pyaudio.paInt16,rate=16000,channels=1,threshold=500):

        VoiceRecorder.__init__(self,chunk,frmt,rate,channels,threshold)
        self.__words = words
        self.__centroid_path = centroid_path
        self.__centroids = []
        self.__maxs = []
        os.system('cls' if os.name == 'nt' else 'clear')
        self.record_environment_sound(3)
        print("Treshold:", self.getThreshold())
        input("Precione ENTER para continuar")
        os.system('cls' if os.name == 'nt' else 'clear')


    def read_files(self):

        for word in self.__words:
            file = open(self.__centroid_path+"/"+word+".ctrd",'r')
            max = float(file.readline())
            self.__maxs.append(max)
            mfcc = []
            for line in file:
                a = list(map(float,line.split(" ")))
                mfcc.append(a)
            self.__centroids.append(mfcc)

    def compare(self,data_audio):

        min_dist = math.inf
        index = None

        for i in range(len(self.__centroids)):
            dist,p = fastdtw(data_audio,self.__centroids[i],dist=euclidean)
            if((min_dist>dist) and (dist<self.__maxs[i])):
                min_dist = dist
                index = i
        return self.__words[index] if index!=None else None

    def extract_params(self):

        self.record_to_file("temp.wav")
        (rate, sig) = wav.read("temp.wav")
        data_audio = mfcc(sig,rate)
        os.remove("temp.wav")
        return data_audio

