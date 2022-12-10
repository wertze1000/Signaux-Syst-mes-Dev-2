# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:59:38 2022
@author: qphot
"""

import matplotlib.pyplot as plt
import numpy as np

def amplitude(t):
    return 1

def freq(t):
    return 1

def phi(t):
    return np.pi/2

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

y1 = y(amplitude, freq, phi, time)

# plt.plot(time, y1)

# ax.set_ylim(-1.1 , 1.1)
# ax.set_ylabel("y1")
# ax.set_xlabel("t (s)")

# plt.show()