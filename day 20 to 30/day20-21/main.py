import time
from turtle import Screen
from food import Food
from snake import Snake, generate_border
from scoreboard import ScoreBoard

# bug report:
# after losing score value is set to 0. cause of update method in scoreboard
# fix it in later time.

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turning off tracers. we need to use update() method

# making snake body
snake = Snake()
generate_border()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
print("Begin Moving!")
while game_is_on:
    screen.update()  # updating screen
    time.sleep(0.090)  # sleep it for 0.1 second
    snake.move()

    # checking collision with food
    if snake.head.distance(food) < 15:
        print("Collected")
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        print("wall collision")
    # detect collision with Tail
    for body_part in snake.body_parts[1:]:  # slicing
        if snake.head.distance(body_part) < 10:
            scoreboard.reset()
            snake.reset()
            print("collision with Tail")

screen.exitonclick()
