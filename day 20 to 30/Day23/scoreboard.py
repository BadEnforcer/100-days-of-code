from turtle import Turtle
FONT = ("LMS I Love This Game", 24, "normal")
# POSITION = (-280, 280)
POSITION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.write(arg=f"Level : {self.level}", move=False, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level : {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=FONT)
