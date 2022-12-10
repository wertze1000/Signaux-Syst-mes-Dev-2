# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:47:32 2022

@author: qphot
"""

import matplotlib.pyplot as plt
import numpy as np
import Q1_1
import random

time = np.linspace(0,2,4001)

# random renvoie un nombre entre 0,1 
#donc on divise par 10 et on multiplie par pi/2
phi_rand = np.zeros(len(time))
for i in range(len(time)):
    phi_rand[i] = (np.pi / 2 + random.random() / 10 * (np.pi / 2))
    
# https://stackoverflow.com/questions/14313510/how-to-calculate-rolling-moving-average-using-python-numpy-scipy
# msg de yatu
# def moving_average(x, w):
#     return np.convolve(x, np.ones(w), 'valid') / w

# phi_smooth = moving_average(phi_rand, 10)


# # https://www.geeksforgeeks.org/how-to-calculate-moving-averages-in-python/
window_size = 10  
i = 0
phi_smooth = []

while i < len(phi_rand) - window_size + 1:
    window = phi_rand[i : i + window_size]
  
    window_average = round(sum(window) / window_size, 2)
    phi_smooth.append(window_average)
    i += 1

i = len(phi_rand)
while i > len(phi_rand) - window_size + 1:
    window = phi_rand[i : i + window_size]
  
    window_average = round(sum(window) / window_size, 2)
    phi_smooth.append(window_average)
    i -= 1


phi_const = np.zeros(len(time))
for i in range(len(time)):
    phi_const[i] = np.pi / 2

# ax = plt.axes()

# plt.plot(time, phi_rand)
# plt.plot(time, phi_smooth)
# plt.plot(time, phi_const)

# ax.set_ylim(np.pi/2 - 0.2 * np.pi / 2 , np.pi/2 + 0.2 * np.pi / 2)
# ax.set_ylabel("y1")
# ax.set_xlabel("t (s)")

# plt.show()

# Signal générique de Q1.3 
def amplitude(t):
    return 1/2

def freq(t):
    return 2

def phi(t):
    return phi_smooth[t]

y5 = Q1_1.y(amplitude, freq, phi, time)

ax = plt.axes()

plt.plot(time, y5) 
# on observe que le signal présente des pics par rapport au signal initial 

plt.show()



