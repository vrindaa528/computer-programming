#Find First Non-Repeating Character
#Question: Write a program to find the first non-repeating character in a string.

#Solution:

s = "swiss"
for char in s:
    if s.count(char) == 1:
        print(char)  # Output: "w"
        break
