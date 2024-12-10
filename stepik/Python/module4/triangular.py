n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

maximum=matrix[0][0]
for i in range(n):
    for j in range(n):
        if ((i>=j and i<=n-1-j) or (i <= j and i>=n-1-j)) and matrix[i][j]>maximum:
            maximum = matrix[i][j]   
print(maximum)