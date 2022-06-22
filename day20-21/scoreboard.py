from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # use turtle.write command
        self.penup()
        self.color("white")
        self.write(arg=f"Score : {self.score}", move=True, align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.score += 1
