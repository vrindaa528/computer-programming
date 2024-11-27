# Flatten a Nested List
#Question: Write a program to flatten a nested list.

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
