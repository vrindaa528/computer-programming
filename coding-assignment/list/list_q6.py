#Remove Odd Numbers
#Question: Write a program to remove all odd numbers from a list.

#Solution:


my_list = [1, 2, 3, 4, 5, 6]
even_list = [x for x in my_list if x % 2 == 0]
print(even_list)  
