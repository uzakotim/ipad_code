text1 = list(input().lower())
text2 = list(input().lower())
for i in ".,!?:;- ":
    while i in text1:
        text1.remove(i)
    while i in text2:
        text2.remove(i)
dict1 = {}
dict2 = {}

for i in text1:
    dict1[i] = dict1.get(i,0)+1
for i in text2:
    dict2[i] = dict2.get(i,0)+1

print("YES" if dict1==dict2 else "NO")
