from turtle import Turtle

MOVE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(position)
        self.speed("fastest")

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE)


