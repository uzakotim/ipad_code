n = int(input())
myset = set([input() for _ in range(n)])
word = input()
print("OK" if word not in myset else "REPEAT")
"""
5
Лас-Вегас
Сеул
Лондон
Ницца
Адел
Лас-Вегас
"""