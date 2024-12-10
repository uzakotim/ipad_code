n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()

for i in range(n):
    for j in range(n):
        if i==j:
            temp = matrix[i][i]
            matrix[i][i] = matrix[n-1-i][i]
            matrix[n-1-i][i] = temp
printMatrix(matrix)

"""
5
2 2 3 1 3
4 6 6 7 5
7 8 9 7 8
4 5 6 4 5
1 2 3 1 2
"""