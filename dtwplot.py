import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
import numpy as np
import scipy.io.wavfile as wav

from fastdtw import fastdtw
audio1 = "dois/dois0.wav"
audio2 = "mais/mais3.wav"

(rate, sigX) = wav.read(audio1)
(rate, sigY) = wav.read(audio2)


dist,path = fastdtw(sigX, sigY, dist=euclidean)
x = [i[0] for i in path]
y = [i[1] for i in path]


plt.title('DTW PATH')
plt.xlabel(audio1)
plt.ylabel(audio2)
plt.plot(x,y)
plt.axis([-5000, 5000+max(x), -5000, 5000+max(y)])

plt.show()