# WAP to find whether a string is a palindrome or not.
s = input("Enter a String: ")

if(s == s[::-1]):
    print(s,"is Palindrome")
else:
    print(s,"is Not Palindrome")