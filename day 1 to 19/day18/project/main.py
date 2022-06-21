import turtle
from tkinter import *
import random
from colors import final_project_colors
from turtle import Turtle, Screen
# dot size = 20
# dots =  10 by 10

tim = Turtle()
tim.hideturtle()
tim.penup()
turtle.colormode(255)
canvas = Screen()
tim.setheading(225)
tim.fd(250)
tim.setheading(0)
tim.speed("fastest")
canvas.screensize(6000, 6000)
for i in range(0, 10):
    tim.dot(20, random.choice(final_project_colors))
    tim.fd(50)


def from_left():
    tim.left(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(500)
    tim.setheading(0)
    for i in range(0, 10):
        tim.dot(20, random.choice(final_project_colors))
        tim.fd(50)


from_left()
from_left()
from_left()
from_left()
from_left()
from_left()
from_left()
from_left()
from_left()

ts = turtle.getscreen()
ts.getcanvas().postscript(file="duck.eps")
canvas.exitonclick()