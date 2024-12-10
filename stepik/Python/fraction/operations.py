from fractions import Fraction as F

str1 = input()
str2 = input()
frac1 = F(str1)
frac2 = F(str2)

print(str1 + ' + ' + str2 + ' = ' + str(frac1+frac2))
print(str1 + ' - ' + str2 + ' = ' + str(frac1-frac2))
print(str1 + ' * ' + str2 + ' = ' + str(frac1*frac2))
print(str1 + ' / ' + str2 + ' = ' + str(frac1/frac2))
