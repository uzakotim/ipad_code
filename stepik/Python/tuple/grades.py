n = int(input())
students = [tuple([x for x in input().split()]) for _ in range(n)]
for i in students:
    print(" ".join(i))
print()
for i in students:
    if i[1]== '4' or i[1] == '5':
        print(" ".join(i))
