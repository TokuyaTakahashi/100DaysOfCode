from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_seg = []
        self.create_snake()
        self.head = self.snake_seg[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.pu()
        segment.goto(position)
        self.snake_seg.append(segment)

    def extend(self):
        self.add_segment(self.snake_seg[-1].position())

    def move(self):
        for index in range(len(self.snake_seg) - 1, 0, -1):
            x_move = self.snake_seg[index - 1].xcor()
            y_move = self.snake_seg[index - 1].ycor()
            self.snake_seg[index].goto(x_move, y_move)
        self.head.forward(20)

    def reset(self):
        for seg in self.snake_seg:
            seg.goto(1000,1000)
        self.snake_seg.clear()
        self.create_snake()
        self.head = self.snake_seg[0]

    def left(self):
        self.head.setheading(LEFT)

    def right(self):
        self.head.setheading(RIGHT)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)
