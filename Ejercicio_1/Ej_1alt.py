#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Definicion de las funciones
def f(x):  # Primer ancho
    return np.piecewise(x, [(x<-2), ((-2<=x) & (x<=-1) | (1<=x) & (x<=2)), (x>2)], [0, 1, 0])

def f2(x):  # Segundo ancho
    return np.piecewise(x, [(x<-3), ((-3<=x) & (x<=-1) | (1<=x) & (x<=3)), (x>3)], [0, 1, 0])

# Array de valores de x
x_vals = np.linspace(-4, 4, 4000)

# Trasnformadas de Fourier incluido el desplazamiento de frecuencia cero al centro del espectro
Fou = np.fft.fft(f(x_vals))
freq = np.fft.fftfreq(len(Fou), d = x_vals[1]-x_vals[0])
Fou_S = np.fft.fftshift(Fou)
freq_s = np.fft.fftshift(freq)

# Norma al cuadrado de la transformada de Fourier
FuncA = Fou_S * np.conj(Fou_S)

# Graficacion del primer ancho de la funcion
plt.xlim(-5, 5)
plt.plot(freq_s, FuncA, '-*')
plt.title('Norma al cuadrado, transf. Fourier')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('Transf. al cuadrado')
plt.grid()
plt.savefig('Transf^2.png')

# Transformada de Fourier para el otro ancho
Fou2 = np.fft.fft(f2(x_vals))
freq = np.fft.fftfreq(len(Fou2), d = x_vals[1]-x_vals[0])
Fou2_S = np.fft.fftshift(Fou2)

# Norma al cuadrado de la anterior transformada
FuncA2 = Fou2_S * np.conj(Fou2_S)

# Graficacion del segundo ancho
plt.xlim(-5,5)
plt.plot(freq_s, FuncA2, '-*')
plt.title('Cambio de ancho en la funcion')
plt.xlabel('Frecuencias($\omega$)')
plt.ylabel('Transf. al cuadrado')
plt.grid()
plt.savefig('Transf^2_2.png')


