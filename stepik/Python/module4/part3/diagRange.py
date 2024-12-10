[n,m] = [int(x) for x in input().split()]
matrix = [[0]*m for _ in range(n)]

counter = 0
k = 0

while counter < (n+m):
    for i in range(counter+1):
        for j in range(counter+1):
            if i==counter-1-j:
                try:
                    matrix[i][j] = k
                except:
                    continue
                
    k+=1
    counter +=1
    if k > m: 
        k = 1

for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3),end="")
        print()

"""
0,0
1,0 0,1
2,0 1,1, 0,2

3,0 2,1 1,2 0,3

"""        
"""
3 7
1 2 3 4 5 6 7
2 3 4 5 6 7 1
3 4 5 6 7 1 2
"""