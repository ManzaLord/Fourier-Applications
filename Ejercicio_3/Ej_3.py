import os
import numpy as np
import matplotlib.pyplot as plt

def plotFunc(t,data, signalName, graphicsPath):
    #Grafica la senal
    plt.figure(figsize=(10,5))
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

def plotFourier(dataF, signalName, graphicsPath):
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
    plt.xlim([-4000,4000])

    #Grafica la parte imaginaria de la transformada
    plt.subplot(2, 1, 2)
    plt.plot(freq,imag)
    plt.ylabel("Magnitud")
    plt.title(f"Parte imaginaria de la señal {signalName[:-4]}")
    plt.xlabel("Frecuencia (Hz)")
    plt.xlim([-4000,4000])
    
    #Se asegura que no se superpongan las graficas
    plt.tight_layout()

    #Guarda la grafica
    plt.savefig(os.path.join(graphicsPath,f"Transformada_de_{signalName[:-4]}.pdf"))
    plt.show()

def findFreq(dataF, signalName):
    #Separa los datos necesarios de la transformada
    real = dataF[0]
    freq = dataF[2]
    
    #Ciclo que revisa todas las magnitudes de la parte real de la transformada
    print(f"Frencuencias de la señal {signalName[:-4]}")
    for i in range(1,len(real)-1):

        #Si la magnitud real es mayor que su valor anterior, el siguiente y un valor minimo, se concidera un maximo
        if real[i] > real[i+1] and real[i] > real[i-1] and real[i] > 0.0001:

            #Muestra la frecuencia a la que ocurre el maximo
            print(round(freq[i],3))

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

    #Busca las frecuencias de la senal
    findFreq(dataFourier,dataFile)

    #Genera la grafica de la parte real e imaginaria de la transformada
    plotFourier(dataFourier, dataFile,graphicsPath)