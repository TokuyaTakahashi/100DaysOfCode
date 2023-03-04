from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACKGROUND = '#91C2AF'
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/1000 japanese frequency translations.csv')
    words_dict = data.to_dict(orient='records')
else:
    words_dict = data.to_dict(orient='records')
timer = 0
word = {}

#-------------------------FUNCTIONS-----------------------------#


def new_word():
    global word
    word = random.choice(words_dict)
    set_word(word['Japanese'])
    countdown(3)


def correct():
    global word, words_dict
    words_dict.remove(word)
    print(len(words_dict))
    data = pandas.DataFrame(words_dict)
    data.to_csv('./data/words_to_learn.csv', index=False)
    new_word()


def countdown(count):
    global timer, word
    if count == 0:
        screen.after_cancel(timer)
        translation = word['English']
        lang_label.config(text='English', bg=CARD_BACKGROUND, fg='white')
        word_label.config(text=f'{translation}', bg=CARD_BACKGROUND, fg='white')
        canvas.itemconfig(canvas_image, image=card_back)
    else:
        timer = screen.after(1000, countdown, count - 1)


def set_word(jpn_word):
    lang_label.config(text='Japanese', bg='white', fg='black')
    word_label.config(text=f'{jpn_word}', bg='white', fg='black')
    canvas.itemconfig(canvas_image, image=card_front)

#----------------------------UI---------------------------------#


screen = Tk()
screen.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
screen.title('Japanese Flashcards')

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas = Canvas(width=900, height=626, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(450, 313, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

lang_label = Label(font=('Ariel', 40, 'italic'), text='Japanese', bg='white')
word_label = Label(font=('Ariel', 60, 'bold'), text='sample', bg='white')
lang_label.place(x=320, y=150)
word_label.place(x=320, y=263)

check_mark = PhotoImage(file='./images/right.png')
x_mark = PhotoImage(file='./images/wrong.png')
correct_button = Button(image=check_mark, width=100, height=100,
                        highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=correct)
wrong_button = Button(image=x_mark, width=100, height=100,
                      highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=new_word)
correct_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)
screen.mainloop()