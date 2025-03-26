#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def FTd(x, N):

    t = np.linspace(-4, 4, N)
    x_vals = x(t)
    xsom = np.zeros(N, dtype=np.complex_)
    omega = 2 * np.pi / N

    for k in range(N):
        for i in range(N):
            xsom[k] += x_vals[i] * np.exp(-1j*omega*k*i)
        xsom[k] /= N
    return xsom, t

def f(x):
    return np.piecewise(x, [x<-2, ((-2<=x) & (x<=-1) | (1<=x) & (x<=2)), x>2], [0, 1, 0])

N = 1024
F, t = FTd(f, N)
freq = np.fft.fftfreq(N, d=(t[1] - t[0]))

F_S = np.fft.fftshift(F)
freq_s = np.fft.fftshift(freq)

x_vals = np.arange(-4, 4, 0.01)

plt.figure(figsize=(11,7))
plt.xlim(-4, 4)
plt.ylim(0, 2)
plt.plot(x_vals, f(x_vals), color='b')
plt.title('Espectro de frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.grid(True)
plt.savefig('graf_Func.png')

plt.figure(figsize=(11,7))
plt.xlim(-5, 5)
plt.plot(freq_s, np.abs(F_S), color='b')
plt.title('Espectro de frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.grid(True)
plt.savefig('graf_DFT.png')

A = F_S * np.conj(F_S)

plt.figure(figsize=(11,7))
plt.xlim(-5, 5)
plt.plot(freq_s, np.abs(A), color='b')
plt.title('Espectro de frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.grid(True)
plt.savefig('graf_A.png')

