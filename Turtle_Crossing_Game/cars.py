from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color((random.random(), random.random(), random.random()))
        self.shape('square')
        self.shapesize(stretch_len=random.randint(2, 3), stretch_wid=1)
        self.pu()
        self.goto(260, random.randint(-260, 260))
        self.setheading(180)

    def move(self, speed):
        self.forward(speed)

    def restart(self):
        self.color((random.random(), random.random(), random.random()))
        self.shapesize(stretch_len=random.randint(2, 3), stretch_wid=1)
        self.goto(260, random.randint(-260, 260))
