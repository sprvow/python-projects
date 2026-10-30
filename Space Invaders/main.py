from turtle import *
import random
import time

# ---------------- SCREEN ---------------- #

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

# ---------------- PLAYER ---------------- #

player = Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.goto(0, -250)

# ---------------- BULLET ---------------- #

bullet = Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.3, stretch_len=0.8)
bullet.penup()
bullet.hideturtle()

bullet_state = "ready"

# ---------------- SCORE ---------------- #

score = 0
lives = 3

scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)


def update_score():
    scoreboard.clear()
    scoreboard.write(
        f"Score: {score}   Lives: {lives}",
        align="center",
        font=("Arial", 18, "normal")
    )


update_score()

# ---------------- ALIENS ---------------- #

aliens = []

for row in range(3):
    for col in range(8):

        alien = Turtle()
        alien.shape("circle")
        alien.color("lime")
        alien.penup()

        x = -280 + col * 80
        y = 200 - row * 60

        alien.goto(x, y)

        aliens.append(alien)

alien_speed = 2

# ---------------- CONTROLS ---------------- #

def move_left():
    x = player.xcor() - 25

    if x > -370:
        player.goto(x, player.ycor())


def move_right():
    x = player.xcor() + 25

    if x < 370:
        player.goto(x, player.ycor())


def fire_bullet():
    global bullet_state

    if bullet_state == "ready":

        bullet_state = "fire"

        bullet.goto(
            player.xcor(),
            player.ycor() + 15
        )

        bullet.showturtle()


screen.listen()

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

# ---------------- COLLISION ---------------- #

def collision(t1, t2):
    return t1.distance(t2) < 20


# ---------------- GAME LOOP ---------------- #

game_on = True

while game_on:

    screen.update()
    time.sleep(0.01)

    move_down = False

    for alien in aliens:

        alien.setx(
            alien.xcor() + alien_speed
        )

        # Смяна на посоката

        if alien.xcor() > 370:
            move_down = True

        if alien.xcor() < -370:
            move_down = True

        # Сблъсък с играча

        if collision(alien, player):

            scoreboard.goto(0, 0)

            scoreboard.write(
                "GAME OVER",
                align="center",
                font=("Arial", 28, "bold")
            )

            game_on = False

        # Извънземното е минало зад теб

        if alien.ycor() < -270:

            lives -= 1

            update_score()

            alien.goto(
                random.randint(-300, 300),
                250
            )

            if lives == 0:

                scoreboard.goto(0, 0)

                scoreboard.write(
                    "GAME OVER",
                    align="center",
                    font=("Arial", 28, "bold")
                )

                game_on = False

        # Ударено извънземно

        if bullet_state == "fire":

            if collision(bullet, alien):

                bullet.hideturtle()

                bullet_state = "ready"

                bullet.goto(
                    0,
                    -400
                )

                alien.goto(
                    random.randint(-300, 300),
                    random.randint(150, 250)
                )

                score += 10

                update_score()

    # Всички слизат надолу

    if move_down:

        alien_speed *= -1

        for alien in aliens:

            alien.sety(
                alien.ycor() - 30
            )

    # Движение на куршума

    if bullet_state == "fire":

        bullet.sety(
            bullet.ycor() + 12
        )

        if bullet.ycor() > 300:

            bullet.hideturtle()

            bullet_state = "ready"

screen.exitonclick()