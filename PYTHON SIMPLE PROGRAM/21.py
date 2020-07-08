# WAP to merge to two unsorted arrays.

print("Enter elements of List 1 separated by space: ")
list1 = [int(x) for x in input().split()]

print("Enter elements of List 2 separated by space: ")
list2 = [int(x) for x in input().split()]

list3 = list1 + list2
list3.sort()

print("Merged List:",list3)