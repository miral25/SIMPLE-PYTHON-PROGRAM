# WAP to interchange the largest and the smallest number in an array.

print("Enter list elements separated by space: ")
list1 = [int(x) for x in input().split()]

list2 = list1.copy()
list2.sort()

pos_s = list1.index(list2[0])
pos_l = list1.index(list2[-1])

temp = list1[pos_s]
list1[pos_s] = list1[pos_l]
list1[pos_l] = temp

print("Interchanged List:",list1)

