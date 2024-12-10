set1 = set([int(x) for x in input().split()])
set2 = set([int(x) for x in input().split()])
set3 = set([int(x) for x in input().split()])

set4 = set1 & set2
set5 = set4 - set3
print(*sorted(set5,reverse=True),sep=' ')

"""
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10
"""