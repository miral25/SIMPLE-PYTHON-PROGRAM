# WAP to read and display a 2x2x2 array.
from numpy import *
i = j = k = 2

a = zeros((i,j,k),int)
for i in range(2): 
    for j in range(2): 
        for k in range(2):
            a[i][j][k] = int(input("Enter element A[%d][%d][%d]: "%(i,j,k)))

print(a)