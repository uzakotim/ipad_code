n= int(input())
matrix = [[0]*n for _ in range(n)]
for i in range(n):
    matrix[i][n-1-i] = 1

for i in range(n):
    for j in range(n):
        if (i>=j) and (i > n-j-1):
            matrix[i][j] = 2
        if (i<=j) and (i > n-j-1):
            matrix[i][j] = 2

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()