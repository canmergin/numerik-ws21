import numpy as np
import numexpr as ne


def function(f,x):
    return ne.evaluate(f) ## Take the string input, cast it into function using ne.evaluate and evaluate the output of function "


def integral(f,a,b,n):
    ## Trapezregel
    h = (b-a)/(n)
    f_x_j = 0
    for j in range(2,n+1): ## n+1 to sum all of the elements
        x_j = a + ((j-1)*h)
        f_x_j += function(f,x_j)
    T = h*((0.5*(function(f,a)+function(f,b)))+f_x_j)

    ## Simpsonregel
    S = 0
    S_1 = 0
    S_2 = 0
    for i in range(1,n+1):
        S_1 += function(f,a+((2*i-1)*(h/2)))
    for j in range(1,n):
        S_2 += function(f,a+j*h)
    S += (h/6)*(function(f,a)+function(f,b)+4*S_1+2*S_2)
    return T, S

## Input
f = "x**2"
a = 0
b = 6
n = 2
## Output
T, S = integral(f,a,b,n)
print(T)
print(S)