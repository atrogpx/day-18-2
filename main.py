import turtle
from turtle import Screen
import random
# turtle.hideturtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# turtle.resizemode("user")
# turtle.pensize(8)
turtle.speed("fastest")
screen = Screen()
print(screen)
# while True:
#     turtle.color(random_color())
#     turtle.setheading(random.randrange(0, 360, 90))
#     turtle.forward(20)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_spirograph(10)
