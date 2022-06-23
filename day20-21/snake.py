from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


# noinspection PyMethodFirstArgAssignment
class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]  # snake head for quick access

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body_segment = Turtle("square")
        body_segment.color("white")
        body_segment.penup()
        body_segment.goto(position)
        self.body_parts.append(body_segment)

    def extend(self):
        self.add_segment(self.body_parts[-1].position())

    def move(self):
        for seg_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[seg_num - 1].xcor()
            new_y = self.body_parts[seg_num - 1].ycor()
            self.body_parts[seg_num].goto(x=new_x, y=new_y)
        self.body_parts[0].fd(MOVE_DISTANCE)

    # player movement
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
