import numpy as np
import matplotlib.pyplot as lp

def FTd(x):

    N = len(x)
    n = np.arange(N)
    k = np.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n/N)

    X = np.dot(e, x)

    return X

def f(x):
    return np.piecewise(x, [(x<-2), ((-2<=x<=-1) & (1<=x<=2)), (x>2)], [0, 1, 0])

x = np.linspace(-5, 5, 1000)

