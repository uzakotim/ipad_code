array = [x for x in input().split()]
n = int(input())

def findChunks(array,n):
    chunk  = []
    chunks = []
    k=1
    for i in range(len(array)):
        chunk.append(array[i])
        if k%n == 0:
            chunks.append(chunk)
            chunk = []
        k+=1
    if chunk:
        chunks.append(chunk)
    print(chunks)

findChunks(array,n)
