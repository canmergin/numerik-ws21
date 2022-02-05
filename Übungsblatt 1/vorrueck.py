import numpy as np

def vorrueck(L,R,b):
    y = np.zeros(b.shape[0])
    y[0] = b[0] ## Initial condition
    for i in range(1,len(y)):
        y[i] = b[i]    ## Set the b value as initial solution for y
        for j in range (0,len(y)):
            if i != j:  ## So that no unnecessary subtractions are made
                y[i] -= L[i][j]*y[j] ## Subtract the matrix value * y(-1)-value from the solution
    x = np.zeros(b.shape[0])
    x[len(x)-1] = y[len(x)-1]/R[len(x)-1][len(x)-1]
    for i in range(len(x)-2,-1,-1):
        x[i] = y[i]    ## Set the y value as initial solution for x
        factor = 0
        for j in range (0,len(x)):
            if i == j:  ## To divide by the matrix value of its
                factor = R[i][j]
                continue
            else:
                x[i] -= (R[i][j]*x[j]) ## Subtract the matrix value y-value from the solution
        if (factor != 0): ## Divide in the end so equation is correct
            x[i] /= factor
    return x
