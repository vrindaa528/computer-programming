#Write a function that removes duplicates from the list.
#Input: [1, 2, 2, 3, 4, 4, 5]
#Output: [1, 2, 3, 4, 5]
#Explanation: The function will remove all duplicate elements from the list and return the unique elements

lst = [1, 2, 2, 3, 4, 4, 5]
result = list(set(lst))
print(f"List with duplicates removed: {result}")  # Output: [1, 2, 3, 4, 5]
