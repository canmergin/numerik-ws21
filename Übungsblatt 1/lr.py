import numpy as np


def lr(A):
    L = np.eye(A.shape[0])
    L = L.astype(np.float64)
    A = A.astype(np.float64)
    for a in range(0,A.shape[0]-1): ## The variable for the current column , GAUSS ALGORITHMUS
        for i in range(a+1,A.shape[0]): ## The variable for the current row, the initial value of range is "a+1" to create the triangle shape of R matrix
            for j in range(a,A.shape[0]): ## The variable for comparison row, the initial value of range is "a" to not check back
                if A[i][a] == 0 or A[j][a] == 0 or i==j: ## To not divide anything by 0 / i!=j, so no comparison of same row
                    continue
                L[i][a] = A[i][a] / A[j][a] ## Update L matrix before R
                A[i] = A[i] - (A[i][a] / A[j][a])*A[j] ## Update R matrix
                break ## Break not to update a row more than once in one step
    return L, A

