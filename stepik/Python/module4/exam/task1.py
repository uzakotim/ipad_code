array = input().split()
n = int(input())
result = []
k = 0
for i in range(n):
    k = i
    temp = []
    while k<len(array):
        temp.append(array[k])
        k+=n
    result.append(temp)
print(result)

"""
a b c d e f g h i j k l m n
3
"""