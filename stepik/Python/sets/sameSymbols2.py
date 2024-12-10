n = int(input())
line = ""
for i in range(n):
    line+=input().lower()
print(len(set(line)))
"""
5
aAa
bB
ccc
dDdd
ppppP
"""