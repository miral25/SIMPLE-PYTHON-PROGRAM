# 36] 	WAP to compare two strings.

s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

if(s1 > s2):
    print(s1,"is greater than",s2)
    print(s1 + "comes after " + s2 + " in the dictionary.")
    
elif(s1 < s2):
    print(s2,"is greater than",s1)
    print(s2 + " comes after " + s1 + " in the dictionary.")
    
else:
    print("The two strings are equal")