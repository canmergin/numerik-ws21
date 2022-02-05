import numpy as np
from scipy.linalg import lu
from scipy.linalg import hilbert


T = np.zeros(shape=(12,6))
for i in range(0,T.shape[0]): 
    T[i][0] = i+2  ## First Column // Fill first column witn numbers n= 2,3...13
    A = hilbert(i+2)  ## Create a Hilbert matrix with n = i+2
    b = A[:,0]+A[:,i+1] ## Calculate the vector b
    x = np.zeros(shape=(i+2))  ## Create vector x
    x[0] = 1 ## Set the first entry of x to 1
    x[i+1] = 1  ## Set the last entry of x to 1
    x_norm = np.linalg.norm(x, np.inf) ## Norm of x is calculated here not to calculate it multiple times in further steps

    T[i][1] = np.linalg.cond(A, np.inf)*1e-16  ## Second Column // Calculate the condition number of A with inf-Norm

    x_bs = np.linalg.solve(A,b)
    T[i][2] = np.linalg.norm(x-x_bs, np.inf) / x_norm ## Third Column // Calculate the relative error of the solution of A with inf-Norm

    P,L, R = lu(A, permute_l=False) ## Calculate the LR-Decomposition of matrix A
    x_lr = np.linalg.solve(R,np.linalg.solve(L,P@b)) ## Vorwaertseinzetsen und Rueckwaertseinzetsen // Calculate the solution x with LR-Decomposition
    T[i][3] = np.linalg.norm(x-x_lr, np.inf) / x_norm ## Fourth Column // Calculate the relative error of the solution x with LR-Decomposition
    L_ch = np.linalg.cholesky(A) ## Calculate the Cholesky-Decomposition of matrix A
    x_ch = np.linalg.solve(L_ch.T,np.linalg.solve(L_ch,b))  ## Vorwaertseinzetsen und Rueckwaertseinzetsen // Calculate the solution x with Cholesky-Decomposition
    T[i][4] = np.linalg.norm(x-x_ch, np.inf) / x_norm ## Fifth Column // Calculate the relative error of the solution x with Cholesky-Decomposition

    T[i][5] = np.linalg.norm(A@x_ch - b, np.inf) ## Sixth Column
print(T)


###############################################################################################################################################################
# Der Algorithmus, der am schlechsten ab schneidet, ist LR-Zerlegunug mit Pivotisierung bei Hilbertmatrizen. Wenn man als Algorithmus die LR-Zerlegung mit Pivotisierung verwendet, ist die relative 
# Fehler sehr groß für n größer 5. Aber wenn man die LR-Zerlegung ohne Pivotiseriung (d.h. ohne P-Matrix / in Python lu(A, permute_l=True)), ist die relative Fehler sehr gering für n = 2, 3, . . . , 13.
# Das Äquivalent von Backslash A\b ist bei Python numpy.linalg.solve und nach unserer Meinung verwendet diese Funktion auch die LR-Zerlegung, da die relative Fehler bei LR-Zerlegung ohne Pivotisierung
# gleich ist. Cholesky-Zerlegung liefert auch sehr kleine relative Fehler wie numpy.linalg.solve.. Alle relative Fehlern in dieser Tabelle sind abhängig von Rechner, Programmiersprache, spezifische
# Funktionen, die verwendet werden. Deswegen kann man die Ergebnisse wirklich nicht hunderprozentig richtig interpretieren.
#
# Die Hilbertmatrizen mit n>13 sind nicht positiv definit. Man kann die Cholesky-Zerlegung für nicht positiv definite Matrizen nicht berechnen, deswegen bekommt man eine Fehlermeldung und das Programm
# funktionert nicht. Mann kan die Tabelle für n = 14 oder n = 15 nicht erstellen.
###############################################################################################################################################################