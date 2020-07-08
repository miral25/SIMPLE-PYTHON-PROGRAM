# WAP to multiply two m x n matrices.

from numpy import *

r1,c1 = [int(i) for i in input("Enter no. of Rows and Columns of the Matrices: ").split()]

a = zeros((r1,c1),int)
print("\nEnter elements of Matrix A: ")
for i in range(r1):
    for j in range(c1):
        a[i][j]=int(input("Enter element A[%d][%d]: "%(i,j)))


b = zeros((r1,c1),int)
print("\nEnter elements of Matrix B: ")
for i in range(r1):
    for j in range(c1):
        b[i][j]=int(input("Enter element B[%d][%d]: "%(i,j)))

print("\nMatrix A:")
print(a)

print("\nMatrix B:")
print(b)

c = zeros((r1,c1),int)
for i in range(len(a)): 
    for j in range(len(b[0])): 
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j] 

print("\nProduct Matrix: ")
print(c)