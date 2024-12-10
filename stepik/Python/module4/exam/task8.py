n = int(input())
matrix = [[0]*n for _ in range(n)]

for j in range(n):
    for i in range(n-j):
        matrix[j+i][j] = i
        matrix[j][j+i] = i

def printMatrix(matriix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()


printMatrix(matrix)