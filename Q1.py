# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:59:38 2022

@author: qphot
"""

import matplotlib.pyplot as plt
import numpy as np

# 20  = x * 0.005 
# 

def y(A, f, phi):
    return A * np.cos(2*np.pi*f - phi)

ax = plt.axes()

time = np.linspace(0,20,4001)

x1 = np.zeros(4001)
for i in range (4001):
    x1[i] = y(1, 1, np.pi/2)

plt.plot(time, x1)

ax.set_ylim(-1.1 , 1.1)   
ax.set_xlim(0 , 20)   
listOf_Xticks = np.arange(0, 20, 1)
plt.xticks(listOf_Xticks)

ax.set_ylabel("y1")
ax.set_xlabel("t (s)")

plt.show()
