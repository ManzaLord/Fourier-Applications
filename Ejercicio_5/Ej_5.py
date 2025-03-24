import numpy as np
import matplotlib.pyplot as plt
import os

def fourierTransformation(signal):
    #Calcula la transformada de fourier de la senal
    fourierSignal = np.fft.fft2(signal, norm="forward")

    #Centra las frecuencias de la transformada de fourier
    fourierSignal = np.fft.fftshift(fourierSignal)

    #Calcula la parte real de la transformada
    real = np.fft.fftshift(np.real(fourierSignal))

    #Calcula la parte imaginaria de la transformada
    imaginary = np.fft.fftshift(np.imag(fourierSignal))

    #Retorna unalista con los valores calculados de la transformada
    return [real, imaginary]

def plotFourier(dataF, signalName,graphicsPath):

    #Separa los datos de la transformada de fourier
    real = dataF[0]
    imag = dataF[1]

    #Grafica la parte real de la transformada
    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.pcolormesh(real, cmap='gray', shading='auto')
    plt.title(f"Parte real de la señal {signalName}")
    plt.ylabel("Magnitud")
    plt.xlabel("Frecuencia (Hz)")

    # Grafica la parte imaginaria de la transformada
    plt.subplot(1, 2, 2)
    plt.pcolormesh(imag, cmap='gray', shading='auto')
    plt.ylabel("Magnitud")
    plt.title(f"Parte imaginaria de la señal {signalName}")
    plt.xlabel("Frecuencia (Hz)")
    
    #Se asegura que no se superpongan las graficas
    plt.tight_layout()

    #Guarda la grafica
    plt.savefig(os.path.join(graphicsPath,f"Transformada_de_{signalName}.pdf"))
    plt.show()

#Array solicitados
data1 = np.zeros((30, 30))
data2 = np.zeros((30, 30))
data3 = np.zeros((30, 30))

#Cambia los puntos solicitados de los arrays a 1
data1[5, 5] = 1
data1[5, 10] = 1
data2[5, 5] = 1
data2[25, 5] = 1
data3[10, 15] = 1
data3[25, 20] = 1

#Crea una lista con los 3 arrays
dataList = [data1, data2, data3]

graphicsPath = os.path.join(os.path.dirname(__file__),"Graphics")


#Por cada array en la lista
contador = 1
for data in dataList:

    #Nombre del array
    nombre = f"Array_{contador}"
    contador += 1

    #Calcula la transformada de fourier del array
    dataFourier = fourierTransformation(data)

    #Genera el grafico de la transformada del array
    plotFourier(dataFourier,nombre,graphicsPath)