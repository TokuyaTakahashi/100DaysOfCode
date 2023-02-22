from turtle import Turtle
FONT = ('VT323', 50, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_one = 0
        self.score_two = 0
        self.shape('square')
        self.pencolor('white')
        self.hideturtle()
        self.pu()
        self.draw_score()
        # self.draw_line()

    def draw_line(self):
        line = Turtle()
        line.hideturtle()
        line.shape('square')
        line.pencolor('white')
        line.pu()
        line.goto(0, -250)
        line.setheading(90)
        line.width(5)
        while line.ycor() < 250:
            line.pendown()
            line.forward(40)
            line.pu()
            line.forward(40)

    def draw_score(self):
        self.goto(-100, 150)
        self.write(f"{self.score_one}", align='center', font=FONT)
        self.goto(100, 150)
        self.write(f"{self.score_two}", align='center', font=FONT)

    def add_point(self, name):
        self.clear()
        if name == "pad_one":
            self.score_one += 1
        else:
            self.score_two += 1
        self.draw_score()
