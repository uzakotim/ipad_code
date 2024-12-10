n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for row in matrix:
    average = sum(row)/len(row)
    counter = 0
    for j in row:
        if j > average:
            counter+=1
    print(counter)
