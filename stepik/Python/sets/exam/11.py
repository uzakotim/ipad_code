n = int(input())
sets = []
for i in range(n):
    k = int(input())
    sets.append({input() for _ in range(k)})

total = sets[0]
for i in range(1,n):
    total = total & sets[i]
print(*sorted(total),sep='\n')
"""
2
4
Черкасов
Фокин
Самойлов
Устинов
2
Черкасов
Устинов
"""