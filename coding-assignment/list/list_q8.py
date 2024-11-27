#Check for Sublist
#Question: Write a program to check if one list is a sublist of another.

#Solution:

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4]
is_sublist = all(item in list1 for item in list2)
print("Is sublist:", is_sublist)  # Output: Is sublist: True
