# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:49:14 2022

@author: Emile
"""
import matplotlib.pyplot as plt
import numpy as np
import waveFunctions as wf

time = np.linspace(0,20,4001)

y2 = wf.alphaWave(time)    #near active EEG
y3 = wf.thetaWave(time)    #slower EEG
y4 = wf.thetaWaveK(time)   #Theta but with a sleep spindle
y5 = wf.deltaWave(time)    #theta but with a lower freq
y6 = wf.REM(time)          #dreaming state, awake-like

fig = plt.figure(figsize = (20, 10))

ax1 = fig.add_subplot(511)
plt.ylabel('Voltage [μV]')
plt.yticks(np.linspace(min(y2), max(y2), 3))
plt.xticks(np.linspace(0,20,21))


ax2 = fig.add_subplot(512)
plt.ylabel('Voltage [μV]')
plt.yticks(np.linspace(min(y3), max(y3), 3))
plt.xticks(np.linspace(0,20,21))


ax3 = fig.add_subplot(513)
plt.ylabel('Voltage [μV]')
plt.yticks(np.linspace(min(y4), max(y4), 3))
plt.xticks(np.linspace(0,20,21))

ax4 = fig.add_subplot(514)
plt.ylabel('Voltage [μV]')
plt.yticks(np.linspace(min(y5), max(y5), 3))
plt.xticks(np.linspace(0,20,21))

ax5 = fig.add_subplot(515)
plt.ylabel('Voltage [μV]')
plt.yticks(np.linspace(min(y6), max(y6), 3))
plt.xticks(np.linspace(0,20,21))

plt.xlabel('Time [s]')
ax1.plot(time, y2)
ax2.plot(time, y3)
ax3.plot(time, y4)
ax4.plot(time, y5)
ax5.plot(time, y6)
