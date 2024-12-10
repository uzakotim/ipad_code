n = int(input())
matrix = [['.' for _ in range(n)] for _ in range(n)]

for j in range(n):
    matrix[n//2][j] = '*'
for i in range(n):
    matrix[i][n//2] = '*'

for i in range(n):
    for j in range(n):
        if (i == j) or (i == n-1-j):
            matrix[i][j] = '*'


for j in range(n):
        for i in range(n):
            print(str(matrix[i][j]),end=" ")
        print()