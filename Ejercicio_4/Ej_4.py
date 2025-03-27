#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Se definen las funciones
def func1(x):
    return np.piecewise(x, [x<=2, x>2], [1, 0])

def func2(x):
    return x

def func3(x):
    return x + 500

def func4(x):
    return np.exp(-x*x)

# Se definen los valores de x para las funcs
x_vals = np.linspace(0, 1000, 1000)
x_vals_g = np.linspace(0, 10, 1000)

#Graficacion de las funciones
plt.figure(1)
plt.xlim(0,4)
plt.plot(x_vals_g, func1(x_vals_g))
plt.title('Funcion 1')
plt.xlabel('Valores de x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig('Func1.png')

plt.figure(2)
plt.plot(x_vals, func2(x_vals))
plt.title('Funcion 2')
plt.xlabel('Valores de x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig('Func2.png')

plt.figure(3)
plt.plot(x_vals, func3(x_vals))
plt.title('Funcion 3')
plt.xlabel('Valores de x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig('Func3.png')

plt.figure(4)
plt.xlim(0,4)
plt.plot(x_vals_g, func4(x_vals_g))
plt.title('Funcion 4')
plt.xlabel('Valores de x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig('Func4.png')

# Transformadas de Fourier y desplazamiento de frecuencia cero
Fou1 = np.fft.fft(func1(x_vals_g))
Fou1_s = np.fft.fftshift(Fou1)

Fou2 = np.fft.fft(func2(x_vals))
Fou2_s = np.fft.fftshift(Fou2)

Fou3 = np.fft.fft(func3(x_vals))
Fou3_s = np.fft.fftshift(Fou3)

Fou4 = np.fft.fft(func4(x_vals_g))
Fou4_s = np.fft.fftshift(Fou4)

freq1 = np.fft.fftfreq(len(Fou1), d = x_vals_g[1]-x_vals_g[0])
freq1_s = np.fft.fftshift(freq1)

freq2 = np.fft.fftfreq(len(Fou2), d = x_vals[1]-x_vals[0])
freq2_s = np.fft.fftshift(freq2)

freq3 = np.fft.fftfreq(len(Fou3), d = x_vals[1]-x_vals[0])
freq3_s = np.fft.fftshift(freq3)

freq4 = np.fft.fftfreq(len(Fou4), d = x_vals_g[1]-x_vals_g[0])
freq4_s = np.fft.fftshift(freq4)

# Transformadas seno y coseno
Cos1 = fft.dct(func1(x_vals_g))
Cos2 = fft.dct(func2(x_vals))
Cos3 = fft.dct(func3(x_vals))
Cos4 = fft.dct(func4(x_vals_g))

Sen1 = fft.dst(func1(x_vals_g))
Sen2 = fft.dst(func2(x_vals))
Sen3 = fft.dst(func3(x_vals))
Sen4 = fft.dst(func4(x_vals_g))

#Graficacion de las transformadas (real/imag/abs)
plt.figure(5)
plt.xlim(-3, 3)
plt.plot(freq1_s, np.real(Fou1_s), color='red', label='Real')
plt.plot(freq1_s, np.imag(Fou1_s), color='blue', label='Imaginario')
plt.plot(freq1_s, np.abs(Fou1_s), color='green', label='Absoluto')
plt.title('Transformada 1')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('F(x)')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('Transf_1.png')

plt.figure(6)
plt.xlim(-0.05, 0.05)
plt.plot(freq2_s, np.real(Fou2_s), color='red', label='Real')
plt.plot(freq2_s, np.imag(Fou2_s), color='blue', label='Imaginario')
plt.plot(freq2_s, np.abs(Fou2_s), color='green', label='Absoluto')
plt.title('Transformada 2')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('F(x)')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('Transf_2.png')

plt.figure(7)
plt.xlim(-0.05, 0.05)
plt.plot(freq3_s, np.real(Fou3_s), color='red', label='Real' )
plt.plot(freq3_s, np.imag(Fou3_s), color='blue', label='Imaginario')
plt.plot(freq3_s, np.abs(Fou3_s), color='green', label='Absoluto')
plt.title('Transformada 3')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('F(x)')
plt.legend(loc='upper right')
plt.grid()
plt.savefig('Transf_3.png')

plt.figure(8)
plt.xlim(-3, 3)
plt.plot(freq4_s, np.real(Fou4_s), color='red', label='Real')
plt.plot(freq4_s, np.imag(Fou4_s), color='blue', label='Imaginario')
plt.plot(freq4_s, np.abs(Fou4_s), color='green', label='Absoluto')
plt.title('Transformada 4')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('F(x)')
plt.legend(loc='upper right')
plt.grid()
plt.savefig('Transf_4.png')

# Graficacion de las transformadas seno y coseno
plt.figure(9)
plt.xlim(0, 3)
plt.plot(freq1, Cos1, color='red', label='Coseno')
plt.plot(freq1, Sen1, color='blue', label='Seno')
plt.title('Seno y coseno 1')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('F(x)')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('CosSen_1.png')

plt.figure(10)
plt.xlim(0, 0.05)
plt.plot(freq2, Cos2, color='red', label='Coseno')
plt.plot(freq2, Sen2, color='blue', label='Seno')
plt.title('Seno y coseno 2')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('F(x)')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('CosSen_2.png')

plt.figure(11)
plt.xlim(0, 0.05)
plt.plot(freq3, Cos3, color='red', label='Coseno')
plt.plot(freq3, Sen3, color='blue', label='Seno')
plt.title('Seno y coseno 3')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('F(x)')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('CosSen_3.png')

plt.figure(12)
plt.xlim(0, 5)
plt.plot(freq4, Cos4, color='red', label='Coseno')
plt.plot(freq4, Sen4, color='blue', label='Seno')
plt.title('Seno y coseno 4')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('F(x)')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('CosSen_4.png')


