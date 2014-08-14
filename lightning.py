import turtle
import random
import math
import time
screen = turtle.Screen()
screen.screensize(1024,768)
alex = turtle.Turtle()


MAX_ROTATE_ANGLE=90
MAX_DISTANCE=40
MAX_RANGE=20

TRUNK_BRANCH_ODDS=30
LEFT_BRANCH_ODDS=30
RIGHT_BRANCH_ODDS=30


r=147
g=49
b=147

def clearScreen() :
    screen.bgcolor("black")
    screen.colormode(255)

def init():
    alex.penup()
    x=random.randint(-300,300)
    y=random.randint(300,400)
    
    alex.setpos(x, y)
    alex.pendown()
    alex.right(90)
    alex.speed(0)

    
    
def generateRGB():
    global r
    r=random.randint(0,255)
    global g
    g=random.randint(0,255)
    global b
    b=random.randint(0,255)

def drawLightning(step, distance, side) :
    if step> 0:
        for i in range(0,MAX_RANGE):
            alex.pensize(step*2)
            
            alex.pencolor(r,g,b)
            alex.forward(distance)
            
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
            
            alex.setheading(randomAngle)
            
            #recursion does not store turtle position so we we have to do it manually..
            pos=alex.position()
           
            
            #trunk type branch
            rand = random.randint(0,TRUNK_BRANCH_ODDS);
            if rand==0:
                drawLightning(step-1, math.floor(distance/2), 0)   
            
            #left type branch
            rand = random.randint(0,LEFT_BRANCH_ODDS);
            if rand==0:
                drawLightning(step-1, math.floor(distance/2), 1)
            
            #right type branch    
            rand = random.randint(0,RIGHT_BRANCH_ODDS);
            if rand==0:
                drawLightning(step-1, math.floor(distance/2), 2)
            
            # ..and later we should restore the position
            alex.penup()
            alex.setposition(pos) 
            alex.pendown()
    
i=-1
while True:
    i+=1
    if i % 2==0:
        clearScreen()
        time.sleep(1)
        alex.clear()
        i=0
    init()
    generateRGB()
    drawLightning(3, MAX_DISTANCE, 0)
  
turtle.done()