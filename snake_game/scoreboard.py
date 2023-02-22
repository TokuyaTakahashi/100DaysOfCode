from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt', mode='r') as file:
            self.high_score = file.read()
        self.score = 0
        self.goto(0, 275)
        self.hideturtle()
        self.pencolor('white')
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 15, 'bold'))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER", align="center", font=('Courier', 15, 'bold'))
