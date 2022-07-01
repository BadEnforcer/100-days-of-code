import time
import turtle

from computer_handle import ComputerHandle
from player_handler import PlayerHandle
from turtle import Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.title("ping pong test")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

com = ComputerHandle()
player = PlayerHandle()


while 1 == 1:
    while com.bottom_handler.ycor() > -280:
        com.go_down()

    while com.bottom_handler.ycor() < 280:
        com.go_up()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_down, "Down")

screen.exitonclick()
