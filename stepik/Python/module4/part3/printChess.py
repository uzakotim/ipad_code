[n,m] = [int(x) for x in input().split()]
matrix = [['.']*m for _ in range(n)]
for i in range(n):
    if i%2==0:
        for j in range(m):
            if j%2==0:
                matrix[i][j] = '.'
            else:
                matrix[i][j] = '*'
    else:
        for j in range(m):
            if j%2==0:
                matrix[i][j] = '*'
            else:
                matrix[i][j] = '.'

for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=" ")
    print()
            

"""
3 4
"""