import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)
turtle.speed(0)
snake_body = []
x_coordinate = 0
for i in range(0, 3):
    body_part = Turtle("square")
    body_part.pendown()
    body_part.color("white")
    body_part.setx(x_coordinate)
    snake_body.append(body_part)
    if i >= 1:
        x_coordinate -= 20

snake_head = snake_body[0]
screen.update()


is_game_on = True
while is_game_on:
    screen.update()
    for segment in range(len(snake_body) - 1, 0, -1):
        x_cord = snake_body[segment - 1].xcor()
        y_cord = snake_body[segment - 1].ycor()
        snake_body[segment].goto(x_cord, y_cord)
    snake_head.fd(1)

    def up():
        snake_head.setheading(90)

    def down():
        snake_head.setheading(270)

    def left():
        snake_head.setheading(180)

    def right():
        snake_head.setheading(0)

    screen.listen()
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")


screen.exitonclick()
