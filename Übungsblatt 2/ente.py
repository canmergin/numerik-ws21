import numpy as np
import matplotlib.pyplot as plt


def swz(A):
    U, E, VT = np.linalg.svd(A)
    sigma = np.zeros(shape=(A.shape[0],A.shape[1]))
    for i in range(0,sigma.shape[1]):
        if E[i] > 1e-12:
            sigma[i][i]=E[i]
    return U, sigma, VT


A = np.array([[-0.87,0.25],[0.75,0.87]])
U, E, VT = swz(A)
ente = np.array([[0,1,1,1.5,2.5,3,3,4,2,2,1,-3.7,-5,-4,-3,0],
                 [1,0,3.5,4,4,3.5,3,3,2,-1,-2,-2,1,0,1,1]])

t1 = np.linspace(0,2*np.pi,100)
r = 6
x = r*np.cos(t1)
y = r*np.sin(t1)
kreis = np.array([x,y])
plt.rcParams['figure.figsize'] = [16,16]
plt.rcParams["figure.autolayout"] = True

##Untransformiert

plt.subplot(1,4,1)
plt.axis([-10,10,-10,10])
plt.yticks([-10,-5,0,5,10], fontsize=12)
plt.xticks([-10,-0,10],fontsize=12)
plt.title('Ausgangsbild', fontsize=18, color='black')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(ente[0,:],ente[1,:],color='black', linewidth=4)
plt.plot(kreis[0,:],kreis[1,:],color='black', linewidth=4)

##VT transformiert
plt.subplot(1,4,2)
enteVT = VT@ente
kreisVT = VT@kreis
plt.axis([-10,10,-10,10])
plt.yticks([-10,-5,0,5,10], fontsize=12)
plt.xticks([-10,0,10],fontsize=12)
plt.title('nach orth. Trafo. V^T', fontsize=18, color='black')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(enteVT[0,:],enteVT[1,:],color='black', linewidth=4)
plt.plot(kreisVT[0,:],kreisVT[1,:],color='black', linewidth=4)

##E transformiert
plt.subplot(1,4,3)
enteE = E@enteVT
kreisE = E@kreisVT
plt.axis([-10,10,-10,10])
plt.yticks([-10,-5,0,5,10], fontsize=12)
plt.xticks([-10,0,10],fontsize=12)
plt.title('nach Streckung ∑', fontsize=18, color='black')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(enteE[0,:],enteE[1,:],color='black', linewidth=4)
plt.plot(kreisE[0,:],kreisE[1,:],color='black', linewidth=4)

##U transformiert
plt.subplot(1,4,4)
enteU = U@enteE
kreisU = U@kreisE
plt.axis([-10,10,-10,10])
plt.yticks([-10,-5,0,5,10], fontsize=12)
plt.xticks([-10,0,10],fontsize=12)
plt.title('nach orth. Trafo. U', fontsize=18, color='black')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(enteU[0,:],enteU[1,:],color='black', linewidth=4)
plt.plot(kreisU[0,:],kreisU[1,:],color='black', linewidth=4)



plt.show()















