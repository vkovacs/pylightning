import turtle
import random
wn = turtle.Screen()
alex = turtle.Turtle()
alex.penup()
alex.setpos(0, 300)
alex.pendown()
alex.right(90)
alex.speed(0)

MAX_ROTATE_ANGLE=90
MAX_DISTANCE=40
MAX_RANGE=20

LEFT_BRANCH_MOD=6
RIGHT_BRANCH_MOD=4

def drawLightning(step, distance, side) :
    if step> 0:
        for i in range(0,MAX_RANGE):
            alex.pensize(step*2)
            alex.forward(distance)
            #randomAngle=random.randint(-MAX_ROTATE_ANGLE,MAX_ROTATE_ANGLE)
            
            #trunk
            if side==0 :
                #180-360
                randomAngle = random.randint(200,340)
            #left
            if side==1 :
                #180-270
                randomAngle = random.randint(200,250)
            #right    
            if side==2:
                #270-360
                randomAngle= random.randint(290,340)
            
            #alex.left(randomAngle)
            alex.setheading(randomAngle)
            
            pos=alex.position()
            heading=alex.heading()
            if i % LEFT_BRANCH_MOD == 0:
                #alex.setheading(180)
                drawLightning(step-1, distance/2, 1)
                #alex.setheading(270)
                
            if i % RIGHT_BRANCH_MOD == 0:
                #alex.setheading(180)
                drawLightning(step-1, distance/2, 2)
                #alex.setheading(270)
                
            alex.penup()
            alex.setposition(pos) 
            alex.pendown()
    

drawLightning(2, MAX_DISTANCE, 0)
turtle.done()