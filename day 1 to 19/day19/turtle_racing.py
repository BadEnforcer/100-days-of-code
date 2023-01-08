from turtle import Turtle, Screen
import random

is_race_on = False
display_1 = Screen()
display_1.setup(width=500, height=400)
user_bet = display_1.textinput(title="Turtle Race!", prompt="Place your Bets by typing the color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
players = []
location_y = 80
for color in colors:
    holder = color
    color = Turtle("turtle")
    color.penup()
    color.color(holder)
    color.goto(-230, location_y)
    location_y -= 30
    players.append(color)

if user_bet:
    is_race_on = True

while is_race_on:
    for player in players:
        if player.xcor() > 230:
            is_race_on = False
            winning_color = player.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The {winning_color} turtle is the Winner.")
            else:
                print(f"You lost. {winning_color} is the winning color.")
        rand_distance = random.randint(0, 10)
        player.forward(rand_distance)

display_1.exitonclick()
