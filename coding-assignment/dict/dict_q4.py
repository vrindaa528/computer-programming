#Update Nested Dictionary

nested_dict = {'a': {'b': {'c': 42}}}
keys = ['a', 'b', 'c']
value = 100
sub_dict = nested_dict
for key in keys[:-1]:
    sub_dict = sub_dict.setdefault(key, {})
sub_dict[keys[-1]] = value
print(nested_dict)  #output:{'a': {'b': {'c': 100}}}
