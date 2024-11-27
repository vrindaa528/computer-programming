#Sort Dictionary by Values
#Question: Write a program that sorts a dictionary by its values.

#Solution:

data = {'a': 5, 'b': 10, 'c': 2, 'd': 8}
sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
print(sorted_data)  
# Output: {'c': 2, 'a': 5, 'd': 8, 'b': 10}
