# WAP to insert a number at a given location in an array.

print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]

num = int(input("Enter the number to be inserted: "))
pos = int(input("Enter the position at which the number is to be inserted: "))

nlist.insert(pos,num)
print(nlist)