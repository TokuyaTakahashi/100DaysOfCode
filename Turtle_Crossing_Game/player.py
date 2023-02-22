from turtle import Turtle
MOVE = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(MOVE)