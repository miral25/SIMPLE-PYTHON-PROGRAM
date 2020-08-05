# WAP to find whether a number is even or odd using functions

def odd_even(num):
    if (num%2==0):
        return 1
    else:
        return 0
    
num = int(input("Enter a number: "))    

flag = odd_even(num)

if(flag == 1):
    print(num,"is Even")
else:
    print(num,"is Odd")

    
''' # WAP to find whether a number is even or odd
num = int(input("Enter a number: "))     

if (num%2==0):
    print(num,"is Even")
        
else:
    print(num,"is Odd")
     
'''
