from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier" , 16, "normal")  # font type, font size, font formatting

class ScoreBoard(Turtle):
    """This will initialize a ScoreBoard on top of the screen."""
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
        """Will update score"""
        self.score += 1
        print(f"Food collected. Score: {self.score}")
        self.clear()
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=(FONT))

    def game_over(self):
        """Prints Game over screen"""
        print(f"Game over. {self.score}")
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=(FONT))