#Invert a Dictionary

d = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in d.items()}
print(inverted)  # Output: {1: 'a', 2: 'b', 3: 'c'}
