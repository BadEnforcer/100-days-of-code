from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier" , 16, "normal")  # font type, font size, font formatting

class ScoreBoard(Turtle):
    """This will initialize a ScoreBoard on top of the screen."""
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(arg=f"Score : {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=(FONT))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w")as file:
                file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.update_score()


    def update_score(self):
        """Will update score"""
        self.score += 1
        print(f"Food collected. Score: {self.score}")
        self.clear()
        self.write(arg=f"Score : {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=(FONT))

    # def game_over(self):  # useless
    #     """Prints Game over screen"""
    #     print(f"Game over. {self.highscore}")
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=(FONT))