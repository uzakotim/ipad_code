n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()
new_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[n-1-j][i])
    new_matrix[i] = row 

printMatrix(new_matrix)


"""
4
1 9 4 2
3 8 1 5
6 7 4 6
1 9 7 8
"""