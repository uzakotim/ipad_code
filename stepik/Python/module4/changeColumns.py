n = int(input())
m = int(input())
matrix = [[int(x) for x in input().split()] for j in range(n)]
[one, two] = [int(x) for x in input().split()]

for i in range(n):
    for j in range(m):
        if j == one:
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][two]
            matrix[i][one] = temp
            continue
        if j == two:
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][one]
            matrix[i][one] = temp
            continue
                

for row in matrix:
    print("".join([str(x).ljust(3) for x in row]))