from turtle import Turtle
STARTING_POS = (-280, 40), (-280, 20), (-280, 0), (-280, -20), (-280, -40)
WIDTH = 20
MOVE_DISTANCE = 1


class PlayerHandle:
    def __init__(self):
        self.p_handlers = []
        self.initiate()
        self.top_handler = self.p_handlers[0]
        self.bottom_handler = self.p_handlers[4]

    def initiate(self):
        for pos in STARTING_POS:
            p_handle = Turtle("square")
            p_handle.width(WIDTH)
            p_handle.penup()
            p_handle.color("white")
            p_handle.goto(pos)
            p_handle.setheading(90)
            self.p_handlers.append(p_handle)

    def go_up(self):
        for handler in self.p_handlers[::-1]:
            handler.fd(MOVE_DISTANCE)
        screen.update()
    def go_down(self):
        for handler in self.p_handlers:
            handler.bk(MOVE_DISTANCE)


