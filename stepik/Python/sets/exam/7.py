m = int(input())
n = int(input())
math = set([input() for _ in range(m)])
info = set([input() for _ in range(n)])
set3 = (math | info) - info
print(len(set3))
"""
2
3
Хохлов
Фадеев
Ершов
Ушаков
Хохлов
"""