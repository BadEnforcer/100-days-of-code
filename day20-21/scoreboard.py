from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier" , 16, "normal")  # font type, font size, font formatting

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # use turtle.write command
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=(FONT))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=(FONT))