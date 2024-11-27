#Dictionary Comprehension with Condition

squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
