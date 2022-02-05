import numpy as np

from vorrueck import *
from lr import *
count = 0
count1 = 0
count2= 0
for i in range(0,1000):
    A = np.array([[1,2,3,4],[6,3,7,4],[3,9,5,3],[0,2,5,7]]);
    A = np.floor(1+np.random.rand(4,4)*10)

    x = np.array([1,1,1,1]);
    x = np.ones(4)

    b = A@x;

    L,R=lr(A+0);

    x0=vorrueck(L+0,R+0,b+0)

    q1 = np.linalg.norm(L@R-A)
    print(q1)
    if q1>1e-12:
        count1 += 1
        print('lr falsch')

    q2 = np.linalg.norm(x0-x)
    ##print(q2)
    if q2>1e-12:
        count += 1
        print('vorrueck falsch')
    if q2>1e-12 and q1<1e-12:
        count2 += 1
        print(A)
        print("")
        print(b)
print(count)
print(count1)
print(count2)