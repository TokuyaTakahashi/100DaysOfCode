import turtle
from caption import Caption
image = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title("US: Name The States")
screen.setup(width=730, height=490)
screen.addshape(image)
turtle.shape(image)

caption = Caption()
answer_state = screen.textinput(title="Guess The State", prompt="What's another state's name?")

screen.exitonclick()