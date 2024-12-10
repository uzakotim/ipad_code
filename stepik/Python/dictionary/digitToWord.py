dictio = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
}
number = [int(x) for x in input()]
print(*[dictio[x] for x in number],sep=' ')
"""
230
"""