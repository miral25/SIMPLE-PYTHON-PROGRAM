'''
WAP to read a 2D array marks which stores the marks of 5 students in 3 subjects.  
WAP to display the highest marks in each subject.
'''
ALLOW_THREADS()from numpy import *
 
marks = zeros((5,3),int)
for i in range(5):
    print("\nEnter marks obtained by student %d: "%(i+1))
    for j in range(3):
        marks[i][j] = int(input("Enter marks %d: "%(j+1)))

print()

for i in range(3):
    max_marks = 0
    for j in range(5): 
        if(marks[j][i] > max_marks):
            max_marks = marks[j][i]
    print("Highest marks obtained in Subject {0} = {1}".format(i+1, max_marks))