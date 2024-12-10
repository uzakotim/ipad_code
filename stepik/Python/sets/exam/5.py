set1 = {int(x) for x in input().split()}
set2 = {int(x) for x in input().split()}
set3 = set1 & set2
if list(set3):
    print(*sorted(set3,reverse=True))
else:
    print("BAD DAY")
"""
6 56 7 34 14
675 45 246 2 1
"""