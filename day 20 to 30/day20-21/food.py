import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # you can adjust the shape size. we are setting it to 10x10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        print(f"Random food spawned")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
