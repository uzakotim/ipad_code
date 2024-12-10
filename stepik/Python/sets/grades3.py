set1 = set([int(x) for x in input().split()])
set2 = set([int(x) for x in input().split()])
set3 = set([int(x) for x in input().split()])

set4 = set3 | set2 | set1
set5 = set(list(range(11)))
set6 = set5-set4
print(*sorted(set6),sep=' ')

"""
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10
"""