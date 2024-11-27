#Count Vowels
#Question: Write a program to count the number of vowels in a string.

#Solution:

s = "hello world"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print(count)  # Output: 3
