from turtle import Turtle
import random
MOVE = [10, -10]
START_SPEED = 0.05


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.pu()
        self.speed_x = random.choice(MOVE)
        self.speed_y = random.choice(MOVE)
        self.move_speed = START_SPEED

    def move(self):
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y)

    def switch(self):
        self.speed_y = -1 * self.speed_y

    def hit(self):
        self.speed_x = -1 * self.speed_x
        self.move_speed *= .95

    def reset_ball(self):
        self.goto(0, 0)
        self.speed_x = random.choice(MOVE)
        self.speed_y = random.choice(MOVE)
        self.move_speed = START_SPEED
