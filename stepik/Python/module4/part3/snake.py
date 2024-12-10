[n,m] = [int(x) for x in input().split()]
matrix = [['.']*m for _ in range(n)]
rng = list(range(1,(n*m)+1))
k=0
matrix = []
for i in range(n):
    row = []
    if i%2==0:
        for j in range(m):
            row.append(rng[k])
            k+=1
    else:
        for j in range(m):
            row.append(rng[k])
            k+=1
        row = row[::-1]
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3),end="")
    print()