import numpy as np
import numexpr as ne


def function(f,x):
    return ne.evaluate(f) ## Take the string input, cast it into function using ne.evaluate and evaluate the output of function "f" at the point "x"


def regulafalsi(f,a,b,tol):
    while True:
        x = (a*function(f,b)-b*function(f,a))/(function(f,b)-function(f,a)) ## Calculate x_k
        if (function(f,x) > 0 and function(f,a) > 0) or (function(f,x) < 0 and function(f,a) < 0): ## Check if the signs of l and x_k are same
            a = x
        else:
            b = x
        x_next = (a*function(f,b)-b*function(f,a))/(function(f,b)-function(f,a)) ## Calculate x_k+1 to check the loop condition with tolerance
        if np.abs(x_next - x) < tol:
            break
    return x



print(regulafalsi("1 + cos(x)*cosh(x)",1,2,0.000000001)) ## Type the function as a string in type of f(x) Example: Type "1 + cos(x)*cosh(x)" for f(x) = 1 + cos(x)*cosh(x) // Type "cos(x)" for f(x) = cos(x)

## Wir mussten "numexpr" Package benutzen um die Funktion f als eine einzige Eingabe in der Funktion regulafalsi zu übermitteln. Ohne diese Package kann man Funktionen wie cos(x)*cosh(x) direkt
## nicht übergeben und kann nur einzeln Funktionen wie "cos" eingeben.