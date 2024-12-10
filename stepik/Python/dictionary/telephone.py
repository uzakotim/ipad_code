numbers = {}
for _ in range(int(input())):
    inp = input().split()
    numbers[inp[1].lower()] = numbers.get(inp[1].lower(), []) + [inp[0]]
results = []
for _ in range(int(input())):
    inp = input().lower()
    if inp in list(numbers.keys()):
        line = " ".join(list(numbers[inp]))
        results.append(line)
    else:
        results.append("абонент не найден")

print(*results,sep='\n')
"""
3
79184219577 Женя
79194249271 Руслан
79281234567 Женя
3
Руслан
женя
Рустам
"""