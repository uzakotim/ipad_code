n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
words = ["Верхняя четверть: ","Правая четверть: ","Нижняя четверть: ","Левая четверть: "]
sums = [0]*4
for i in range(n):
    for j in range(n):
        if (i<j and i<n-1-j):
            sums[0] += matrix[i][j]
        if (i<j) and (i>n-1-j):
            sums[1] += matrix[i][j]
        if (i>j) and (i>n-1-j):
            sums[2] += matrix[i][j]
        if (i>j) and (i<n-1-j):
            sums[3] += matrix[i][j]
for i in range(len(sums)):
    print(words[i] + str(sums[i]))