n = int(input())
z1 = complex(input())
z2 = complex(input())
z1_not = z1.conjugate()
z2_not = z2.conjugate()
print(z1**n + z2**n + z1_not**n + z2_not**(n+1))
"""
1
2+3j
1+4j
"""