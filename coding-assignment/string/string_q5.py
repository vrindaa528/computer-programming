#Anagram Check
#Question: Write a program to check if two strings are anagrams.

#Solution:

s1 = "listen"
s2 = "silent"
is_anagram = sorted(s1) == sorted(s2)
print(is_anagram)  # Output: True
