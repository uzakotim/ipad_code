set1 = set([int(x) for x in input()])
set2 = set([int(x) for x in input()])
flag = set2.issubset(set1)
print("YES" if flag else "NO")
