from fractions import Fraction as F
n = int(input())
sum = F('0')
for i in range(1,n+1):
    sum += F(1,i**2)
print(sum)