dictio = {}
com_dict = {'write':'W','read':'R','execute':'X'}
for _ in range(int(input())):
    inp = input().split()
    commands = [inp[x] for x in range(1,len(inp))]
    dictio[inp[0]] = commands
results = []
for _ in range(int(input())):
    inp = input().split()
    if com_dict[inp[0]] in dictio[inp[1]]:
        results.append("OK")
    else:
        results.append("Access denied")
print(*results,sep='\n')
"""
2
marvel_movies X
dc_com X R
2
execute dc_com
write dc_com
"""