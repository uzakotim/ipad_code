n = int(input())
m = int(input())
matrix = [[i*j for i in range(m)] for j in range(n)]
for row in matrix:
    print("".join([str(x).ljust(3) for x in row]))