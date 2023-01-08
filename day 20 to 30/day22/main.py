from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

scoreboard = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_loop = True
while is_loop:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("hit")
        ball.bounce_x()

    # Detect r_paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_l_score()
        print("miss")

    # left paddle.py Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_r_score()
        print("miss")
screen.exitonclick()
