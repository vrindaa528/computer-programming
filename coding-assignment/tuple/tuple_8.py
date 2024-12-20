#Count Occurrences of Element in Nested Tuple
#Question: Write a program to count the occurrences of a specific element in a nested tuple.

#Solution:

nested_tuple = ((1, 2, 3), (4, 3, 2, 1), (3, 2, 1))
element = 3
count = sum(t.count(element) for t in nested_tuple)
print(count)  # Output: 3
