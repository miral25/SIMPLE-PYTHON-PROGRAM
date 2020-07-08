# WAP to find the mean of n numbers using arrays.

print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]

n = len(nlist)
sum1 = 0

for num in nlist:
    sum1 = sum1 + int(num)
    
mean = float(sum1)/n 
print("Mean of n numbers: {0}".format(mean))    