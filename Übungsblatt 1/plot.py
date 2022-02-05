import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = [9.75, 7.5]
plt.rcParams["figure.autolayout"] = True
plt.subplot(211)
t1 = np.linspace(0,1,1000)
plt.title('y=sin(5x) und y=cos(5x)', fontsize=12, color='black')
plt.xlabel('x', fontsize=12, color='black')
plt.ylabel('y', fontsize=12, color='black')
plt.axis([0,1,-2,2])
plt.yticks([-2,-1,0,1,2], fontsize=12)
plt.xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],fontsize=12)
plt.grid(True, linestyle='--')
G1_1 = plt.plot(t1, np.sin(5*t1))
G1_2 = plt.plot(t1, np.cos(5*t1))
plt.setp(G1_1, color='black', linewidth=0.6)
plt.setp(G1_2, color='black', linewidth=0.6)


plt.subplot(212)
t2 = np.linspace(-3,3,1000)
plt.title('y=sin(exp(x))', fontsize=12, color='black')
plt.xlabel('x', fontsize=12, color='black')
plt.ylabel('y', fontsize=12, color='black')
plt.axis([-3,3,-1.5,1.5])
plt.yticks([-1.5,-1,-0.5,0,0.5,1,1.5],fontsize=12)
plt.xticks([-3,-2,-1,0,1,2,3],fontsize=12)
G2 = plt.plot(t2,np.sin(np.exp(t2)))
plt.setp(G2, color='black', linewidth=0.6)
plt.grid(False)




plt.show()