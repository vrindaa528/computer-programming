#List Comprehension
#Given a list numbers = [1, 2, 3, 4, 5], create a new list that contains the squares of each element.

#Solution

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
