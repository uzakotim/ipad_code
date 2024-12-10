text = input()
symbols = '.,;:-?!()'
line = list(tuple(text.lower()))
for sym in symbols:
    while sym in line:
        line.remove(sym)
line = "".join(line)
words = line.split()
dictio = {}
for x in words:
    dictio[x] = dictio.get(x, 0) + 1
result = sorted(dictio.items(),key=lambda x: x[0])
print(min(result,key = lambda x:x[1])[0])
"""
home sweet home sweet.
"""