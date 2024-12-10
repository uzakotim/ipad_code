n = int(input())
dictio = {}
for _ in range(n):
    inp = input().split()
    dictio[inp[0]] = inp[1]
word = input()
if word in dictio:
    print(dictio[word])
elif word in dictio.values():
    idx = list(dictio.values()).index(word)
    print(list(dictio.keys())[idx])
"""
4
Awful Terrible
Beautiful Pretty
Great Excellent
Generous Bountiful
Pretty
"""