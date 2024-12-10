n = input()
alphabet = "abcdefgh"
[x,y] = [8-int(n[1]),alphabet.index(n[0])]
matrix = [['.']*8 for _ in range(8)]
poses = [[x+2,y+1],[x+1,y+2],[x-1,y+2],[x-2,y+1],[x-2,y-1],[x-1,y-2],[x+1,y-2],[x+2,y-1]]
matrix[x][y] = 'N'

for pose in poses:
    if (pose[0]<8 and pose[0]>-1) and (pose[1]<8 and pose[1]>-1):
        matrix[pose[0]][pose[1]] = "*"

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()

printMatrix(matrix)
