# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:33:07 2022

@author: Emile
"""

import matplotlib.pyplot as plt
import numpy as np
import waveFunctions as wf
from numpy.fft import fft
#frequency guide:
#alpha:             [8-12Hz] 
#theta:             [4-8Hz]
#theta + spindle:   [10-15Hz]
#delta:             [2-4Hz]
#REM:               [15-60Hz]

sr = 2000                  #Sampling Rate
ts = 1/sr                  #Time interval
time = np.arange(0,200,ts)

#y1 = wf.alphaWave(time)     #near active EEG
#y2 = wf.thetaWave(time)     #slower EEG
#y3 = wf.thetaWaveK(time)   #Theta but with a sleep spindle
#y4 = wf.deltaWave(time)     #theta but with a lower freq
y5 = wf.REM(time)           #dreaming state, awake-like

FFT1 = fft(y5)
N = len(FFT1)
n = np.arange(N)
T = N/sr
freq = n/T

plt.figure(figsize = (12, 6))

plt.plot(freq, np.abs(FFT1))
plt.xlabel('Freq (Hz)')
plt.ylabel('|FFT Amplitude|')
plt.xlim(0,20)
plt.ylim(0,275000)

plt.show()

# plt.plot(time, y1)