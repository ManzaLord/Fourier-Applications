import matplotlib.pyplot as plt
import numpy as np
import os

#Funcion de estudio
def func(position, a = 3):
    #Calcula el radio para todas las coordenadas de la malla
    r = np.sqrt(position[0]**2 + position[1]**2)

    #Retorna una lista de valores, segun el valor de r (r>a da 0, r<=a da 1)
    return np.where(r <= a, 1, 0)

#Grafica la funcion dada
def plotFunc(pos, fValues, title, log = False):
    #Grafica los valores dados
    plt.pcolormesh(pos[0], pos[1], fValues, cmap='seismic')

    #Indica en la barra si usa una escala logaritmica
    if log == True:
        plt.colorbar(label="Magnitud (Escala logaritmica)")
    else:
        plt.colorbar(label="Magnitud")

    #Agrega el titulo y los limites de la grafica
    plt.title(title)
    plt.xlim(-5,5)
    plt.ylim(-5,5)

#Define la dimension de la matriz cuadrada
maxPoints = 500 

#Crea una malla de coordenadas
position = np.meshgrid(np.linspace(-5, 5, maxPoints), np.linspace(-5, 5, maxPoints))

#Calcula los valores de la funcion en la matriz de coordenadas
funcValues = func(position)

#Calcula la transformada de fourier de la funcion
fourierValues = np.fft.fft2(funcValues)

#Centra los valores de la frencuencia cero 
fourierValues = np.fft.fftshift(fourierValues)

#Calcula la transformada por su conjugado
magFourier =np.abs(fourierValues) ** 2

#Convierte las magnitudes a escala logaritmica para mejor visualizacion del cambio de valores de la transformada
logMagFourier = np.log(magFourier + 1)

#Define el tamano del plano
plt.figure(figsize=(10,4))

#Grafica la funcion de estudio
plt.subplot(1,2,1)
plotFunc(position, funcValues, title = "Funcion f(r)")

#Grafica la transformada de la funcion por su complemento
plt.subplot(1,2,2)
plotFunc(position, logMagFourier, title = "Funcion F(k)F¯(k)", log = True)

#Se asegura que no se superponer ambas graficas
plt.tight_layout()

#Guarda la grafica y la muestra
plt.savefig(os.path.join(os.path.dirname(__file__),"Grafica_Ejercicio2.pdf"))
plt.show()