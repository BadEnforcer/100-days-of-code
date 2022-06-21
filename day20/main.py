import time
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turning off tracers. we need to use update() method

# making snake body
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()  # updating screen
    time.sleep(1)  # sleep it for 0.1 second
    snake.move()
screen.exitonclick()
