set1 = set([int(x) for x in input().split()])
set2 = set([int(x) for x in input().split()])
lst3 = sorted(set1.difference(set2))
print(*lst3,sep=' ')
