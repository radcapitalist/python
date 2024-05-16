
from tkinter import *
from tkinter import messagebox

import os
from random import randint, choice, shuffle
import pandas

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

IMG_CARD_BACK = "images/card_back.png"
IMG_CARD_FRONT = "images/card_front.png"
IMG_RIGHT = "images/right.png"
IMG_WRONG = "images/wrong.png"
DATA_FILE = "data/french_words.csv"
NEED_TO_LEARN_FILE = "data/need_to_learn.csv"

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.minsize(500, 400)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.geometry("+300+300")

img_card_front = PhotoImage(file=IMG_CARD_FRONT)
img_card_back = PhotoImage(file=IMG_CARD_BACK)

canvas = Canvas(width=800, height=526, highlightthickness=0,
                bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image = img_card_front, anchor=CENTER)
canvas.grid(row=0, column=0, columnspan=2)

txt_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black", anchor=CENTER)
txt_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black", anchor=CENTER)

ready = True

def show_card(card):
    canvas.itemconfig(card_image, image = img_card_front)
    canvas.itemconfig(txt_title, text = "French", fill="black")
    canvas.itemconfig(txt_word, text = card.french, fill="black")

def flip_card(card):
    global ready
    canvas.itemconfig(card_image, image = img_card_back)
    canvas.itemconfig(txt_title, text = "English", fill="white")
    canvas.itemconfig(txt_word, text = card.english, fill="white")
    ready = True

current_card = None

def new_card():
    global current_card, ready
    current_card = cards.getRandomCard()
    show_card(current_card)
    ready = False
    window.after(3000, flip_card, current_card)

def on_right_clicked():
    cards.drop(current_card)
    if ready:
        new_card()

def on_wrong_clicked():
    if ready:
        new_card()

img_wrong = PhotoImage(file=IMG_WRONG)
btn_wrong = Button(image = img_wrong, highlightthickness=0, command=on_wrong_clicked)
btn_wrong.grid(row=1, column=0)

img_right = PhotoImage(file=IMG_RIGHT)
btn_right = Button(image = img_right, highlightthickness=0, command=on_right_clicked)
btn_right.grid(row=1, column=1)

class Card:
    def __init__(self, index, french, english):
        self.french = french
        self.english = english
        self.index = index

class Cards:
    def __init__(self):
        if os.path.isfile(NEED_TO_LEARN_FILE):
            self.cards = pandas.read_csv(NEED_TO_LEARN_FILE)
        else:
            self.cards = pandas.read_csv(DATA_FILE)

    def getRandomCard(self):
        nrows = self.cards.shape[0]
        print(f"nrows: {nrows}")
        index = randint(0, nrows - 1)
        print(f"nth_card: {index}")
        carddef = self.cards.iloc[index]
        card = Card(index, carddef["French"], carddef["English"])
        return card
    
    def drop(self, card):
        print(card)
        print(card.index)
        self.cards.drop(card.index, inplace=True)
        self.cards.to_csv(NEED_TO_LEARN_FILE, index=False)
        self.cards = pandas.read_csv(NEED_TO_LEARN_FILE)

cards = Cards()

new_card()

window.mainloop()