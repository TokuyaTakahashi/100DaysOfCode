from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clockwise():
    tim.setheading(tim.heading() - 10)


def move_counter():
    tim.setheading(tim.heading() + 10)


def reset():
    tim.speed("fastest")
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()
    tim.speed(8)


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_counter)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=reset)


screen.exitonclick()