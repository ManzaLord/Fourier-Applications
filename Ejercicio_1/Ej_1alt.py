#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.piecewise(x, [(x<-2), ((-2<=x) & (x<=-1) | (1<=x) & (x<=2)), (x>2)], [0, 1, 0])

def f2(x):
    return np.piecewise(x, [(x<-3), ((-3<=x) & (x<=-1) | (1<=x) & (x<=3)), (x>3)], [0, 1, 0])


x_vals = np.linspace(-4, 4, 4086)

Fou = np.fft.fft(f(x_vals))
freq = np.fft.fftfreq(len(Fou), d = x_vals[1]-x_vals[0])
Fou_S = np.fft.fftshift(Fou)
freq_s = np.fft.fftshift(freq)

FuncA = Fou_S * np.conj(Fou_S)

plt.xlim(-5, 5)
plt.plot(freq_s, FuncA, '-*')
plt.title('Norma al cuadrado, transf. Fourier')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('Transf. al cuadrado')
plt.savefig('Transf^2.png')

Fou2 = np.fft.fft(f2(x_vals))
freq = np.fft.fftfreq(len(Fou2), d = x_vals[1]-x_vals[0])
Fou2_S = np.fft.fftshift(Fou2)

FuncA2 = Fou2_S * np.conj(Fou2_S)

plt.xlim(-5,5)
plt.plot(freq_s, FuncA2, '-*')
plt.title('Cambio de ancho en la funcion')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('Transf. al cuadrado')
plt.savefig('Transf^2_2.png')


