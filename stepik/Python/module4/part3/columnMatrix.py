[n,m] = [int(x) for x in input().split()]
rng = list(range(1,n*m+1))
k = 0
matrix = [[0]*m for _ in range(n)]
for j in range(m):
    for i in range(n):
        matrix[i][j] = rng[k]
        k+=1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3),end="")
    print()