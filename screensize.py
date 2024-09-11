import turtle as trtl
import random

painter = trtl.Turtle()

trtl.screensize(800,800)
painter.speed(0)

rainbow_colors = [ #AI Generated. Prompt: Generate a python list of 10 colors in the rainbow
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
]

position = painter.pos()

for i in reversed(range(5)):
    size = (i+1)*150
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
