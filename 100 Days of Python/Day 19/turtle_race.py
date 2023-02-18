import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

x_position = -230
y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=x_position, y=y_position[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You won! The {winner} turtle won the race!")
            else:
                print(f"You lose. You chose {user_bet}. The winner was {winner}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()