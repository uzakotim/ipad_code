import random

names = []
n = int(input())
for _ in range(n):
    names.append(input())
rng = list(range(0,n))
result = []
i=0
while len(result)<n:
    selected_friend = random.choice(rng)
    if i != selected_friend:
        result.append(selected_friend)
        rng.remove(selected_friend)
        i+=1

for i in range(n):
    print(names[i] + ' - '+names[result[i]])
"""
Sample Input 2:

5
Владимир Смолов
Тагир Хан
Давид Лавров
Арина Приходько
Глеб Анисимов

Sample Output 2:

Владимир Смолов - Тагир Хан  0 - 1
Тагир Хан - Арина Приходько 1 - 3
Давид Лавров - Глеб Анисимов 2 - 4
Арина Приходько - Владимир Смолов 3 - 0
Глеб Анисимов - Давид Лавров 4 - 2
"""