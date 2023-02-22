from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=500)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

score = Scoreboard()
ball = Ball()
pad_1 = Paddle((-490, 0), "pad_one")
pad_2 = Paddle((480, 0), "pad_two")
screen.update()
game_running = True


# paddle1 controls
screen.onkeypress(fun=pad_1.go_up, key='a')
screen.onkeypress(fun=pad_1.go_down, key='d')

# paddle2 controls
screen.onkeypress(fun=pad_2.go_up, key='Left')
screen.onkeypress(fun=pad_2.go_down, key='Right')


screen.listen()


def reset_game():
    ball.reset_ball()
    pad_2.pos_reset((480, 0))
    pad_1.pos_reset((-490, 0))


while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    if pad_1.moving or pad_2.moving:
        ball.move()

    # paddle collision
    if pad_1.ycor() > 200:
        pad_1.go_down()
    elif pad_1.ycor() < -200:
        pad_1.go_up()

    if pad_2.ycor() > 200:
        pad_2.go_down()
    elif pad_2.ycor() < -200:
        pad_2.go_up()

    # ball collision
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.switch()

    # paddle and ball collision
    if ball.distance(pad_1) < 50 and ball.xcor() < -470:
        ball.hit()
    elif ball.distance(pad_2) < 50 and ball.xcor() > 460:
        ball.hit()

    # ball out of bounds
    if ball.xcor() > 500:
        reset_game()
        score.add_point(pad_1.name)
    elif ball.xcor() < -500:
        reset_game()
        score.add_point(pad_2.name)

screen.exitonclick()
