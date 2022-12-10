# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:42:24 2022

@author: qphot
"""

import matplotlib.pyplot as plt
import numpy as np
import Q1_1

# Bruit
def amplitude(t):
    return 0.1

def freq(t):
    return 100

def phi(t):
    return 0



# ax = plt.axes()

time = np.linspace(0,20,4001)

y_bruit = Q1_1.y(amplitude, freq, phi, time)

y4 = np.zeros(len(time))

for i in range(len(time)):
    y4[i] = Q1_1.y1[i] + y_bruit[i]

# plt.plot(time, y4)
# # on observe que le signal n'est plus aussi lisse que le signal de départ

# ax.set_ylim(-1.1 , 1.1)
# ax.set_ylabel("y1")
# ax.set_xlabel("t (s)")

# plt.show()