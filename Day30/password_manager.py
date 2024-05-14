
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

import os
from random import randint, choice, shuffle

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

LOGO = "logo.png"
PWFILE = "passwords.json"
DEFAULT_USERNAME = "eric.hill@outlook.com"

class PasswordEntry:
    def __init__(self, **args):
        self.website = ""
        self.username = ""
        self.password = ""
        if 'key' in args:
            self.website = args["key"]
            entry = args["value"]
            print(f"key: {self.website}, value: {entry}")
            self.username = entry["username"]
            self.password = entry["password"]
        else:
            self.website = args["website"]
            self.username = args["username"]
            self.password = args["password"]

    def set(self, website, user, password):
        self.website = website
        self.username = user
        self.password = password

    def serialize(self):
        return {
            self.website: {
                "username": self.username,
                "password": self.password,
            }
        }
    

class PasswordManager:
    def __init__(self):
        self.entries = []
        if not os.path.exists(PWFILE):
            with open(file = PWFILE, mode = "w") as f:
                pass
        else:
            with open(file = PWFILE) as f:
                entry_dict = json.load(f)
                for (key, value) in entry_dict.items():
                    entry = PasswordEntry(key=key, value=value)
                    self.entries.append(entry)

    def add(self, website, username, password):
        entry = PasswordEntry(website = website, username = username, 
                              password = password)
        self.entries.append(entry)

    def serialize(self):
        with open(file = PWFILE, mode = "w") as f:
            dict = {}
            for entry in self.entries:
                json_entry = entry.serialize()
                print(json_entry)
                for (key, value) in json_entry.items():
                    dict[key] = value
            json.dump(dict, f, indent = 4)

    def find_website(self, website):
        ws_lc = website.lower()
        found_entry = None
        for entry in self.entries:
            if entry.website.lower() == ws_lc:
                found_entry = entry
                break;
        return found_entry
    
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
    
    passwordManager.add(website, username, password)
    input_website.delete(first=0, last=END)
    input_username.delete(first=0, last=END)
    input_username.insert(0, DEFAULT_USERNAME)
    input_pw.delete(first=0, last=END)
    input_website.focus()
    passwordManager.serialize()
    messagebox.showinfo(title="Success!", message="Password successfully saved.")
    
def on_search_clicked():
    website = input_website.get().strip()
    if len(website) <= 0:
        messagebox.showerror(title="No Search Text", message="Enter a website to search for.")

    entry = passwordManager.find_website(website)
    if entry is None:
        messagebox.showerror(title="Failure!", message=f"Website '{website}' not found in database.")
    else:
        messagebox.showinfo(title=entry.website, message=\
                            f"Email: {entry.username}\nPassword: {entry.password}")
    
def on_list_clicked():
    websites = [entry.website for entry in passwordManager.entries]
    list = "\n".join(websites)
    messagebox.showinfo(title="Website List", message=list)

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
input_website = Entry(width = 21)
input_website.grid(row = 1, column = 1)
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
btn_search = Button(text="Search", width = 14, command=on_search_clicked)
btn_search.grid(row=1, column=2)
btn_gen = Button(text="Generate Password", command=on_generate_clicked)
btn_gen.grid(row=3, column=2)

btn_add = Button(text="Add", width=19, command=on_add_clicked)
btn_add.grid(row=4, column=1, columnspan=1)
btn_list = Button(text="List", width=14, command=on_list_clicked)
btn_list.grid(row=4, column=2, columnspan=1)

window.mainloop()
