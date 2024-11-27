#List Comprehension with Condition
#Question: Write a program to create a new list from an existing list, containing only the even numbers.

#Solution:

my_list = [1, 2, 3, 4, 5, 6]
even_list = [x for x in my_list if x % 2 == 0]
print
