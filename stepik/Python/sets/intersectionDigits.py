sets = []
set1 = set()
n = int(input())
for i in range(n):
    sets.append(set([int(x) for x in input()]))
set1 = sets[0]
for i in range(1,n):
    set1.intersection_update(sets[i])
print(*sorted(set1),sep=' ')

"""
4
12345
236
3452222
9302
"""