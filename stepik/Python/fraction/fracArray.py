from fractions import Fraction as F
from math import gcd
n = int(input())
lst = []
for i in range(1,n):
    for j in reversed(range(1,n+1)):
        if i<j and gcd(i,j)==1:
            lst.append(F(i,j))
print(*sorted(lst),sep='\n')