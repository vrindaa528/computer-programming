#Calculate Running Total
#Question: Write a program to calculate the running total of elements in a list.

#Solution:

my_list = [1, 2, 3, 4, 5]
running_total = [sum(my_list[:i+1]) for i in range(len(my_list))]
print(running_total)  # Output: [1, 3, 6, 10, 15]
