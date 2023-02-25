import turtle
import pandas
from caption import Caption

image = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title("US: Name The States")
screen.setup(width=730, height=490)
screen.addshape(image)
turtle.shape(image)
caption = Caption()
data = pandas.read_csv('50_states.csv')
state_arr = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in state_arr if state not in guessed_state]
        states_to_learn = {'states missed': missing_states}
        pandas.DataFrame(states_to_learn).to_csv('states_to_learn.csv')
        break
    if answer_state in state_arr:
        state_x_pos = int(data[data['state'] == answer_state].x)
        state_y_pos = int(data[data['state'] == answer_state].y)
        caption.write_state(answer_state, (state_x_pos, state_y_pos))
        state_arr.pop(state_arr.index(answer_state))
        guessed_state.append(answer_state)

screen.exitonclick()
