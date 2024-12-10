import random
from string import ascii_letters
from string import digits
from string import ascii_lowercase
from string import ascii_uppercase

array = list(tuple(ascii_letters + digits))
array.remove('l')
array.remove('I')
array.remove('1')
array.remove('O')
array.remove('o')
array.remove('0')
def generate_password(length):
    ok1 = False
    ok2 = False
    ok3 = False
    while((ok1+ok2+ok3)!=3):
        ok1 = False
        ok2 = False
        ok3 = False
        password = random.sample(array,length)
        for letter in password:
            if letter in digits:
                ok1 = True
            if letter in ascii_lowercase:
                ok2 = True
            if letter in ascii_uppercase:
                ok3 = True
    return password

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