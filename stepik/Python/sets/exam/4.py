m = int(input())
n = int(input())
home = set([input() for _ in range(m)])
task = [input() for _ in range(n)]
for book in task:
    print("YES" if book in home else "NO")
"""
4
4
Хоббит
Алиса в стране чудес
Том Сойер
Остров сокровищ
Буратино
Хоббит
Остров сокровищ
Война и мир
"""