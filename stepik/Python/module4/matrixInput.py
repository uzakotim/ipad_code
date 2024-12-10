rows = int(input())
cols = int(input())
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(input())
    matrix.append(row)

for row in matrix:
    print(" ".join(row))

print()
for i in range(cols):
    for j in range(rows):
        print(matrix[j][i],end=" ")
    print()

"""
4
2
и
швец
и
жнец
и
на
дуде
игрец
"""