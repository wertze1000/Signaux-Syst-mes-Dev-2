# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:11:30 2022

@author: qphot
"""

import matplotlib.pyplot as plt
import numpy as np
import Q1_3
import scipy

ax = plt.axes()

time = np.linspace(0,1,4001)

y_3A_fft = scipy.fft.fft(Q1_3.y_3A)
freq = scipy.fft.fftfreq(time.shape[-1])

plt.plot(freq, y_3A_fft, label = 'FFT en fonction de la fréquence')

ax.set_ylabel("FFT en amplitude de y3A")
ax.set_xlabel("Fréquence (Hz)")
ax.set_label('Label via method')

ax.legend()

