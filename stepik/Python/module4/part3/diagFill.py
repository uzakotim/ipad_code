[n,m] = [int(x) for x in input().split()]
matrix = [[0]*m for _ in range(n)]

counter = 0
rng = list(range(1,(n*m)+1))
k = 0
while counter < (n+m):
    for i in range(counter+1):
        for j in range(counter+1):
            if i==counter-1-j:
                try:
                    matrix[i][j] = rng[k]
                    k+=1
                except:
                    continue
                
    counter +=1

for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3),end="")
        print()
