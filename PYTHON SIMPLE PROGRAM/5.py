# WAP to calculate the sum of numbers from m to n.

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

sum1 = 0
i = m
while(i<=n):
    sum1 = sum1 + i
    i = i + 1
    
print("Sum of numbers from {0} to {1}: {2}".format(m,n,sum1))