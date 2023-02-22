from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.car_speed = 5
        self.car_amount = 10
        self.hideturtle()
        self.pu()
        self.goto(-150, 270)
        self.write(f"Level: {self.level}", align='right', font=('Courier', 15, 'bold'))

    def next(self):
        self.clear()
        self.level += 1
        self.car_speed += 10
        self.car_amount += 2
        self.write(f"Level: {self.level}", align='right', font=('Courier', 15, 'bold'))

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align='center', font=('Courier', 15, 'bold'))