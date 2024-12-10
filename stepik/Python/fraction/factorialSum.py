from fractions import Fraction as F
from math import factorial
n = int(input())
sum = F('0')
for i in range(1,n+1):
    sum += F(1,factorial(i))
print(sum)