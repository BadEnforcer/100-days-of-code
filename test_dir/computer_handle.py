import turtle
from turtle import Turtle
STARTING_POS = (280, 40), (280, 20), (280, 0), (280, -20), (280, -40)
WIDTH = 20
MOVE_DISTANCE = 40


class ComputerHandle:
    def __init__(self):
        self.c_handlers = []
        self.initiate()
        self.top_handler = self.c_handlers[0]
        self.bottom_handler = self.c_handlers[2]

    def initiate(self):
        for pos in STARTING_POS:
            c_handle = Turtle("square")
            c_handle.width(WIDTH)
            c_handle.penup()
            c_handle.color("white")
            c_handle.goto(pos)
            c_handle.setheading(90)
            self.c_handlers.append(c_handle)

    def go_up(self):
        for handler in self.c_handlers[::-1]:
            handler.fd(MOVE_DISTANCE)

    def go_down(self):
        for handler in self.c_handlers:
            handler.bk(MOVE_DISTANCE)



