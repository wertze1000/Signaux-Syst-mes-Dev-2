# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:29:55 2022

@author: Emile
"""
import numpy as np

#EEG Voltage range: [25; 200]
#Wave parameter functions:
def amplitude(t):
    F=[]
    F.append(1/200)
    return np.cos(2*np.pi*F[0]*t)

def freq(t):
    return 1/10

def phi(t):
    return 0

#Standard wave function:
def stdWave(amplitude, freq, phi, t):
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

#Relaxed wakefullness function:

def alphaWave(t):
    #[25;35]μV (microVolts)
    Y = []
    time = t
    
    def Amp1(t):
        F = []
        F.append(1/20000)
        return (0.2)*np.cos(2*np.pi*F[0]*t)
    
    def Amp2(t):
        F = []
        F.append(1/20000)
        return ((0.3)*np.cos(2*np.pi*F[0]*t)) - ((0.2)*np.cos(2*np.pi*F[0]*t))
    
    def Amp3(t):
        F = []
        F.append(1/10000)
        return ((0.1)*np.cos(2*np.pi*F[0]*t))
    
    
    def Freq1(t):
        return 8
    
    def Freq2(t):
        return 10
    
    def Phase1(t):
        return 0
    
    def Phase2(t):
        return (np.pi)/2
    
    def Phase3(t):
        return np.pi*np.cos(2*(1/70)*t)
    
    #SleepSpindle call:
    Y1 = stdWave(Amp1, Freq1, Phase1, time)
    Y2 = stdWave(Amp2, Freq2, Phase1, time)
    Y3 = stdWave(Amp3, Freq2, Phase3, time)
    
    for i in range(len(t)):
        Y.append(Y1[i] + Y2[i] - Y3[i])
        
    print('ALPHA    : minimum =', min(Y), 'maximum =', max(Y))
    return Y

def thetaWave(t):
#[60;90]μV (microVolts)
    Y = []
    time = t
    
    def amp1(t):
        F = []
        F.append(1/25000)
        return (0.2)*np.cos(2*np.pi*F[0]*t)
    
    def freq1(t):
        return 3.865
    
    def phase1(t):
        return 0.2
    
    def amp2(t):
        F=[]
        F.append(1/12500)
        return (0.1)*np.cos(2*np.pi*F[0]*t) + (0.2)*np.cos(2*np.pi*F[0]*t)
    
    def freq2(t):
        return 6.25
    
    def phase2(t):
        return (np.pi/2)+0.1
    
    def amp3(t):
        F=[]
        F.append(1/125)
        return (0.1)*np.cos(2*np.pi*F[0]*t)
    
    def freq3(t):
        return 4.8
    
    def phase3(t):
        return 0.3
    
    def amp4(t):
        F = []
        F.append(11)
        return (0.1)*np.cos(2*np.pi*F[0]*t)
    
    def freq4(t):
        return 5.3
    
    def phase4(t):
        return (np.pi/2) - 0.2
    
    
    Y1 = stdWave(amp1, freq1, phase1, time)
    Y2 = stdWave(amp2, freq2, phase2, time)
    Y3 = stdWave(amp3, freq3, phase3, time)
    Y4 = stdWave(amp4, freq4, phase4, time)
    
    for i in range(len(t)):
        Y.append(Y1[i] + Y2[i] + Y3[i] + Y4[i]**4)
        
    print('THETA    : minimum =', min(Y), 'maximum =', max(Y))
    return Y

def thetaWaveK(t):
#[25;35]μV (microVolts)
    Y = []
    time = t
    
    def amp1(t):
        F = []
        F.append(1/20000)
        return (0.3)*np.cos(2*np.pi*F[0]*t)
    
    def freq1(t):
        return 3.865
    
    def phase1(t):
        return 0.2
    
    def amp2(t):
        F=[]
        F.append(1/10000)
        return (0.1)*np.cos(2*np.pi*F[0]*t) + (0.2)*np.cos(2*np.pi*F[0]*t)
    
    def freq2(t):
        return 6.25
    
    def phase2(t):
        return (np.pi/2)+0.1
    
    def amp3(t):
        F=[]
        F.append(1/150)
        return (0.1)*np.cos(2*np.pi*F[0]*t)
    
    def freq3(t):
        return 4.8
    
    def phase3(t):
        return 0.3
    
    def amp4(t):
        F = []
        F.append(10)
        return (0.1)*np.cos(2*np.pi*F[0]*t)
    
    def freq4(t):
        return 5.3
    
    def phase4(t):
        return (np.pi/2) - 0.2
    
    def sleepSpindle(t):
        time = t
        def ampSpindle(t):
            F = []
            F.append(1/70)
            return (0.8)*np.cos(2*np.pi*F[0]*t)
        
        def freqSpindle(t):
            return 13; #Spindle Freq setting (11-16 Hz)
    
        def phaseSpindle(t):
            return (np.pi/2)+0.2
        
            
        return stdWave(ampSpindle, freqSpindle, phaseSpindle, time)
    
    Y1 = stdWave(amp1, freq1, phase1, time)
    Y2 = stdWave(amp2, freq2, phase2, time)
    Y3 = stdWave(amp3, freq3, phase3, time)
    Y4 = stdWave(amp4, freq4, phase4, time)
    Spindle = sleepSpindle(time)
    
    spindleInterval = np.linspace(10,16,1200)
    
    for i in range(len(t)):
        
        if(t[i] >= 11 and t[i] <= 12):
            
            if(t[i] - spindleInterval[i - 2001] < 0.01):
                Y.append(Spindle[i])
                
        else:
            Y.append(Y1[i] + Y2[i] + Y3[i] + Y4[i]**4)
      
    print('THETAK   : minimum =', min(Y), 'maximum =', max(Y))
    return Y

def deltaWave(t):
#[110;180]μV (microVolts)
    Y = []
    time = t
    
    def amp1(t):
        F = []
        F.append(1/25000)
        return (0.15)*np.cos(2*np.pi*F[0]*t)
    
    def freq1(t):
        return 3
    
    def phase1(t):
        return 0
    
    def amp2(t):
        F=[]
        F.append(1/1000)
        return - (0.1)*np.cos(2*np.pi*F[0]*t) + (0.2)*np.cos(2*np.pi*F[0]*t)
    
    def freq2(t):
        return 2
    
    def phase2(t):
        return np.pi/2
    
    def amp3(t):
        F=[]
        F.append(1/150)
        return (0.1)*np.cos(2*np.pi*F[0]*t)
    
    def freq3(t):
        return 2.2
    
    def phase3(t):
        return 0.4
    
    def amp4(t):
        F = []
        F.append(1/10)
        return (0.2)*np.cos(2*np.pi*F[0]*t) - (0.1)*np.sin(2*np.pi*F[0]*t)
    
    def freq4(t):
        return 3.2
    
    def phase4(t):
        return 0.6
    
    
    Y1 = stdWave(amp1, freq1, phase1, time)
    Y2 = stdWave(amp2, freq2, phase2, time)
    Y3 = stdWave(amp3, freq3, phase3, time)
    Y4 = stdWave(amp4, freq4, phase4, time)
    
    for i in range(len(t)):
        Y.append(Y1[i] + Y2[i] + Y3[i] + Y4[i]**4)
        Y[i] /= 1
        Y[i] *= 120
        Y[i] += 150
    print('DELTA    : minimum =', min(Y), 'maximum =', max(Y))
    #[110;180]μV (microVolts)
    print('OK')
    return Y

def REM(t):
#[25;35]μV (microVolts)
    Y = []
    time = t
    
    def Amp1(t):
        F = []
        F.append(1/25000)
        return (0.2)*np.cos(2*np.pi*F[0]*t)
    
    def Amp2(t):
        F = []
        F.append(1/20000)
        return ((0.3)*np.cos(2*np.pi*F[0]*t)) - ((0.2)*np.cos(2*np.pi*F[0]*t))
    
    def Amp3(t):
        F = []
        F.append(1/12000)
        return ((0.1)*np.cos(2*np.pi*F[0]*t))
    
    
    def Freq1(t):
        return 9
    
    def Freq2(t):
        return 10
    
    def Phase1(t):
        return 0.2
    
    def Phase2(t):
        return (np.pi)/2
    
    def Phase3(t):
        return np.pi*np.cos(2*(1/70)*t)
    
    #SleepSpindle call:
    Y1 = stdWave(Amp1, Freq1, Phase1, time)
    Y2 = stdWave(Amp2, Freq2, Phase1, time)
    Y3 = stdWave(Amp3, Freq2, Phase3, time)
    
    for i in range(len(t)):
        Y.append(Y1[i] + Y2[i] - Y3[i])
        Y[i] += 2.5
        Y[i] /= 8
        Y[i] *= 100
        
    print('REM      : minimum =', min(Y),'maximum =', max(Y))
    print('OK')
    return Y
