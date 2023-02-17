import turtle
from turtle import *
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


def herst_painting():
    turtle.colormode(255)
    x_pos = -350
    y_pos = -350

    timmy = Turtle()
    timmy.pu()
    timmy.speed("fastest")
    timmy.setpos(x_pos, y_pos)
    for _ in range(10):
        for _ in range(10):
            timmy.dot(20, random.choice(rgb_colors))
            timmy.pu()
            timmy.forward(50)
        y_pos += 50
        timmy.setpos(x_pos, y_pos)


herst_painting()
screen = turtle.Screen()
screen.exitonclick()

