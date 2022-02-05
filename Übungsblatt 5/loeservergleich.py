import numpy as np
import matplotlib.pyplot as plt



def Ableitung(t,y):
    y_strich = np.cos(t) * y
    return y_strich

def Euler(h,x):
    y = np.zeros(x.shape[0])
    x[0] = 0
    y[0] = 1
    for i in range(1,x.shape[0]):
        y[i] = y[i-1] + h * Ableitung(x[i-1],y[i-1])
    return y

def Collatz(h,x):
    y = np.zeros(x.shape[0])
    x[0] = 0
    y[0] = 1
    for i in range(1,x.shape[0]):
        y[i] = y[i-1] + h * Ableitung(x[i-1] + 0.5*h, y[i-1] + 0.5*h*Ableitung(x[i-1],y[i-1]))
    return y

def Henn(h, x):
    y = np.zeros(x.shape[0])
    x[0] = 0
    y[0] = 1
    for i in range(1,x.shape[0]):
        y[i] = y[i-1] + h* ((0.5*Ableitung(x[i-1],y[i-1]))+(0.5*Ableitung(x[i-1]+h, y[i-1]+(h*Ableitung(x[i-1],y[i-1])))))
    return y


def loesevergleich(h):
    x = np.arange(0,50+h,h)
    plt.plot(x, Euler(h,x),color='blue', linewidth=1, label='Euler')
    plt.plot(x, Collatz(h,x),color='red', linewidth=1,label='Collatz')
    plt.plot(x,Henn(h, x),color='green', linewidth=1,label='Henn')
    plt.legend()
    plt.grid(True)
    plt.show()

loesevergleich(0.5)


