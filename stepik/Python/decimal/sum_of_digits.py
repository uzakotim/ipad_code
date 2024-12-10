from decimal import *
num = Decimal(input())
num = abs(num)
line = str(num)
num_tuple = num.as_tuple()
if line[0] == '0':
    minimal = 0
else:
    minimal = min(num_tuple.digits)
print(max(num_tuple.digits) + minimal)