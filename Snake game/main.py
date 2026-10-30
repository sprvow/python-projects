import time

from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

# SCREEN SETUP
screen = Screen()
screen.setup(width=600, height=600)      # Set the size of the game window
screen.bgcolor("black")                  # Set background color
screen.title("My Snake Game")             # Set window title
screen.tracer(0)                          # Turn off automatic screen updates

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# GAME LOOP
game_is_on = True
while game_is_on:
    screen.update()                       # Update the screen manually
    time.sleep(0.1)                       # Control the speed of the snake

    snake.move()

    #Detect a collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collission with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collission with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #if head collides with any segment in the tail.
        #trigger game_over


screen.exitonclick()                     # Close the window on mouse click