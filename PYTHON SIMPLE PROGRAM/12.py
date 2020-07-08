# WAP to read and display n numbers using an array/list.

print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]

print(nlist)
print("\n")

for x in nlist:
  print(x)