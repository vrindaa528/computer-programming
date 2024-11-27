#Swap Tuple Elements
#Question: Write a program to swap the first and last elements of a tuple.

#Solution:


my_tuple = (1, 2, 3, 4, 5)
swapped_tuple = (my_tuple[-1],) + my_tuple[1:-1] + (my_tuple[0],)
print(swapped_tuple)  # Output: (5, 2, 3, 4, 1)
