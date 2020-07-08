# WAP to fill a square matrix with value zero on the diagonals, 1 on the upper right triangle, and -1 on the lower left triangle.

from numpy import *
row,col = [int(i) for i in input("Enter no. of Rows and Columns of the array: ").split()]

a = zeros((row,col),int)
for i in range(row):
    for j in range(col):
        if(i == j):
            a[i][j] = 0
        elif(i>j):
            a[i][j] = -1
        else:
            a[i][j] = 1

print(a)