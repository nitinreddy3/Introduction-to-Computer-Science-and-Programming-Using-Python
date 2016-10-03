"""
ssume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
#s = 'azcbobobegghakl'
result = 0
for i in range(len(s)):
    if i <= len(s) - 3:
        if s[i:i + 3] == 'bob':
            result += 1
print("Number of times bob occurs is: ", result)


