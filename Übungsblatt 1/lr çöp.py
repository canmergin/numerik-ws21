import numpy as np


def lr(A):
    L = np.eye(A.shape[0])
    L = L.astype(np.float64)
    A = A.astype(np.float64)
    
    for a in range(0,A.shape[0]-1): ## The variable for the current column , GAUSS ALGORITHMUS
        for i in range(a+1,A.shape[0]): ## The variable for the current row, the initial value of range is "a+1" to create the triangle shape of R matrix
            for j in range(a,A.shape[0]): ## The variable for comparison row, the initial value of range is "a" to not check back
                B = np.ndarray.copy(A)
                B = B.astype(np.float64)
                if A[i][a] == 0 or A[j][a] == 0: ## To not divide anything by 0
                    continue
                if  i!=j: ## i!=j, so no comparison of same row
                    ##L[i][a] = A[i][a] / A[j][a] ## Update L matrix before R
                    A[i] = A[i] - (A[i][a] / A[j][a])*A[j] ## Update R matrix
                    count = 0
                    for c in range(0, A.shape[0]-1):
                        if A[i][c] == 0:
                            count += 1
                    if count != a+1:
                        A = B
                        continue
                    L[i][a] = B[i][a] / B[j][a]
                    break
    print(L@A)
    print("")
    print(L)
    print("")
    print(A)
    return L, A




R = np.array([[3,6,10,3],
             [5,10,2,4],
             [9,1,4,8],
             [9,3,1,1]]) 

lr(R)


