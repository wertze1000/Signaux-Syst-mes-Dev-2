# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:22:51 2022

@author: Emile
"""

import matplotlib.pyplot as plt
import numpy as np
import waveFunctions as wf

sr = 2000                  #Sampling Rate
ts = 1/sr                  #Time interval
time = np.arange(0,500,ts)

y1 = wf.alphaWave(time)         #near active EEG
y2 = wf.thetaWave(time)         #slower EEG
y3 = wf.thetaWaveKLong(time)    #Theta but with a sleep spindle
y4 = wf.deltaWave(time)         #theta but with a lower freq
y5 = wf.REM(time)               #dreaming state, awake-like

yCycle = []

y1setZero = (max(y1) + min(y1))/2
y2setZero = (max(y2) + min(y2))/2
y3setZero = (max(y3) + min(y3))/2
y4setZero = (max(y4) + min(y4))/2
y5setZero = (max(y5) + min(y5))/2

spindleSetStop = 0

for i in range(len(time)):
    
    if(time[i] - 100 < 0.01):
        spindleSetStop = i
        break
        
for i in range(len(time)):
    currentTime = time[i]
    
    if(currentTime < 100):
        y1[i] -= y1setZero
        yCycle.append(y1[i])
        
    elif(currentTime >= 100 and currentTime < 200):
        y2[i] -= y2setZero
        yCycle.append(y2[i])
        
    elif(currentTime >= 200 and currentTime < 300):
        y3[i - (spindleSetStop)*2] -= y3setZero
        yCycle.append(y3[i - (spindleSetStop)*2])
        #print("y3 indexes:",i - spindleSetStop*2) #Should be 100009
        
    elif(currentTime >= 300 and currentTime < 400):
        y4[i] -= y4setZero
        yCycle.append(y4[i])
        
    elif(currentTime >= 400 and currentTime <= 500):
        y5[i] -= y5setZero
        yCycle.append(y5[i])

fs = sr
plt.specgram(yCycle, Fs = fs, NFFT = 10*fs, noverlap = None, vmin=-50)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.colorbar()
plt.ylim(0, 30)
plt.show()
















