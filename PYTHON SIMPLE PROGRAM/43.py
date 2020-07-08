# WAP to read multiple lines of text and then count the number of characters, words and lines in the text.
import sys
 
fname = input("Enter filename: ")
lines = 0
words = 0
characters = 0
 
for line in open(fname):
    lines += 1
    characters += len(line)
 
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print("Number of Characters:", characters) 
print("Number of Words:", words)
print("Number of Lines:", lines)

