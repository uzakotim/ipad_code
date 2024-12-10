lines = input().split()
sets = [set(x) for x in lines]
OK = True
for i in range(len(sets)-1):
    if sets[i] == sets[i+1]:
        OK = True
    else:
        OK = False
        break
print("YES" if OK else "NO")

"""
автор товар отвар
"""