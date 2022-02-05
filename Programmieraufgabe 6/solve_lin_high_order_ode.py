import numpy as np
import matplotlib.pyplot as plt


def solve_lin_high_order_ode(t,p,z,mu,start):
    roots = np.roots(p)
    ## Partikulare Lösung
    y_p = (z/np.polyval(p,mu))*np.exp(mu*t)
    ## Allgemeine Lösung
    mu_j_array = [np.power(mu,x) for x in range(roots.size)]
    abl_links = -(z/np.polyval(p,mu))*np.array(mu_j_array)
    A = np.zeros((roots.size,roots.size),dtype=complex)
    for i in range(roots.size):
        for j in range(roots.size):
            A[i][j] = np.power(roots[j],i)
    b = start+abl_links
    c = np.linalg.solve(A,b)
    y_h = np.zeros(t.size, dtype=complex)
    for z in range(roots.size):
        y_h += np.exp(roots[z]*t)*c[z]
    return y_p + y_h

## Input
p = np.array([1,0.1,17,1,16])
start = np.array([0,0,0,1])
t = np.linspace(0,200,1000)
z = 0
mu = 1j
## Output
y = np.zeros(t.size, dtype=complex)
y = solve_lin_high_order_ode(t,p,z,mu,start)
# Plotting
plt.figure(figsize=(20, 11),constrained_layout = True)
plt.subplot(421)
plt.plot(t,np.real(solve_lin_high_order_ode(t,np.array([1,1]),0,2j,np.array([1]))),color='blue',linewidth=3)
plt.axis([0,50,0,1])
plt.title('z=0', fontsize=12, color='black')

plt.subplot(422)
plt.plot(t,np.real(solve_lin_high_order_ode(t,np.array([2,1,10]),0,1j,np.array([1,0]))),color='blue',linewidth=3)
plt.axis([0,50,-1,1])
plt.title('z=0', fontsize=12, color='black')

plt.subplot(423)
plt.plot(t,np.real(solve_lin_high_order_ode(t,np.array([1,1]),1,2j,np.array([1]))),color='blue',linewidth=3)
plt.plot(t,np.cos(2*t),color='red',linewidth=3)
plt.axis([0,50,-1,1])
plt.title('z=1', fontsize=12, color='black')

plt.subplot(424)
plt.plot(t,np.real(solve_lin_high_order_ode(t,np.array([2,1,10]),1,1j,np.array([1,0]))),color='blue',linewidth=3)
plt.plot(t,np.cos(t),color='red',linewidth=3)
plt.axis([0,50,-1,1])
plt.title('z=1', fontsize=12, color='black')

plt.subplot(425)
plt.plot(t,np.real(solve_lin_high_order_ode(t,np.array([1,0,4]),0,2.1j,np.array([1,0]))),color='blue',linewidth=1.5)
plt.axis([0,200,-1,1])
plt.title('z=0', fontsize=12, color='black')

plt.subplot(426)
plt.plot(t,np.real(solve_lin_high_order_ode(t,np.array([1,0.1,17,1,16]),0,1j,np.array([0,0,0,1]))),color='blue',linewidth=3)
plt.axis([0,100,-0.1,0.1])
plt.title('z=0', fontsize=12, color='black')

plt.subplot(427)
plt.plot(t,np.real(solve_lin_high_order_ode(t,np.array([1,0,4]),1,2.1j,np.array([1,0]))),color='blue',linewidth=1.5)
plt.plot(t,np.cos(2.1*t),color='red',linewidth=3)
plt.axis([0,200,-5,5])
plt.title('z=1', fontsize=12, color='black')

plt.subplot(428)
plt.plot(t,np.real(solve_lin_high_order_ode(t,np.array([1,0.1,17,1,16]),1,1j,np.array([0,0,0,1]))),color='blue',linewidth=3)
plt.plot(t,np.cos(t),color='red',linewidth=3)
plt.axis([0,100,-1,1])
plt.title('z=1', fontsize=12, color='black')
plt.show()


