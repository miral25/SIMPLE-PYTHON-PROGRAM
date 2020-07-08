'''
In a small company there are 5 salesmen. Each salesman is supposed to sell 3 products. WAP using 2D array to print: 
1.	Total sales by each salesman.
2.	Total sales of each item.
'''
from numpy import *

sales = zeros((5,3),int)
for i in range(5):
    print("\nEnter sales of 3 products sold by salesman %d: "%(i+1))
    for j in range(3):
        sales[i][j] = int(input("Enter product %d: "%(j+1)))

print()        
for i in range(5):
    total_sales = 0
    for j in range(3):        
        total_sales += sales[i][j]
    print("Total Sales by Salesman {0} = {1}".format(i+1,total_sales))
        
print()
for i in range(3):
    total_sales = 0
    for j in range(5):        
        total_sales += sales[j][i]
    print("Total Sales of Product {0} = {1}".format(i+1,total_sales))