# WAP to find whether the array of integers contains a duplicate number.

print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]

for i in range(0, len(nlist)):    
    for j in range(i+1, len(nlist)):    
        if(nlist[i] == nlist[j]):    
            print("Duplicate number '{0}' found at locations {1} and {2}".format(nlist[j],i,j));   