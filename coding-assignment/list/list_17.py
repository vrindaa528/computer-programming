#Cartesian Product of Two Lists
#Question: Write a program to compute the Cartesian product of two lists.

#Solution:

from itertools import product

list1 = [1, 2, 3]
list2 = ['a', 'b']
cartesian_product = list(product(list1, list2))
print(cartesian_product)  # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
