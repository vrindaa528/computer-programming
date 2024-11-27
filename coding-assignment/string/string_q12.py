#Find Common Characters
#Question: Write a program to find common characters between two strings.

#Solution:

s1 = "hello"
s2 = "world"
common_chars = set(s1) & set(s2)
print(common_chars)  # Output: {'o', 'l'}
