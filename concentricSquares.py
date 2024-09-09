import turtle as trtl
import random

painter = trtl.Turtle()

painter.speed(100)

rainbow_colors = [ #AI Generated. Prompt: Generate a python list of 10 colors in the rainbow
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Indigo",
    "Violet",
    "Pink",
    "Light Blue",
    "Light Green"
]

position = painter.pos()

for i in reversed(range(5)):
    size = (i+1)*20
    painter.penup()
    painter.goto(position[0]-size/2,position[1]+size/2)
    painter.begin_fill()
    painter.pendown()
    painter.fillcolor(random.choice(rainbow_colors))
    for g in range(4):
        painter.forward(size)
        painter.right(90)
    painter.end_fill()

trtl.done()
