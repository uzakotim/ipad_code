n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

def isSymmetrical(matrix):
    for i in range(n):
        for j in range(n):
            if (i>j) and matrix[i][j]!=matrix[j][i]:
                print("NO")
                return
    print("YES")

isSymmetrical(matrix)
