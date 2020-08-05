'''
WAP to sort the given URLs based on their frequency. 
When two or more URLs have same frequency count then print the lexicographically smaller URL first.
'''
from collections import Counter 
from collections import OrderedDict

url_list = list(input("Enter URL: ").split())

frequency = Counter(url_list)

result = [item for items, c in Counter(sorted(url_list)).most_common() for item in [items] * c] 

result = list(OrderedDict.fromkeys(result))

print("\n\nResult: "+str(result))

#www.google.com www.twitter.com www.google.com www.fb.com