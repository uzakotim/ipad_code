n = int(input())
m = int(input())
matrix = [[int(x) for x in input().split()] for j in range(n)]

maximal = matrix[0][0]
indeces = [0,0]
for i in range(n):
    for j in range(m):
        if matrix[i][j]>maximal:
            maximal = matrix[i][j]
            indeces = [i,j]
print(" ".join([str(x) for x in indeces]))