import numpy as np


def tridiagloes(a,b,f):
    c = np.zeros(a.shape)  ## Create vector c
    d = np.zeros(b.shape)  ## Create vector d
    c[0] = np.sqrt(a[0])   ## Set the initial condition for c[0] as it is calculated differently then the others
    d[0] = b[0]/np.sqrt([a[0]]) ## Set the initial condition for d[0] as it is needed for the first calculation in for loop
    for i in range(1,a.shape[0]):
        c[i] = np.sqrt(a[i] - np.square(d[i-1]))
        if i < b.shape[0]: ## To iterate in for loop one less time for vector d due to its size
            d[i] = b[i] / c[i]
    print(c)
    print(d)
    y = np.zeros(f.shape)
    y[0] = f[0]/c[0]  ## Initial condition
    for i in range(1, y.shape[0]):  ## Vorwaertseinzetsen // Calculate each element of vector y 
        y[i] = (f[i]-d[i-1]*y[i-1])/c[i]
    u = np.zeros(f.shape)
    u[u.shape[0]-1] = y[u.shape[0]-1] / c[u.shape[0]-1]  ## Initial condition
    for i in range(u.shape[0]-2,-1,-1): ## Rueckwaertseinzetsen // Calculate each element of vector u
        u[i] = (y[i]-d[i]*u[i+1])/c[i]
    print(u)
    return u




a = np.array([2,2,2,2,1])
b = np.array([-1,-1,-1,-1])
f = np.array([1,1,1,1,1])
tridiagloes(a,b,f)

###############################################################################################################################################################
# Die Einträge des Verschiebungsvektors sind abhängig von n. u_1 = n | u_2 = u_1 + n-1 = 2n-1 | u_3 = u_2 + n-2 = 3n-3 | u_4 = u_3 + n-3 = 4n-7 ....... 