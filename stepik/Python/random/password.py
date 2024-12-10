import random
from string import ascii_letters
from string import digits
array = list(tuple(ascii_letters + digits))
array.remove('l')
array.remove('I')
array.remove('1')
array.remove('O')
array.remove('o')
array.remove('0')
def generate_password(length):
    return random.sample(array,length)

def generate_passwords(count, length):
    for _ in range(count):
        password = generate_password(length)
        print("".join(password))

n, m = int(input()), int(input())
generate_passwords(n,m)

"""
Sample Input 1:
9
7

Sample Output 1:

YbykdW8
heEWSyL
MDxYCzf
syWRujr
mFGBYNJ
bhmg5ip
2XmPgsx
hy7UMVs
JzKPyBw
"""