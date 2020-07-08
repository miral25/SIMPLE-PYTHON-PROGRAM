# WAP to sort the names of the students.

print("Enter name of students separated by space: ")
names = [x for x in input().split()]

sorted_names = sorted(names)
print("Sorted Names: ",sorted_names)