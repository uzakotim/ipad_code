def findTrace(matrix):
    total = 0
    for i in range(len(matrix)):
        total+=matrix[i][i]
    return total

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
print(findTrace(matrix))