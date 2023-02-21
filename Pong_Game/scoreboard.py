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
        self.draw_line()

    def draw_line(self):
        self.pu()
        self.goto(0, -250)
        self.setheading(90)
        self.width(5)
        while self.ycor() < 250:
            self.pendown()
            self.forward(40)
            self.pu()
            self.forward(40)

    def draw_score(self):
        self.goto(-100, 150)
        self.write(f"{self.score_one}", align='center', font=FONT)
        self.goto(100, 150)
        self.write(f"{self.score_two}", align='center', font=FONT)
