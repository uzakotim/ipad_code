m = int(input())
n = int(input())
math = set([input() for _ in range(m)])
info = set([input() for _ in range(n)])
set1 = (math | info) - info
set2 = (math | info) - math
set3 = set1 | set2
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