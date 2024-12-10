word = tuple(input())
secret = {}
for i in word:
    secret[i] = secret.get(i,0)+1
signature = {}
for _ in range(int(input())):
    inp = input().split(sep=': ')
    signature[inp[0]] = int(inp[1])
for symbol in secret:
    idx = list(signature.values()).index(secret[symbol])
    secret[symbol] = list(signature.keys())[idx]

result = []
for i in word:
    result.append(secret[i])
print("".join(result))

"""
*!*!*?
3
а: 3
н: 2
с: 1
"""