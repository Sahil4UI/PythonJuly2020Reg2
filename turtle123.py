import turtle
import random
screen  = turtle.Screen()
pen = turtle.Turtle()
screen.bgcolor(0,0,0)
r =0
g=255
b=0
turtle.colormode(255)
for i in range(0,10000,10):
    pen.circle(10+i)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    pen.color(r,g,b)

