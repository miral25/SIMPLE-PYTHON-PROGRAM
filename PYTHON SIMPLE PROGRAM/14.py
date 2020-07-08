# WAP to print the position of the smallest number of n numbers using arrays.

print("Enter list elements separated by space: ")
list1 = [int(x) for x in input().split()]

list2 = list1.copy()

list2.sort()
small = list2[0]

pos = list1.index(list2[0])
print("The position of the smallest number '{0}' is {1}".format(small,pos))

