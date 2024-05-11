
from tkinter import *
from tkinter import messagebox
import pyperclip

import os
from random import randint, choice, shuffle

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

LOGO = "logo.png"
PWFILE = "passwords.txt"
DEFAULT_USERNAME = "eric.hill@outlook.com"

class PasswordEntry:
    def __init__(self, **args):
        self.website = ""
        self.username = ""
        self.password = ""
        if 'textline' in args:
            textline = args['textline']
            parts = textline.split("|")
            self.website = parts[0].strip()
            self.username = parts[1].strip()
            self.password = parts[2].strip()
        else:
            self.website = args["website"]
            self.username = args["username"]
            self.password = args["password"]

    def set(self, website, user, password):
        self.website = website
        self.username = user
        self.password = password

    def serialize(self):
        return f"{self.website} | {self.username} | {self.password}"
    

class PasswordManager:
    def __init__(self):
        self.entries = []
        if not os.path.exists(PWFILE):
            with open(file = PWFILE, mode = "w") as f:
                pass
        else:
            with open(file = PWFILE) as f:
                while line := f.readline():
                    entry = PasswordEntry(textline = line)
                    self.entries.append(entry)

    def add(self, website, username, password):
        entry = PasswordEntry(website = website, username = username, 
                              password = password)
        self.entries.append(entry)

    def serialize(self):
        with open(file = PWFILE, mode = "w") as f:
            text = ""
            for entry in self.entries:
                text += entry.serialize() + "\n"
            f.write(text)
    
passwordManager = PasswordManager()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    pw = "".join(password_list)
    pyperclip.copy(pw)
    return pw

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

def on_generate_clicked():
    genpw = generate_password()
    input_pw.delete(first=0, last=END)
    input_pw.insert(0, genpw)

def on_add_clicked():
    website = input_website.get().strip()
    username = input_username.get().strip()
    password = input_pw.get().strip()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Blank Fields", message='"Website" and "Password" cannot be left blank.')
        return
    
    retval = messagebox.askyesno(title=website, 
                        message=f"You entered:\n\nUsername: {username}\nPassword: {password}\n\nAre you sure you want to save this password?")
    if retval:
        passwordManager.add(website, username, password)
        input_website.delete(first=0, last=END)
        input_username.delete(first=0, last=END)
        input_username.insert(0, DEFAULT_USERNAME)
        input_pw.delete(first=0, last=END)
        input_website.focus()
        passwordManager.serialize()
        messagebox.showinfo(title="Success!", message="Password successfully saved.")
    else:
        messagebox.showinfo(title="Canceled", message="Password not saved.")
    
window = Tk()
window.title("Password Generator")
window.minsize(200, 200)
window.config(padx = 20, pady = 20)
window.geometry("+300+200")

canvas = Canvas(width = 200, height=200, highlightthickness = 0)
logo_png = PhotoImage(file = LOGO)
canvas.create_image(100, 100, image = logo_png, anchor = CENTER)
canvas.grid(row = 0, column = 0, columnspan=3)

lbl_website = Label(text = "Website")
lbl_website.grid(row = 1, column=0)
input_website = Entry(width = 40)
input_website.grid(row = 1, column = 1, columnspan = 2)
input_website.focus()
lbl_username = Label(text="Email/Username")
lbl_username.grid(row=2, column=0)
input_username = Entry(width=40)
input_username.grid(row=2, column=1, columnspan=2)
input_username.insert(0, DEFAULT_USERNAME)
lbl_pw = Label(text = "Password")
lbl_pw.grid(row=3, column=0)
input_pw = Entry(width=21)
input_pw.grid(row=3, column=1)
btn_gen = Button(text="Generate Password", command=on_generate_clicked)
btn_gen.grid(row=3, column=2)

btn_add = Button(text="Add", width=38, command=on_add_clicked)
btn_add.grid(row=4, column=1, columnspan=2)



window.mainloop()