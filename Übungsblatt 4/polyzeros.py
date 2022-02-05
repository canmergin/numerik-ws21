import numpy as np

def polyzeros(a):
    x = np.random.random(a.shape[0]-1) + np.random.random(a.shape[0]-1) * 1j ## Assign random values x_0 for all steps
    z = np.zeros(a.shape[0]-1,dtype = complex)  ## Create a complex numbered zero array to save root values
    a_der = np.polyder(a)   ## Calculate the derivative once and save it not to calculate it in every step
    while True:       
        z[0] = x[0] - (np.polyval(a,x[0])/np.polyval(a_der,x[0])) ## Calculate the first root seperately
        if np.abs(np.polyval(a,z[0])) < 1e-12:
            break
        x[0] = z[0]
    for j in range(1,a.shape[0]-1): ## For all the roots other than first one
        while True:  ## Iterate until one of the dividers become zero
            if np.abs(np.polyval(a,x[j])) < 1e-12: ## Break not to divide by zero
                break 
            nennerLinks = (np.polyval(a_der,x[j]))/(np.polyval(a,x[j]))  ## Calculate the left side of the denominator
            nenner = nennerLinks
            for g in range(0,j): 
                if np.abs(x[j]-z[g]) < 1e-12: ## Break not to divide by zero
                    break
                nennerRechts = (1)/(x[j]-z[g])
                nenner -= nennerRechts
            z[j] = x[j] - (1/(nenner))
            if np.abs(np.polyval(a,z[j])) < 1e-12:
                break
            x[j] = z[j]  
    return z
    



## Input
a = np.array([1,0,0,0,-1])
## Output
print(polyzeros(a))
#print(np.roots(a))
## Testing
if np.abs(np.linalg.norm(polyzeros(a))-np.linalg.norm(np.roots(a))) < 1e-12:
    print("Function correct")