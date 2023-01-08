from turtle import Screen
import pandas
from handler import Operator, image


screen = Screen()
screen.addshape(image)
op = Operator()
screen.setup(height=491, width=725)
screen.title("US States Game")
# screen.tracer(0)

while op.score != 50:
    op.ask()
if op.score == 50:
    pass
screen.exitonclick()
