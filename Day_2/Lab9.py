"""
9. Dictionaries – Merge
Write a program that merges two dictionaries into one. If a key exists in both, the value from
the second dictionary should be used.
"""
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4}
merged_dict = {}

for key in dict1:
    merged_dict[key] = dict1[key]

for key in dict2:
    merged_dict[key] = dict2[key]

print("Merged dictionary:{}".format(merged_dict))
