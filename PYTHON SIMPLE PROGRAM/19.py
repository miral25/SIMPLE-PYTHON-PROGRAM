# WAP to insert a number in an array that is already sorted in ascending order.
import bisect  
  
def insert(list, n): 
    bisect.insort(list, n)  
    return list

print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]
num = int(input("Enter the number to be inserted: "))  

print(insert(nlist, num)) 

'''
 
print("Enter list elements separated by space: ")
nlist = [int(x) for x in input().split()]
num = int(input("Enter the number to be inserted: "))  

k = len(nlist)

for i in range(len(nlist)): 
    if nlist[i] > k: 
        index = i 
        break
res = nlist[: i] + [k] + nlist[i :] 
  
print(res) 

'''
