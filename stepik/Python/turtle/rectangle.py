from signal import pause
import turtle

def rectangle(width, height):
    for _ in range(4):
        turtle.forward(height)
        turtle.left(90)
        height, width = width, height


def triangle(side):
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)


def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    
# width = int(input())
# height = int(input())
# rectangle(width,height)

side = int(input())
turtle.setheading(20)
square(side)
turtle.setheading(45)
square(side)
turtle.setheading(65)
square(side)
pause()