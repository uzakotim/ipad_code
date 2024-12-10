import random
from string import ascii_uppercase
def generate_index():
    first = "".join(random.sample(ascii_uppercase,2))
    second = "".join(random.sample(ascii_uppercase,2))
    third = str(random.choice(list(range(10,100))))
    fourth = str(random.choice(list(range(10,100))))
    return first+third+'_'+fourth+second

print(generate_index())




"""
AB23_56VG
"""