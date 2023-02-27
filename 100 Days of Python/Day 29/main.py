from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
web_entry = Entry(width=52)
web_entry.grid(column=1, row=1, columnspan=2, pady=5)
web_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, pady=5)
pass_entry = Entry(width=30)
pass_entry.grid(column=1, row=3, pady=5, sticky=W)

# Buttons
generate_pass = Button(text='Generate Password', width=15)
generate_pass.grid(column=2, row=3)
add_pass = Button(text='Add', width=44)
add_pass.grid(column=1, row=4, columnspan=2)
window.mainloop()