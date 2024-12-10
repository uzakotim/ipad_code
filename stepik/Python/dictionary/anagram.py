word1 = tuple(input())
word2 = tuple(input())
dict1 = {}
dict2 = {}

for i in word1:
    dict1[i] = dict1.get(i,0)+1
for i in word2:
    dict2[i] = dict2.get(i,0)+1

print("YES" if dict1==dict2 else "NO")

