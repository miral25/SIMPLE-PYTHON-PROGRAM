# WAP to transpose a n x n matrix.

from numpy import *
row,col = [int(i) for i in input("Enter no. of Rows and Columns of the array: ").split()]

a = zeros((row,col),int)
for i in range(row):
    for j in range(col):
        a[i][j]=int(input("Enter element a[%d][%d]: "%(i,j)))

print("Matrix A:")
print(a)

t = a.transpose()
print("\nTranspose of Matrix A:")
print(t)
