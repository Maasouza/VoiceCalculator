#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from python_speech_features import mfcc
import scipy.io.wavfile as wav
from scipy.stats._continuous_distns import maxwell_gen

from recording import *

os.system('cls' if os.name == 'nt' else 'clear')

vt = VoiceTrainer(512,pyaudio.paInt16,16000,1)

vt.record_environment_sound(3)

print("Threshold definido em:",vt.getThreshold())

input("Precione ENTER para continuar")
os.system('cls' if os.name == 'nt' else 'clear')


print("----\tCriando base para teste")

data = input("Insira o nome das pastas separadas por espaço\nAdicione por ultimo o numero de gravações\n")
data = data.split(" ")

folders = data[:-1]

for folder in folders:

    if (not os.path.exists(folder)):
        os.mkdir(folder)
if(len(data)>1):
    record_times = int(data[-1])
else:
    print("Parametros invalidos")
    exit()

"""for folder in folders:
    for i in range(record_times):
        record_path = folder+"/"+folder+str(i)+".wav"
        vt.record_to_file(record_path)"""


dist = [[0]*record_times for x in range(record_times)]
mfccs = [None] * record_times
if(not os.path.exists("centroid")):
    os.mkdir("centroid")

for folder in folders:
    for k in range(record_times):
        record = folder+"/"+folder+str(k)+".wav"
        (rate,sig) = wav.read(record)
        mfccs[k] = mfcc(sig,rate)
    for i in range(record_times):
        for j in range(i,record_times):
            distance, path = fastdtw(mfccs[i],mfccs[j], dist=euclidean)
            dist[i][j] = distance
            dist[j][i] = distance
    sum = [0] * record_times
    min_index = None
    min_value = math.inf
    max_value = 0
    for i in range(record_times):
        for j in range(record_times):
            sum[i]+=dist[i][j]
            if (max_value < dist[i][j]):
                max_value = dist[i][j]
        if(min_value>=sum[i]):
            min_value = sum[i]
            min_index = i

    centroid = mfccs[min_index]
    file = open("centroid/"+folder+".ctrd","w")
    file.write(str(max_value))
    for i in range(len(centroid)):
        file.write("\n")
        for j in range(len(centroid[i])):
            if(j!=len(centroid[i])-1):
                file.write(str(centroid[i][j])+" ")
            else:
                file.write(str(centroid[i][j]))


