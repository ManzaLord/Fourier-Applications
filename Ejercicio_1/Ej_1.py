import numpy as np
import matplotlib.pyplot as lp

def FTd(x, T, N):

    t = np.arange(0, T, T/N)
    xsom = np.zeros(N, dtype=np.complex_)
    omega = 2 * math.pi / N

    for k in range(N):
        for i in range(N):
            xsom[k] = xsom[k] + x(t[i])*np.e**(-1j*omega*k*i)
        xsom[k] = xsom[k] / N
    return xsom

def f(x):
    return np.piecewise(x, [(x<-2), ((-2<=x<=-1) & (1<=x<=2)), (x>2)], [0, 1, 0])

N = 100
T = 2

F = FTd(f, T, N)


