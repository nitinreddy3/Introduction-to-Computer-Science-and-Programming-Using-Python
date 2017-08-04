"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""
# s = 'xdfhyzfdlnskoyeqphtjbhzm'
maxstring = ""  # 保存最长字符串
index = 0  # 保存当前位置
for i in range(len(s)):
    index = i
    while index < len(s) - 1 and s[index + 1] >= s[index]:
        index += 1
    if index - i + 1 > len(maxstring):
        maxstring = s[i:index + 1]
print("Longest substring in alphabetical order is: ", maxstring)
