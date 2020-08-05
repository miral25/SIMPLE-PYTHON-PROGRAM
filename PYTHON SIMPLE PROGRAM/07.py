# WAP to determine whether a given number is a prime or a composite number.
num = int(input("Enter a number: "))

if (num > 1):
    for i in range(2, num):
        if (num % i == 0):
            print(num,"is a Composite Number")
            break
    else:
        print(num,"is a Prime Number")
elif (num == 0 or 1):
    print(num,"is neither Prime number nor Composite Number")
