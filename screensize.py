import turtle


screen = turtle.Screen()
screen.setup(width=800, height=800)


painter = turtle.Turtle()
painter.hideturtle()
painter.speed(0) 

num_objects = 5  
object_size = 20  

total_space = 800 - 2 * object_size
spacing = total_space / (num_objects - 1) if num_objects > 1 else 0

start_x = -total_space / 2
start_y = 0
for i in range(num_objects):
    x = start_x + i * spacing
    painter.penup()
    painter.goto(x, start_y)
    painter.pendown()
    painter.circle(object_size) 

turtle.done()