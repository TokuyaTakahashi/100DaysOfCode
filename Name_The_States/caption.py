from turtle import Turtle


class Caption(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()

    def write_state(self, state_name, position):
        self.goto(position)
        self.write(f"{state_name}", align='center', font=('Courier', 7, 'normal'))
