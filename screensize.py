import turtle as trtl

painter = trtl.Turtle()

trtl.screensize(800,800)
painter.speed(0)
screen = [800,800]

def drawSquares():
    for i in range(4):
        painter.forward(20)
        painter.right(90)

distance = screen[0]/5

for i in range(5):
    painter.penup()
    painter.goto(((i+1)*distance)-400,0)
    painter.pendown()
    drawSquares()

