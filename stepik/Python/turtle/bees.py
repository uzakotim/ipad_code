from signal import pause

import turtle

def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

size = int(input())
for _ in range(6):
    hexagon(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.right(60)

pause