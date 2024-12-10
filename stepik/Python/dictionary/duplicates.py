line = list(input().split())
dictio = {}
for x in line:
    dictio[x] = 0
new_line = []
for x in line:
    if dictio[x] != 0:
        new_line.append(f"{x}_{dictio[x]}")
    else:
        new_line.append(x)
    dictio[x]+=1
    
print(" ".join(new_line))

"""
a b c a a d c
a b c a_1 a_2 d c_1
"""