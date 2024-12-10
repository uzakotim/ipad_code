myset = [int(x) for x in input().split()]
answer = [int(x) for x in input().split()]
OK = True
count = 0
for i in answer:
    if i not in myset:
        OK=False
        break
    else:
        count+=1
print("YES" if OK and count>=len(myset) else "NO")
"""
1 2 3 4 8 5
1 2 8 2 3 4 5 2
"""