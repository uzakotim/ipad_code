n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()

for i in range(n):
    if i>=n/2:
        break
    for j in range(n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-i][j]
            matrix[n-1-i][j] = temp
            
printMatrix(matrix)


"""
0,0 3,0 . 0,1 3,1 . 0,2 3,2 . 0,3 3,3
1,0 2,0 . 1,1 2,1 . 1,2 2,2 . 1,3 2,3  

4
1 2 3 4
5 6 7 8
8 6 4 2
3 4 5 6
"""