def merge(values):      # values - это список словарей
    dictio = {}
    for dict in values:
        for key in dict:
            dictio[key] = dictio.get(key, set()) | {dict[key]}
    return dictio

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)