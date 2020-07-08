# WAP to find the second largest of n numbers using an array.

print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]

nlist.sort()
print("Second largest element:",nlist[-2])

