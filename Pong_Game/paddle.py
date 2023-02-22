from turtle import Turtle

MOVE = 20


class Paddle(Turtle):

    def __init__(self, position, name):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(position)
        self.speed("fastest")
        self.name = name
        self.moving = False

    def go_up(self):
        self.start_move()
        self.goto(self.xcor(), self.ycor() + MOVE)

    def go_down(self):
        self.start_move()
        self.goto(self.xcor(), self.ycor() - MOVE)

    def pos_reset(self, position):
        self.moving = False
        self.goto(position)

    def start_move(self):
        self.moving = True