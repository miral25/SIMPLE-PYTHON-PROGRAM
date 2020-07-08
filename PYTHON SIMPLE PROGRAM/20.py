# WAP to delete a number from a given location in an array.

print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]

pos = int(input("Enter the position from  which the number is to be deleted: "))

nlist.pop(pos)
print(nlist)