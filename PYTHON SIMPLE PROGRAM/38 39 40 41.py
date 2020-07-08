# WAP to extract a substring from the middle of a given string.
s1 = input("Enter a String: ")
start = int(input("Enter start of substring: "))
end = int(input("Enter end of substring: "))

print("Substring:",s1[start:end+1:1])


# WAP to insert a string in the main text.
s2 = input("Enter substring: ")
pos = int(input("Enter position at which substring is to be inserted: "))

s3 = s1[:pos] + s2 + s1[pos:]
print("New String:", s3)


#WAP to delete a substring from a text.
s4 = input("Enter a String: ")
start = int(input("Enter start of substring: "))
end = int(input("Enter end of substring: "))

if len(s4) > end:
    s4 = s4[0 : start : ] + s4[end : : ]
print("New String:", s4)


# WAP to replace a pattern with another pattern in the text.
s5 = input("Enter a String: ")
word1 = input("Enter word to be replaced: ")
word2 = input("Enter replacing word: ")

s6 = s5.replace(word1,word2)
print("\nReplaced String:",s6)