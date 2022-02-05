import numpy as np
import matplotlib.pyplot as plt

def interpoly(x,f):
    V = np.vander(x) ## Create the Vandermonde Matrix for the x values
    A = np.linalg.solve(V,f) ## Solve the LGS VA=f to calculate the coefficients (Matrix A) of the interpolation polynomial
    F = np.polyval(A,x) ## Calculate the values of the function using the interpolation polynomial
    ## Plotting
    x_Plot = np.linspace(np.amin(x),np.amax(x),1000)
    F_Plot = np.polyval(A,x_Plot) ## Calculate the values of the function using the interpolation polynomial (FOR PLOTTING)
    plt.rcParams["figure.autolayout"] = True
    plt.grid(True)
    plt.axis([np.amin(x)-1,np.amax(x)+1,-2,2])
    plt.title('Interpolationspolynom', fontsize=16, color='black')
    plt.plot(x_Plot,F_Plot,color='blue', linewidth=2)
    plt.scatter(x,f,color="red")
    plt.show()
    return A



###### Input
X_min = -6
X_max = 6
X_n = X_max-X_min+1
x = np.linspace(X_min,X_max,X_n)   ## X-Werte der Stützpunkte für äquidistante Stützstellen
#x = ((X_min+X_max)/2) + ((X_max-X_min)/2)*np.polynomial.chebyshev.chebpts1(X_n)  ## X-Werte der Stützpunkte für Tschebyscheff-Stützstellen
f = 1/(1+x**2)           ## F-Werte der Stützpunkte // Geben Sie die Funktion hier ein

###### Output
A = interpoly(x,f)         ## Koeffizienten des Interpolationpolynoms
print(A)
###### Testing
##print(np.polyval(interpoly(x,f),x))  ## Berechnet die F-Werte der Stützpunkte mit dem Interpolationspolynom 