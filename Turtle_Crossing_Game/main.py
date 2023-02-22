from turtle import Screen
from player import Player
from level import Level
from cars import Car
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player()
level = Level()
all_cars = []


def create_car():
    new_car = Car()
    return new_car


game_running = True

screen.onkeypress(fun=player.move, key='Up')
screen.listen()
while game_running:
    time.sleep(0.1)
    screen.update()
    car_spawn = random.choice([True, False])
    if car_spawn:
        if len(all_cars) < level.car_amount:
            all_cars.append(create_car())

    for car in all_cars:
        car.move(level.car_speed)

        # car movement
        if car.xcor() < -300:
            car.restart()

        # player clears level
        if player.ycor() > 300:
            player.goto(0, -280)
            level.next()

        # player collision
        if player.distance(car) < 20:
            level.game_over()
            game_running = False

screen.exitonclick()