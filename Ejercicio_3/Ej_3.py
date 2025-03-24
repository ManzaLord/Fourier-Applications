import os
import numpy as np
import matplotlib.pyplot as plt

def plotFunc(t,data, signalName, graphicsPath):
    #Grafica la senal
    plt.plot(t,data)
    plt.ylabel("Magnitud")
    plt.title(f"Datos de la señal {signalName[:-4]}")
    plt.xlabel("Tiempo (s)")
    
    #Guarda la grafica
    plt.savefig(os.path.join(graphicsPath,f"{signalName[:-4]}.pdf"))
    plt.show()

def fourierTransformation(signal,t):
    #Calcula la transformada de fourier de la senal
    fourierSignal = np.fft.fft(signal, norm="forward")

    #Centra las frecuencias de la transformada de fourier
    fourierSignal = np.fft.fftshift(fourierSignal)

    #Calcula las frecuencias de la transformada
    frequency = np.fft.fftfreq(len(signal),d = t[1] - t[0])

    #Calcula la parte real de la transformada
    real = np.fft.fftshift(np.real(fourierSignal))

    #Calcula la parte imaginaria de la transformada
    imaginary = np.fft.fftshift(np.imag(fourierSignal))

    #Retorna unalista con los valores calculados de la transformada
    return [real, imaginary, frequency]

def plotFourier(dataF, signalName,graphicsPath):

    #Separa los datos de la transformada de fourier
    real = dataF[0]
    imag = dataF[1]
    freq = dataF[2]

    #Grafica la parte real de la transformada
    plt.subplot(2, 1, 1)
    plt.plot(freq,real)
    plt.title(f"Parte real de la señal {signalName[:-4]}")
    plt.ylabel("Magnitud")
    plt.xlabel("Frecuencia (Hz)")

    # Grafica la parte imaginaria de la transformada
    plt.subplot(2, 1, 2)
    plt.plot(freq,imag)
    plt.ylabel("Magnitud")
    plt.title(f"Parte imaginaria de la señal {signalName[:-4]}")
    plt.xlabel("Frecuencia (Hz)")
    
    #Se asegura que no se superpongan las graficas
    plt.tight_layout()

    #Guarda la grafica
    plt.savefig(os.path.join(graphicsPath,f"Transformada_de_{signalName[:-4]}.pdf"))
    plt.show()

#Obtiene el path del directorio donde esta este programa
mainPath = os.path.dirname(__file__)

#Agrega la carpeta data al path del directorio
filePath = os.path.join(mainPath, "Data")

graphicsPath = os.path.join(mainPath, "Graphics")

#Crea una lista con los nombres de los archivos de datos
dataFiles = os.listdir(filePath)

#Genera un conjunto de datos de 0 a 1s
tValues = np.linspace(0,1,44100)

#Para cada archivo de datos
for dataFile in dataFiles:
    #Agrega el archivo al path del directorio
    dataPath = os.path.join(filePath, dataFile)

    #Lee el archivo de datos
    with open(dataPath, 'r') as f:
        data = np.loadtxt(f)

    #Genera la grafica de los datos en funcion del tiempo
    plotFunc(tValues,data,dataFile,graphicsPath)

    #Obtiene la transformada de fourier de la senal
    dataFourier = fourierTransformation(data,tValues)

    #Genera la grafica de la parte real e imaginaria de la transformada
    plotFourier(dataFourier, dataFile,graphicsPath)

