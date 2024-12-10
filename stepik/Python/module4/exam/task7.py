n = input()
alphabet = "abcdefgh"
[x,y] = [8-int(n[1]),alphabet.index(n[0])]
matrix = [['.']*8 for _ in range(8)]
for i in range(8):
    matrix[x][i] = '*'
    matrix[i][y] = '*'
i = -8
while i < 8:
    if ((x+i>-1)and (x+i<8)) and ((y+i>-1)and (y+i<8)):
        matrix[x+i][y+i] = '*'
        i+=1
    else:
        i+=1
        continue
i = -8
while i < 8:
    if ((x-i>-1)and (x-i<8)) and ((y+i>-1)and (y+i<8)):
        matrix[x-i][y+i] = '*'
        i+=1
    else:
        i+=1
        continue
matrix[x][y] = 'Q'



def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()

printMatrix(matrix)