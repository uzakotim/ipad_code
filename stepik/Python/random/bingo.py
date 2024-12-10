import random
matrix = [[0]*5 for _ in range(5)]
rng = random.sample(list(range(1,75)),24)
k = 0
for i in range(5):
    for j in range(5):
        if not (i==2 and j==2):
            matrix[i][j] = rng[k]
            k+=1

for i in range(5):
    for j in range(5):
        print(str(matrix[i][j]).ljust(3),end='')
    print()
"""
1  16 31 46 61
10 30 42 47 68
3  18 0  48 63
9  19 34 49 70
5  20 35 50 65
"""