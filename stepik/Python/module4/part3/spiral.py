[n,m] = [int(x) for x in input().split()]
matrix = [[0]*m for _ in range(n)]
rng = list(range(1,(n*m)+1))

def formSpiral(rng,matrix):
    top = 0
    bottom = n-1
    left = 0
    right = m-1

    index = 0
    while(1):
        if (left>right):
            break
        for i in range(left,right+1):
            matrix[top][i] = rng[index]
            index += 1
        top += 1

        if (top>bottom):
            break

        for i in range(top,bottom+1):
            matrix[i][right] = rng[index]
            index+=1
        right-=1

        if (left > right):
            break

        for i in range(right,left-1,-1):
            matrix[bottom][i] = rng[index]
            index+=1
        bottom -= 1

        if (top>bottom):
            break

        for i in range(bottom,top-1,-1):
            matrix[i][left] = rng[index]
            index+=1
        left+=1



formSpiral(rng,matrix)

for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3),end="")
        print()
