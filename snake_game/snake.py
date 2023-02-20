from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_seg = []
        self.start_pos = [(-40, 0), (-20, 0), (0, 0)]
        for index in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.pu()
            segment.goto(self.start_pos[index])
            self.snake_seg.append(segment)
        self.head = self.snake_seg[0]

    def move(self):
        for index in range(len(self.snake_seg) - 1, 0, -1):
            x_move = self.snake_seg[index - 1].xcor()
            y_move = self.snake_seg[index - 1].ycor()
            self.snake_seg[index].goto(x_move, y_move)
        self.head.forward(20)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)
