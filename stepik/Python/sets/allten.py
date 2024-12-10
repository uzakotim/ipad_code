line1 = input()
line2 = input()
print('YES' if set(line1+line2) == set([str(x) for x in range(10)]) else 'NO')