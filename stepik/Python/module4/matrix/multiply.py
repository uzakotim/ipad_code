import numpy as np
[n1,m1] = [int(x) for x in input().split()]
matrix1 = [[int(x) for x in input().split()] for _ in range(n1)]
i = input()
[n2,m2] = [int(x) for x in input().split()]
matrix2 = [[int(x) for x in input().split()] for _ in range(n2)]


matrix3 = list(np.array(matrix1).dot(np.array(matrix2)))

for i in range(len(matrix3)):
        for j in range(len(matrix3[0])):
            print(str(matrix3[i][j]),end=" ")
        print()
