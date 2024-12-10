def pascal(n):
    if n == 1:
        return [1]
    triangle = [[1],[1,1]]
    for i in range(2,n):
        init = [1,1]
        for j in range(len(triangle[i-1])-1):
            init.insert(j+1,triangle[i-1][j]+triangle[i-1][j+1])
        triangle.append(init)
    return triangle

def printPascal(triangle):
    if len(triangle) == 1:
        print(str(triangle[0]))
    else:
        for row in triangle:
            print(" ".join([str(x) for x in row]))
n = int(input())
printPascal(pascal(n))