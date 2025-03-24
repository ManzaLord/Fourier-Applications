import matplotlib.pyplot as plt
import numpy as np
import os

#Funcion de estudio
def func(position, a = 3):
    r = np.sqrt(position[0]**2 + position[1]**2)
    return np.where(r <= a, 1, 0)

#Grafica la funcion de estudio
def plotFunc(pos,fValues, title = ""):
    plt.pcolormesh(pos[0], pos[1], fValues, cmap='gray', shading='auto')
    plt.title(title)
    plt.xlim(-5,5)
    plt.ylim(-5,5)


# Crea la malla de coordenadas
maxPoints = 1000
position = np.meshgrid(np.linspace(-5, 5, maxPoints), np.linspace(-5, 5, maxPoints))

# Calcula los valores de la funcion en el plano (X,Y)
funcValues = func(position)

#Calcula la transformada de fourier de la funcion
fourierValues = np.fft.fft2(funcValues)

#Centra los valores de la frencuencia cero
fourierValues = np.fft.fftshift(fourierValues)

#Calcula la transformada por su complemento
magFourier =np.abs(fourierValues) ** 2

#Convierte las magnitudes a escala logaritmica para mejor visualizacion
logMagFourier = np.log(magFourier + 1)

#Grafica la funcion original y la transformada
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plotFunc(position, funcValues, title = "Funcion f(r)")
plt.subplot(1,2,2)
plotFunc(position, logMagFourier, title = "Funcion F(k)F¯(k)")
plt.tight_layout()
mainPath = os.path.dirname(__file__)
plt.savefig(os.path.join(mainPath,"Grafica_Ejercicio2.png"))
plt.show()