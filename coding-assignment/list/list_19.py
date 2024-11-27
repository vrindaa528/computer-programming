#Rotate a List
#Question: Write a program to rotate a list to the right by a given number of steps.

#Solution:


my_list = [1, 2, 3, 4, 5]
steps = 2
rotated_list = my_list[-steps:] + my_list[:-steps]
print(rotated_list)  # Output: [4, 5, 1, 2, 3]
