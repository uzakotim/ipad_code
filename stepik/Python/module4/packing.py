array = [[x] for x in input().split()]
i = 0
while i < len(array)-1:
    if array[i+1][0]==array[i][0]:
        array[i]+=array[i+1]
        array.pop(i+1)
        i-=1
    i+=1
print(array)

"""
w w w o r l d g g g g r e a t t e c c h e m g g p w w
"""