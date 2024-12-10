dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

myset = set(dict1) | set(dict2)
result = {}
for key in myset:
    if key in dict1 and key in dict2:
        result[key] = dict1[key] + dict2[key]
    elif key in dict1:
        result[key] = dict1[key]
    else:
        result[key] = dict2[key]
        
print(result)