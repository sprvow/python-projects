from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import create_bricks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

bricks = create_bricks()

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

game_on = True

while game_on:
    time.sleep(0.01)
    screen.update()

    ball.move()

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    if ball.ycor() > 290:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    for brick in bricks[:]:
        if ball.distance(brick) < 35:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce_y()
            scoreboard.increase_score()

    if ball.ycor() < -300:
        scoreboard.lose_life()

        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_on = False
        else:
            ball.reset_position()

    if len(bricks) == 0:
        scoreboard.next_level()
        bricks = create_bricks()
        ball.speed_up()

screen.exitonclick()
