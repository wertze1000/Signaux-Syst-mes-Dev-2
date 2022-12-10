# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:40:54 2022

@author: wertz
"""

import matplotlib.pyplot as plt
import numpy as np

def amplitude(t):
    F=[]
    F.append(1/200)
    return np.cos(2*np.pi*F[0]*t)

def freq(t):
    return 1/10 # pour que ça soit lisible

def phi(t):
    return 0

def y(amplitude, freq, phi, t):
    A = []
    F = []
    PHI = []
    Y = []
    for i in range(len(t)):
        A.append(amplitude(i))
        F.append(freq(i))
        PHI.append(phi(i))
        Y.append(A[i]*np.cos(2*np.pi*F[i]*t[i] - PHI[i]))
    return Y



# ax = plt.axes()

time = np.linspace(0,20,4001)

y2 = y(amplitude, freq, phi, time)

# plt.plot(time, y2)

# ax.set_ylim(-1.1 , 1.1)
# ax.set_ylabel("y2")
# ax.set_xlabel("t (s)")

# plt.show()