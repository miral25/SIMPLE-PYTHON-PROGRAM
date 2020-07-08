# WAP to read an array of n numbers and then find the smallest number.
print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]

nlist.sort()
print("Smallest element:",nlist[0])