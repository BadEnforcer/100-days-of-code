import turtle
from turtle import Turtle, Screen
import random

# from turtle import *  # this line will import everything form a module. u need to use the * sign
# import turtle as t  # this will alias the module at 't'
timmy = Turtle()
timmy.shape("turtle")
timmy.color("Sky Blue")
turtle.colormode(255)
timmy.speed("fastest")
display_screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spiro(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(120)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spiro(5)
# tuple
# my_tuple = (1 ,3 , 8)
# print(my_tuple[0])  # a tuple value cannot be changed with code. it is set manually. "immutable".
# # what if you want to change the value? well,
# # use list(my_tuple) and convert it into a list. then change its value.


display_screen.exitonclick()  # This needs to oin the bottom of the file

