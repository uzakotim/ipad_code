n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

matrix_elements = []
for i in range(n):
    for j in range(n):
        matrix_elements.append(matrix[i][j])

number = sum(matrix[0])

def checkMatrix(matrix,number):
    flag = True

    for i in range(n):
        if sum(matrix[i])!=number:
            flag = False
            return flag
    for j in range(n):
        total = 0
        for i in range(n):
            total+=matrix[i][j]
        if total!=number:
            flag=False
            return flag
    total = 0
    for i in range(n):
        total+=matrix[i][i]
    if total!=number:
        flag=False
        return flag
    total = 0
    for i in range(n):
        total+=matrix[n-i-1][n-i-1]
    if total!=number:
        flag =False
        return flag
    return flag
    
print("YES" if checkMatrix(matrix,number) and (sorted(matrix_elements) == list(range(1,n*n+1))) else "NO")


