#Replace List Elements
#Question: Write a program to replace all occurrences of a specified value in a list with a new value.

#Solution:

my_list = [1, 2, 3, 4, 3, 3, 5]
old_value = 3
new_value = 9
replaced_list = [new_value if x == old_value else x for x in my_list]
print(replaced_list)  # Output: [1, 2, 9, 4, 9, 9, 5]
