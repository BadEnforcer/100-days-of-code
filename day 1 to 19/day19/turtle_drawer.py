from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.fd(20)


def move_back():
    tim.bk(20)


def turn_right():
    tim.rt(10)


def turn_left():
    tim.lt(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


display_1 = Screen()
display_1.listen()
display_1.onkey(fun=move_forward, key="w")
display_1.onkey(fun=move_back, key="s")
display_1.onkey(fun=turn_left, key="a")
display_1.onkey(fun=turn_right, key="d")
display_1.onkey(fun=clear, key="c")
# we do not use () in this time. cause then the move forward function will tigger before the condition
display_1.exitonclick()
