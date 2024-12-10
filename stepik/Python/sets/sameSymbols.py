n = int(input())
lens = []
for i in range(n):
    lens.append(len(set(input().lower())))
print(*lens,sep='\n')
"""
3
Тимур
Beegeek
АнанАс
"""