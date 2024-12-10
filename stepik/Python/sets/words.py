line = list(tuple(input().lower()))

symbols = '.,;:-?!'
for sym in symbols:
    while sym in line:
        line.remove(sym)
line = "".join(line)
words = line.split()
print(len(set(words)))
"""
Milk is white and so is glue, Ghosts are white and they say BOO!
"""