from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    global e_generate_password

    e_generate_password.delete(0,END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    e_generate_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
passwords_dict = {}


def load():
    global passwords_dict
    try:
        with open('pass.json') as fp:
            passwords_dict = json.load(fp)
    except FileNotFoundError:
        return


def save():
    global e_website
    global e_email_username
    global e_generate_password
    global passwords_dict

    web = e_website.get()
    email_username = e_email_username.get()
    password = e_generate_password.get()

    # Check for empty field
    if web == '':
        messagebox.showerror(title='Oops', message='Empty "website" field!')
        return
    elif email_username == '':
        messagebox.showerror(title='Oops', message='Empty "Email/Username" field!')
        return
    elif password == '':
        messagebox.showerror(title='Oops', message='Empty "Password" field!')
        return

    if web not in passwords_dict.keys():
        passwords_dict[web] = (email_username, password)

        with open('pass.json', 'w+') as fp:
            json.dump(passwords_dict, fp, indent=4)

    e_website.delete(0, END)
    # e_email_username.insert(0, 'safian_haq@live.com')
    e_generate_password.delete(0, END)

    print(passwords_dict)

def search():

    global passwords_dict

    web = e_website.get()
    try:
        email_username, password = passwords_dict[web]
        messagebox.showinfo(title=f'Search: {web}', message=f'Email/Username: {email_username}\nPassword: {password}')
    except KeyError:
        messagebox.showerror(title=f'Search: {web}', message=f'Credentials not found.')



load()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
# window.minsize(500,500)
# window.maxsize(500,500)
window.config(pady=50, padx=50)

# Widgets
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
l_website = Label(text='Website:')
l_email_username = Label(text='Email/Username:')
l_password = Label(text='Password:')

b_generate_password = Button(text='Generate Password', width=14, command=generate_password)
b_add = Button(text='Add', width=35, command=save)

b_search = Button(text='Search', command=search, width=14)

e_website = Entry(width=29)
e_website.focus()

e_email_username = Entry(width=50)
e_email_username.insert(0, 'safian_haq@live.com')
e_generate_password = Entry(width=29)

# Widgets Grid
canvas.grid(column=1, row=0)

l_website.grid(column=0, row=1)
e_website.grid(column=1, row=1, sticky='w', padx=4, pady=4)
b_search.grid(column=2, row=1)

l_email_username.grid(column=0, row=2)
e_email_username.grid(column=1, row=2, columnspan=2, pady=4)

l_password.grid(column=0, row=3)
e_generate_password.grid(column=1, row=3, sticky='w', padx=4, pady=4)
b_generate_password.grid(column=2, row=3, sticky='w')

b_add.grid(column=1, row=4, columnspan=2, pady=4)

window.mainloop()
