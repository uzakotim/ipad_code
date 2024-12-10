dictio = {}
lines = []
for _ in range(int(input())):
    line = input().split()
    lines.append(line)

lines = sorted(lines,key=lambda x:x[0])

for line in lines:
    name = line[0]
    dictio[name] = dictio.get(name, []) + [[line[1],line[2]]]

result = {}
for key in dictio:
    personal_dict= {}
    for item in dictio[key]:
        personal_dict[item[0]] = personal_dict.get(item[0], 0) + int(item[1])
    result[key] = [[prod,personal_dict[prod]] for prod in sorted(personal_dict)]

for key in result:
    print(key+':')
    for prod in result[key]:
        print(prod[0]+ ' '+str(prod[1]))
    
"""
5
Руслан Пирог 1
Тимур Карандаш 5
Руслан Линейка 2
Тимур Тетрадь 12
Руслан Хлеб 3
"""