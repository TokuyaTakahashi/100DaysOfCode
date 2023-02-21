from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 275)
        self.hideturtle()
        self.pencolor('white')
        self.write(f"Score: {self.score}", align="center", font=('Courier', 15, 'bold'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Courier', 15, 'bold'))

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=('Courier', 15, 'bold'))