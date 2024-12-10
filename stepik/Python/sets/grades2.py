set1 = set([int(x) for x in input().split()])
set2 = set([int(x) for x in input().split()])
set3 = set([int(x) for x in input().split()])

set4 = set1 | set2 | set3
for i in set1:
    if (i in set2) and (i in set3):
        if i in set4:
            set4.remove(i)
for i in set2:
    if (i in set1) and (i in set3):
        if i in set4:
            set4.remove(i)
for i in set3:
    if (i in set1) and (i in set2):
        if i in set4:
            set4.remove(i)

print(*sorted(set4),sep=' ')

"""
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10
"""