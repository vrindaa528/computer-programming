#Check for Palindrome
#Question: Write a program to check if a string is a palindrome.

#Solution:

s = "racecar"
is_palindrome = s == s[::-1]
print(is_palindrome)  
