from tkinter import *


def button_clicked():
    miles = int(miles_entry.get())
    km = round(miles * 1.609)
    km_conv.config(text=f"{km}")


screen = Tk()
screen.title('Mile to Km Converter')
screen.config(padx=20, pady=20)

my_label = Label(text='is equal to')
my_label.grid(column=0, rowspan=3)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

km_conv = Label(text="0")
km_conv.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(pady=10, padx=10)

button = Button(text="Calculate")
button.config(command=button_clicked)
button.grid(column=1, row=2)


screen.mainloop()
