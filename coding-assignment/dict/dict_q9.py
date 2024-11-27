#Filter Dictionary by Value
#Question: Write a program that filters a dictionary to only include items with values greater than a specified threshold.

#Solution:

data = {'a': 5, 'b': 10, 'c': 2, 'd': 8}
threshold = 5
filtered_data = {key: value for key, value in data.items() if value > threshold}
print(filtered_data)# Output: {'b': 10, 'd': 8}
