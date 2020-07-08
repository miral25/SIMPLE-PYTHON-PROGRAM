# WAP to calculate the average of first n numbers.

n = int(input("Enter value of n: "))
sum1 = 0

for i in range(0,n+1):
    sum1 = sum1 + i
    
avg = float(sum1)/n
print("Average of first n numbers: {0}".format(avg))    