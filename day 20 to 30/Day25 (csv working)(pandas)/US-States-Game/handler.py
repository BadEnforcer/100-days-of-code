import turtle
import pandas
from turtle import Turtle

DATA_LOCATION = "50_states.csv"
data = pandas.read_csv(DATA_LOCATION)
image = "blank_states_img.gif"
# we can use .item to grab the data from series too ex - data.state.item()
tim = Turtle()
tim.hideturtle()
tim.penup()

ALL_STATES = {"states": []}
for state in data.state:
    ALL_STATES["states"].append(state)


def get_pos(state_name):
    li_state = data[data.state == state_name]
    x_cord = int(li_state.x)
    y_cord = int(li_state.y)
    return x_cord, y_cord


class Operator(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.default_string = "What's another state's name?"
        turtle.shape(image)

    def ask(self):
        global answered_state
        if self.score == 0:
            answered_state = turtle.textinput(title="Guess the State", prompt=self.default_string).capitalize()
        elif self.score > 0 and self.score != 50:
            answered_state = turtle.textinput(title=f"{self.score}/{len(data.state)} States Correct",
                                              prompt=self.default_string).capitalize()
        self.finish()  # check for finish

        for list_state in data.state:
            if answered_state == list_state:
                ALL_STATES["states"].remove(list_state)
                self.add_score(position=get_pos(answered_state))
            elif answered_state == "Exit":
                df = pandas.DataFrame(ALL_STATES)
                df.to_csv("missed_states.csv")
                exit("0")

    def finish(self):
        if self.score == 50:
            tim.goto(0, 0)
            tim.write(arg="YOU WIN", move=False, font=("Courier", 20, "normal"))

    def add_score(self, position):
        self.score += 1
        print(self.score)
        tim.goto(position)
        tim.write(arg=answered_state, move=False, font=("Courier", 10, "normal"))
