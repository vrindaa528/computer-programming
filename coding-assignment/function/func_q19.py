#Remove Element from List
#Question: Write a function to remove all occurrences of a specific element from a list.

#Solution:


def remove_element(lst, element):
    return [x for x in lst if x != element]

# Example
result = remove_element([1, 2, 3, 2, 4], 2)
print(result)  # Output: [1, 3, 4]
