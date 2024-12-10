n = int(input())
dictio = {}
for _ in range(n):
    inp = input().split(sep=': ')
    dictio[inp[0].lower()] = inp[1]
k = int(input())
result = []
for _ in range(k):
    inp = input().lower()
    if inp in dictio:
        result.append(dictio[inp])
    else:
        result.append("Не найдено")
print(*result,sep='\n')
"""
5
Змея: язык программирования Python
Баг: от англ. bug — жучок, клоп, ошибка в программе
Конфа: конференция
Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
Бета: бета-версия, приложение на стадии публичного тестирования
3
Змея
Жаба
костыль
"""