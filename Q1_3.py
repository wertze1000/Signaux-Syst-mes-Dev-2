# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:42:42 2022

@author: qphot
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import Q1_1

# Signal générique 1
def amplitude(t):
    return 1/2

def freq(t):
    return 2

def phi(t):
    return np.pi/4

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

# Signal générique 2
def amplitude_bis(t):
    return 1/1.1

def freq_bis(t):
    return 2

def phi_bis(t):
    return np.pi/2


# ax = plt.axes()

time = np.linspace(0,2,4001)

y_generique = y(amplitude, freq, phi, time)
y_generique_bis = y(amplitude_bis, freq_bis, phi_bis, time)

y_3A = np.zeros(len(time))

for i in range(len(time)):
    y_3A[i] = Q1_1.y1[i] + y_generique[i]
    
y_3B = np.zeros(len(time))
for i in range(len(time)):
    y_3B[i] = Q1_1.y1[i] + y_generique_bis[i]

# plt.plot(time, Q1_1.y1, color = 'blue', label = 'y1')
# plt.plot(time, y_3A, color = 'green', label = 'y3A')
# plt.plot(time, y_3B,color = 'red', label = 'y3B')

# ax.set_ylim(-2 , 2)
# # ax.set_xlim(0 , 2)
# ax.set_ylabel("Amplitude ( - )")
# ax.set_xlabel("t (s)")

# ax.legend()

# plt.show()

