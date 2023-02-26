from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_mark.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        timer_label.config(fg=GREEN, text='Work')
        countdown(work_sec)
    elif reps % 8 != 0:
        timer_label.config(fg=PINK, text='Break')
        countdown(short_break_sec)
    else:
        timer_label.config(fg=RED, text='Break')
        countdown(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f'0{seconds}'
    formatted = f'{minutes}:{seconds}'
    canvas.itemconfig(timer_text, text=formatted)

    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        marks = ''
        for _ in range(work_sessions):
            marks += '✓'
        check_mark.config(text=f'{marks}')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
tomato_png = PhotoImage(file='tomato.png')

timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer)
reset_button = Button(text='Reset', command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, 'bold'))
check_mark.grid(column=1, row=4)

window.mainloop()