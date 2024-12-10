def build_query_string(params):
    results = []
    for key in params:
        result = "=".join([key,str(params[key])])
        results.append(result)
    return "&".join(sorted(results))

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
