#Find All Substrings
#Question: Write a program to find all substrings of a given string.

#Solution:
s = "abc"
substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
print(substrings)  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
