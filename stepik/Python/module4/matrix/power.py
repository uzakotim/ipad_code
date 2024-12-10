import numpy as np
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
power_number = int(input())

init_matrix = matrix[:]
for i in range(power_number-1):
    matrix = list(np.array(matrix).dot(np.array(init_matrix)))

for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]),end=" ")
        print()
