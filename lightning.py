import turtle
import random
wn = turtle.Screen()
alex = turtle.Turtle()
alex.penup()
alex.setpos(0, 300)
alex.left(-90)
alex.pendown()

for i in range(0,30):
    rand=random.randint(-60,60)
    alex.left(rand)
    distance=random.randint(0,40)
    alex.forward(distance)
    alex.left(-rand)
turtle.done()