m = int(input())
n = int(input())
set4 = set()
math = set()
for i in range(m):
    name = input()
    if name in math:
        set4.add(name)
    else:
        math.add(name)
        

info = set()
for i in range(n):
    name = input()
    if name in info:
        set4.add(name)
    else:
        info.add(name)

set1 = (math | info) - info
set2 = (math | info) - math
set3 = (set1 | set2) - set4
print(len(set3) if len(set3)!=0 else "NO")
"""
5
4
Демин
Рыбаков
Сафонов
Игнатов
Мухин
Сафонов
Игнатов
Демин
Рыбаков
"""