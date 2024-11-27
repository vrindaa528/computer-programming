#Find the Longest String
#Question: Write a program to find the longest string in a list of strings.

#Solution:

my_list = ["apple", "banana", "cherry", "date"]
longest_string = max(my_list, key=len)
print(longest_string)  # Output: banana
