n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

rng = list(range(1,n+1))

flag = True

for row in matrix:
    if sorted(row)!= rng:
        flag = False
for j in range(n):
    col = []
    for i in range(n):
        col.append(matrix[i][j])
    if sorted(col)!= rng:
        flag = False
    
print("YES" if flag else "NO")