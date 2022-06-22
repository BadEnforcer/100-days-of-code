import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turning off tracers. we need to use update() method

# making snake body
snake = Snake()
snake.speed(0)
food = Food()
scoreboard = ScoreBoard()


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

    # checking collision with food
    if snake.head.distance(food) < 15:
        print("Collected")
        food.refresh()
        scoreboard.update_score()
screen.exitonclick()
