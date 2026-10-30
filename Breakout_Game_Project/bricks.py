from turtle import Turtle

def create_bricks():
    bricks = []
    colors = ["red", "orange", "yellow", "green", "blue"]

    for row in range(5):
        for col in range(10):
            brick = Turtle()
            brick.shape("square")
            brick.color(colors[row])
            brick.shapesize(stretch_wid=1, stretch_len=3)
            brick.penup()
            brick.goto(-330 + col * 70, 220 - row * 40)
            bricks.append(brick)

    return bricks
