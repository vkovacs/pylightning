import turtle
import random
wn = turtle.Screen()
alex = turtle.Turtle()
alex.penup()
alex.setpos(0, 300)
alex.left(-90)
alex.pendown()

def lightning(mixdirection, maxdistance, fragment) :
    for i in range(0,fragment):
        rand=random.randint(-mixdirection,mixdirection)
        alex.left(rand)
        distance=random.randint(0,maxdistance)
        alex.forward(distance)
        alex.left(-rand)
        
lightning(40,40,40)
turtle.done()