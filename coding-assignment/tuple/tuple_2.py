#Convert Tuple to Dictionary
#Question: Write a program to convert a tuple of tuples into a dictionary.

#Solution:

tuples = (('a', 1), ('b', 2), ('c', 3))
dict_from_tuples = dict(tuples)
print(dict_from_tuples)  # Output: {'a': 1, 'b': 2, 'c': 3}