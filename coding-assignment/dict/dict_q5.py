#Merge Two Dictionaries

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = d1.copy()
for k, v in d2.items():
    if k in merged:
        merged[k] = [merged[k]] if not isinstance(merged[k], list) else merged[k]
        merged[k].append(v)
    else:
        merged[k] = v
print(merged)  #output: {'a': 1, 'b': [2, 3], 'c': 4}
