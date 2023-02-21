from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=1000, height=500)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

game_running = True
score = Scoreboard()
pad_1 = Paddle((-480, 0))
pad_2 = Paddle((480, 0))
screen.update()

# paddle1 controls
screen.onkeypress(fun=pad_1.go_up(), key='a')
screen.onkeypress(fun=pad_1.go_down(), key='d')

# paddle2 controls
screen.onkeypress(fun=pad_2.go_up(), key='Left')
screen.onkeypress(fun=pad_2.go_down(), key='Right')

screen.listen()

while game_running:
    screen.update()

    if pad_1.ycor() > 200:
        pad_1.go_down()
    elif pad_1.ycor() < -200:
        pad_1.go_up()

    if pad_2.ycor() > 200:
        pad_2.go_down()
    elif pad_2.ycor() < -200:
        pad_2.go_up()


screen.exitonclick()
