# String is given and left and right integer is given. 
# Left means number of character to be rotated left, and right means number of characters to be rotated right. 
# Find the resultant string. 
# Solution: O(1) possible. Take the difference of left and right. Extract the sub strings, and concatenate them accordingly python

def rotate(input,d):  
    # slice string in two parts for left and right 
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 
  
    # now concatenate two parts together 
    print("\nLeft Rotation : ", (Lsecond + Lfirst))
    print("Right Rotation : ", (Rsecond + Rfirst))
    
    leftrotate = Lsecond + Lfirst
    rightrotate = Rsecond + Rfirst
    
    print("Concatenated substring: ",(leftrotate + rightrotate))

string = input("Enter a String: ")
d=2
rotate(string,d) 