#Find Duplicates
#Question: Write a program to find duplicate elements in a list.

#Solution:

my_list = [1, 2, 3, 4, 3, 2, 1]
duplicates = list(set([x for x in my_list if my_list.count(x) > 1]))
print(duplicates)  # Output: [1, 2, 3]
