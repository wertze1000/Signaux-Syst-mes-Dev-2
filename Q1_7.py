# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 22:07:34 2022

@author: qphot
"""

import matplotlib.pyplot as plt
import numpy as np
import Q1_1

def amplitude_A(t):
    return 12

def amplitude_B(t):
    return 16

def y(amplitude, t):
    A_p = 1
    f_p = 2
    f_m = 1
    
    A_m = []
    Y = []
    for i in range(len(t)):
        A_m.append(amplitude(t))
        Y.append(A_p * np.cos(2 * np.pi * f_p * t[i] + A_m[i] * np.sin(2 * np.pi * f_m * t[i])))
    return Y

ax = plt.axes()

time = np.linspace(0,20,4001)

y_6A = y(amplitude_A, time)
y_6B = y(amplitude_B, time)

# y_phase = Q1_1.y(amplitude_A, time)
# plt.plot(time, y_phase)

# plt.plot(time, y_6A)
plt.plot(time, y_6B)
# plt.plot(time, Q1_1.y1)

ax.set_ylim(-1.1 , 1.1)
ax.set_ylabel("y1")
ax.set_xlabel("t (s)")

plt.show()

# Expliquer le role de A_m
# j'en sais rien, j'ai essayé de comprendre mais je vois pas

# Amplitude modulation: electronic communication
# https://www.google.com/search?q=in+which+field+is+amplitude+modulation+used&ei=pfyUY4a3Ipf4sAew05agBw&ved=0ahUKEwjGndXggfD7AhUXPOwKHbCpBXQQ4dUDCA8&uact=5&oq=in+which+field+is+amplitude+modulation+used&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABMgUIIRCgATIFCCEQoAEyCAghEBYQHhAdOgoIABBHENYEELADOggIABAHEB4QCjoKCAAQBxAeEA8QCjoGCAAQBxAeOhEILhCABBCxAxCDARDHARDRAzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOhEILhCABBCxAxCDARDHARCvAToOCC4QgAQQsQMQxwEQ0QM6BQgAEIAEOgQIABBDOgoIABCxAxCDARBDOg4ILhCABBCxAxCDARDUAjoLCC4QgAQQxwEQrwE6BQguEIAEOgsILhCABBCxAxCDAToHCAAQgAQQCjoICAAQFhAeEA86BggAEBYQHjoHCAAQgAQQEzoKCCEQFhAeEA8QHToECCEQFUoECEEYAEoECEYYAFCiDFj4RmD1SmgDcAF4AIABhAGIAeQRkgEEMTguN5gBAKABAaABAsgBCMABAQ&sclient=gws-wiz-serp

# Phase modulation : transmitting radio waves
# https://www.google.com/search?q=in+which+field+is+phase+modulation+used&ei=wPyUY86tIN-Bi-gP2-WbyAI&ved=0ahUKEwjOjcPtgfD7AhXfwAIHHdvyBikQ4dUDCA8&uact=5&oq=in+which+field+is+phase+modulation+used&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEMgUIABCiBDoKCAAQRxDWBBCwAzoICCEQwwQQoAE6CgghEMMEEAoQoAFKBAhBGABKBAhGGABQhwRY6Alg3gtoAnABeACAAVKIAaoCkgEBNZgBAKABAcgBCMABAQ&sclient=gws-wiz-serp
