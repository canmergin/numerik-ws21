import numpy as np
import numexpr as ne
import matplotlib.pyplot as plt


def function(f,x):
    return ne.evaluate(f) ## Take the string input, cast it into function using ne.evaluate and evaluate the output of function "


def ableitungsplot(f,a,b,n,h):
    x_stutzpunkte = np.linspace(a,b,n)
    x_lin = np.linspace(a,b,1000)
    f_normal = function(f,x_lin)
    f_ersteAbleitung = (function(f,x_stutzpunkte+h)-function(f,x_stutzpunkte-h))/(2*h)
    f_zweiteAbleitung = (function(f,x_stutzpunkte-h)-(2*function(f,x_stutzpunkte))+function(f,x_stutzpunkte+h))/(h**2)
    ## Plotting
    plt.rcParams["figure.autolayout"] = True
    plt.grid(True)
    plt.axis([a,b,np.amin(f_normal),np.amax(f_normal)])
    plt.title('Ableitungsplot', fontsize=16, color='black')
    plt.plot(x_lin,f_normal,color='blue', linewidth=2, label='f(x)')
    plt.plot(x_stutzpunkte,f_ersteAbleitung,color='red', linewidth=2,label="f'(x)")
    plt.plot(x_stutzpunkte,f_zweiteAbleitung,color='green', linewidth=2,label="f''(x)")
    plt.legend()
    plt.show()

## Input
f = "x**3"
a = 0
b = 3
n = 5
h = 0.1
ableitungsplot(f,a,b,n,h)
