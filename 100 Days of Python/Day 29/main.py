from tkinter import *
from tkinter import messagebox
import json
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    url = web_entry.get()
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)

    email = data[url]['email']
    password = data[url]['password']
    messagebox.showinfo(title=f'{url}', message=f'Email: {email}\nPassword: {password}')
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():

    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password": password
        }
    }

    if len(password) != 0 and len(website) != 0:
        try:
            with open('data.json', 'r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            file = open('data.json', 'w')
            json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
    else:
        messagebox.showerror(title='Missing Inputs', message='Please fill all entries')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

logo = PhotoImage(file='logo.png')
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
url_label = Label(text='Website:')
url_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
pass_label = Label(text='Password:')
pass_label.grid(column=0, row=3)

# Entry
web_entry = Entry(width=32)
web_entry.grid(column=1, row=1, columnspan=2, pady=5, sticky=W)
web_entry.focus()
email_entry = Entry(width=52)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, pady=5)
pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3, pady=5, sticky=W)

# Buttons
search_pass = Button(text='Search', width=14, command=search)
search_pass.grid(column=2, row=1)
generate_pass = Button(text='Generate Password', width=15, command=generate_password)
generate_pass.grid(column=2, row=3)
add_pass = Button(text='Add', width=44, command=add)
add_pass.grid(column=1, row=4, columnspan=2)
window.mainloop()