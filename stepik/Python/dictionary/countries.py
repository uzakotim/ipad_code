cities = {}
for _ in range(int(input())):
    inp = input().split()
    cities[inp[0]] = inp[1:]
result = []
for _ in range(int(input())):
    inp = input()
    for key in cities:
        if inp in cities[key]:
            result.append(key)
            break
print(*result,sep='\n')
"""
2
Германия Берлин Мюнхен Гамбург Дортмунд
Нидерланды Амстердам Гаага Роттердам Алкмар
4
Амстердам
Алкмар
Гамбург
Гаага
"""