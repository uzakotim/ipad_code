wasBefore = []
numbers = [int(x) for x in input().split()]
before = set()
for i in range(len(numbers)):
    if numbers[i] not in before:
        before.add(numbers[i])
        wasBefore.append("NO")
    else:
        wasBefore.append("YES")

print(*wasBefore,sep='\n')
"""
1 1 2 2 5 5 5 5 6 7 8
"""