from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


game_running = True
screen.update()
snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.listen()

while game_running:
    screen.update()
    time.sleep(.09)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.reset()
    #Detect collision with tail
    for segment in snake.snake_seg[1:-1]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.reset()

screen.exitonclick()