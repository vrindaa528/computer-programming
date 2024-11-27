#Find the Smallest Positive Integer Missing from List
#Question: Write a program to find the smallest positive integer that is missing from a list.

#Solution:

my_list = [1, 2, 0, -1, 3, 5]
smallest_missing = 1
while smallest_missing in my_list:
    smallest_missing += 1
print(smallest_missing)  # Output: 4
