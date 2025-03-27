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
    plt.figure(figsize=(10,4))
    plt.subplot(1, 2, 1)
    plt.pcolormesh(real,cmap='seismic')
    plt.title(f"Parte real de la señal {signalName}")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.colorbar(label="Magnitud")

    # Grafica la parte imaginaria de la transformada
    plt.subplot(1, 2, 2)
    plt.pcolormesh(imag,cmap='seismic')
    plt.ylabel("Y")
    plt.title(f"Parte imaginaria de la señal {signalName}")
    plt.xlabel("X")
    plt.colorbar(label="Magnitud")
    
    #Se asegura que no se superpongan las graficas
    plt.tight_layout()

    #Guarda la grafica
    plt.savefig(os.path.join(graphicsPath,f"Transformada del {signalName}.pdf"))
    plt.show()

def plotArray(arrayList,nameList, graphicsPath, title):
    plt.figure(figsize=(5*len(arrayList),4))
    for i in range(0,len(arrayList)):
        
        plt.subplot(1, len(arrayList), i+1)
        plt.pcolormesh(arrayList[i], cmap='grey')
        plt.title(f"Grafica {nameList[i]}")
        plt.colorbar(label="Magnitud")
        plt.ylabel("Y")
        plt.xlabel("X")

    #Se asegura que no se superpongan las graficas
    plt.tight_layout()

    #Guarda la grafica
    plt.savefig(os.path.join(graphicsPath,f"{title}.pdf"))
    plt.show()

#Array solicitados
array1 = np.zeros((30, 30))
array2 = np.zeros((30, 30))
array3 = np.zeros((30, 30))

#Cambia los puntos solicitados de los arrays a 1
array1[5, 5] = 1
array1[5, 10] = 1
array2[5, 5] = 1
array2[25, 5] = 1
array3[10, 15] = 1
array3[25, 20] = 1

#Define la carpeta donde se van a guardar las graficas
graphicsPath = os.path.join(os.path.dirname(__file__),"Graphics")

#Crea una lista con los 3 arrays
arrayList = [array1, array2, array3]

#Por cada array en la lista
contador = 1
for array in arrayList:

    #Nombre del array
    nombre = f"Array {contador}"
    contador += 1

    #Calcula la transformada de fourier del array
    dataFourier = fourierTransformation(array)

    #Genera el grafico de la transformada del array
    plotFourier(dataFourier,nombre,graphicsPath)

#Rota el primer array1 90 grados en sentido horario
array1Rotado = np.rot90(array1)
plotArray([array1,array1Rotado],["Array1", "Array1 Rotado"],graphicsPath, "Comparacion Rotacion Array 1")

#Acerca un punto del array2 
array2Acercado = np.zeros((30, 30))
array2Acercado[25,5] = 1
array2Acercado[15,5] = 1
plotArray([array2,array2Acercado],["Array2", "Array2 Acercado"],graphicsPath, "Comparacion Acercamiento Array 2")

#Aleja un punto del array2 
array2Alejado = np.zeros((30, 30))
array2Alejado[25,5] = 1
array2Alejado[0,5] = 1
plotArray([array2,array2Alejado],["Array2", "Array2 Alejado"],graphicsPath, "Comparacion Alejamiento Array 2")

#Mueve un punto de array 3 en 45 grados
array3Movido = np.zeros((30, 30))
array3Movido[10, 15] = 1
array3Movido[5, 0] = 1 
plotArray([array3,array3Movido],["Array3", "Array3 Movido"],graphicsPath, "Comparacion Movimiento en angulo Array 3")

#Crea una lista con los 4 arrays
arrayNameList = ["Array1 Rotado", "Array2 Acercado", "Array2 Alejado", "Array3 Movimiento en Angulo"]
arrayList = [array1Rotado, array2Acercado, array2Alejado, array3Movido]

#Por cada array en la lista
for i in range(0,len(arrayList)):

    #Calcula la transformada de fourier del array
    dataFourier = fourierTransformation(arrayList[i])

    #Genera el grafico de la transformada del array
    plotFourier(dataFourier,arrayNameList[i],graphicsPath)