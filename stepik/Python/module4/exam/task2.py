n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

maximal = matrix[n-1][n-1]
for i in range(n):
    for j in range(n):
        if ((i<=j) and (i>=n-1-j)) or ((i>=j)and (i>=n-1-j)):
            if matrix[i][j]>maximal:
                maximal = matrix[i][j]

print(maximal)

"""
3
1 4 5
6 7 8
1 1 6
"""