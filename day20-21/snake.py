from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# noinspection PyMethodFirstArgAssignment
class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]  # snake head for quick access

    def create_snake(self):
        x_cords = 0
        for number in range(0, 3):
            body_segment = Turtle("square")
            body_segment.color("white")
            body_segment.penup()
            self.body_parts.append(body_segment)

            if number >= 1:
                x_cords -= 20
                body_segment.goto(x_cords, 0)

    def move(self):
        for seg_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[seg_num - 1].xcor()
            new_y = self.body_parts[seg_num - 1].ycor()
            self.body_parts[seg_num].goto(x=new_x, y=new_y)
        self.body_parts[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def speed(self, speed):
        for i in self.body_parts:
            i.speed(speed)
            