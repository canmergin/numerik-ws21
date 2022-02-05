import numpy as np

def federkraft(x,a):
    F = s*((l/np.linalg.norm(x-a))-1)*(x-a) ## Calculate the spring force
    return F

def federkraftableitung(x,a): ## Calculate the Jacobian Matrix of force
    F_strichLeft = ((l/np.linalg.norm(x-a,2))-1)*np.eye(2,2)
    F_strichRight = -l*(((x-a)@np.transpose(x-a))/np.linalg.norm(x-a,2)**3)
    F_strich = s*(F_strichLeft + F_strichRight)
    return F_strich

def newton(x,tol):
    while True:
        F_ges = federkraft(x,a1)+G+federkraft(x,a2) ## Sum of all the forces
        F_gesAbleitung = federkraftableitung(x,a1)+federkraftableitung(x,a2) ## Sum of all the Jacobian matrices
        x_n = x - np.linalg.inv(F_gesAbleitung)@F_ges ## Newton method
        if np.linalg.norm(x_n-x) < tol:
            x = x_n
            break
        x = x_n
        print(x)
    return x



## Parameters
g = 9.81
m = 1
G = np.array([0,-g*m])
a1 = np.array([0,0])
a2 = np.array([1,1])
s = 10
l = 2
##
x = np.array([0,-4])
newton(x,0.00000001)

#################################################################################
## Newton Verfahren konvergiert nur, wenn der Betrag der Ableitung von x_n kleiner als 1
## ist. Wenn x = [0,4] ist der Betrag der Ableitung großer als 1, deswegen konvergiert
## die Funktion nicht und man darf das Newton-Verfahren nicht verwenden.




