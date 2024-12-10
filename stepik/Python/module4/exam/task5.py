n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

def isSymmetrical(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i<n-1-j) and matrix[i][j]!=matrix[n-1-j][n-1-i]:
                print("NO")
                return 
    print("YES")

isSymmetrical(matrix)
# for i in range(n):
#         for j in range(n):
#             print(str(matrix[i][j]),end=" ")
#         print()
"""
0,0 2,2
0,1 1,2
1,0 2,1

"""

"""
3
0 3 10
4 9 3
7 4 0
"""