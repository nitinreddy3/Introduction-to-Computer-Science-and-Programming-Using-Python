"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""
length = len(s)
maxresult = 1
maxi = 0
maxj = 1
current = 0
indexi = 0
indexj = 0
for i in range(length):
    current = 0
    indexi = i
    indexj = i + 1
    while indexj < length and s[indexj] >= s[indexi]:
        indexi = indexj
        indexj = indexi + 1
        current += 1
    if current > maxresult:
        maxi = i
        maxj = indexj
        maxresult = current
print("Longest substring in alphabetical order is: ",s[maxi:maxj])
