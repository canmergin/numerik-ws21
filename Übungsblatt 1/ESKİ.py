import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker



figure, (ax1,ax2) = plt.subplots(2, sharex=True)
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.subplot(211)
t = plt.title('s', fontsize=14, color='black')
t1 = np.linspace(0,1,1000)
ax1.axis([0,1,-2,2])
plt.yticks([-2,-1,0,1,2])
plt.xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
plt.grid(True, linestyle='--')
Test = ax1.plot(t1, np.sin(5*t1))
Test1 = ax1.plot(t1, np.cos(5*t1))
plt.setp(Test, color='black', linewidth=0.7)
plt.setp(Test1, color='black', linewidth=0.7)


t2 = np.linspace(-3,3,1000)
Test2 = ax2.plot(t2, np.sin(np.exp(t2)))
plt.setp(Test2, color='black', linewidth=0.7)
ax2.grid(True)
ax1.grid(True)


plt.show()


