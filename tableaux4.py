
import numpy as np

x = np.linspace(2,3,5)
x[1] += 1

y = np.zeros(len(x))

for i in range (len(x)):
    y[i] = 4 + 2*i

A = np.zeros((3,5))
A[0,:] = x
A[2,:] = y
A[1,:] = 1
print(A)

