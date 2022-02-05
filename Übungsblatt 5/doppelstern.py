import numpy as np
import matplotlib.pyplot as plt

def kraft(x_1, x_2): ## Calculates the force between two objects in 2D-space (x_1, x_2 are positions, m1, m2 are masses)
    gk = 1
    kraft = (gk*m1*m2)/(np.power(np.linalg.norm(x_2-x_1),3))*(x_2-x_1)
    return kraft

def ableitung(y): ## Input y Array independent with time
    y_ableitung = np.array([y[2],y[3], kraft(y[0],y[1])/m1, -kraft(y[0],y[1])/m2]) ## f(y(t))
    return y_ableitung

def ruku_schritt(y, h): ## Solves the differential equation with Runge-Kutta-Schritt for each step
    k1 = ableitung(y)
    k2 = ableitung(y + (0.5*h*k1))
    k3 = ableitung(y + (0.5*h*k2))
    k4 = ableitung(y + (h*k3))
    y_neu = y + h * ((k1/6)+(k2/3)+(k3/3)+(k4/6))
    return y_neu


def doppelstern(m1,m2,x1,x2,p,h): ## Program overwrites previous positions and speeds of the objects to save memory
    x_1 = np.array([x1, 0]) ## Initial position of object 1
    x_2 = np.array([x2, 0]) ## Initial position of object 2
    v_1 = np.array([0, p/m1]) ## Initial speed of object 1
    v_2 = np.array([0, -p/m2]) ## Initial speed of object 2
    y = np.array([x_1, x_2, v_1, v_2]) ## y(t)
    ## Plotting
    fig = plt.figure()
    plt.scatter(x_1[0],x_1[1],color='blue')
    plt.scatter(x_2[0],x_2[1],color='red')
    plt.axis([-2,2,-2,2])
    plt.draw()
    plt.pause(h)
    fig.clear()
    while True:
        y = ruku_schritt(y,h)
        plt.scatter(y[0][0],y[0][1],color='blue')
        plt.scatter(y[1][0],y[1][1],color='red')
        plt.axis([-2,2,-2,2])
        plt.draw()
        plt.pause(h)
        fig.clear()

## Input (Global Variables)
m1 = 1
m2 = 10
x1 = -1
x2 = 1
p = 1
h = 0.01

doppelstern(m1,m2,x1,x2,p,h)


