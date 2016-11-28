#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import byteorder
from array import array
from struct import pack

import os
import pyaudio
import wave

class VoiceRecorder():


    def __init__(self,chunk=1024,frmt=pyaudio.paInt16,rate=44100,channels=1,threshold=500,):
        self.__THRESHOLD = threshold
        self.__CHUNK_SIZE = chunk
        self.__FORMAT = frmt
        self.__RATE = rate
        self.__CHANNELS = channels

    def is_silent(self,sound):
        return max(sound) < self.__THRESHOLD

    def normalize(self,sound):
        MAXIMUM = 16384 #Max of signed int16
        c = float(MAXIMUM)/max(abs(i) for i in sound)

        r = array('h') #
        for i in sound:
            r.append(int(i*c))
        return r

    def cut(self,sound):
        snd_started = False
        r = array('h')

        for i in sound:
            if not snd_started and abs(i) > self.__THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    def trim(self,sound):

        sound = self.cut(sound)
        sound.reverse()
        sound = self.cut(sound)
        sound.reverse()

        return sound

    def add_silence(self,sound, seconds):
        r = array('h', [0 for i in range(int(seconds*self.__RATE))])
        r.extend(sound)
        r.extend([0 for i in range(int(seconds*self.__RATE))])
        return r

    def record(self):

        p = pyaudio.PyAudio()
        stream = p.open(
            format = self.__FORMAT,
            channels = self.__CHANNELS,
            rate = self.__RATE,
            input = True,
            output =True,
            frames_per_buffer = self.__CHUNK_SIZE)

        num_silent = 0
        snd_started = False

        r = array('h')

        while 1:
            sound = array('h', stream.read(self.__CHUNK_SIZE))
            if byteorder == 'big':
                sound.byteswap()
            r.extend(sound)

            silent = self.is_silent(sound)

            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                print("Gravando...")
                snd_started = True

            if snd_started and num_silent > 30:
                print("Gravação concluida...")
                break

        width = p.get_sample_size(self.__FORMAT)
        stream.stop_stream()
        stream.close()
        p.terminate()

        r = self.normalize(r)
        r = self.trim(r)
        r = self.add_silence(r, 0.5)
        return width, r

    def record_to_file(self,path):

        width, data = self.record()
        data = pack('<' + ('h'*len(data)), *data)

        wf = wave.open(path, 'wb')
        wf.setnchannels(self.__CHANNELS)
        wf.setsampwidth(width)
        wf.setframerate(self.__RATE)
        wf.writeframes(data)
        wf.close()

    def setTreshold(self,value):
        self.__THRESHOLD = value

    def getThreshold(self):
        return self.__THRESHOLD

    def record_environment_sound(self,seconds):
        print("Fique em silencio para a captura do som ambiente\n\nPrecione ENTER para iniciar a captura")
        input()
        p = pyaudio.PyAudio()

        stream = p.open(format = self.__FORMAT,
                        channels = self.__CHANNELS,
                        rate = self.__RATE,
                        input = True,
                        frames_per_buffer = self.__CHUNK_SIZE)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gravando...")

        frames = []
        sound_max = 0
        mean = 0
        t = 0
        for i in range(0, int(self.__RATE / self.__CHUNK_SIZE * seconds)):
            sound = array('h', stream.read(self.__CHUNK_SIZE))
            if max(list(map(abs,sound)))> sound_max:
                sound_max = max(sound)
            frames.append(sound)
        print("Gravação concluida.")

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open("env.wav", 'wb')
        wf.setnchannels(self.__CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.__FORMAT))
        wf.setframerate(self.__RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        self.setTreshold(sound_max)
