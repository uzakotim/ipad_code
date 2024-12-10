n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for j in range(n):
        for i in range(n):
            print(str(matrix[i][j]),end=" ")
        print()
