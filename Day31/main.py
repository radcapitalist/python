
from tkinter import *
from tkinter import messagebox

import os
from random import randint, choice, shuffle

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

IMG_CARD_BACK = "images/card_back.png"
IMG_CARD_FRONT = "images/card_front.png"
IMG_RIGHT = "images/right.png"
IMG_WRONG = "images/wrong.png"
DATA_FILE = "data/french_words.csv"


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.minsize(500, 400)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
window.geometry("+500+500")

canvas = Canvas(width=800, height=526, highlightthickness=0,
                bg=BACKGROUND_COLOR)
img_card_front = PhotoImage(file=IMG_CARD_FRONT)
canvas.create_image(400, 263, image = img_card_front, anchor=CENTER)
canvas.grid(row=0, column=0, columnspan=2)

txt_title = canvas.create_text(300, 120, text="Title", font=("Arial", 24, "italic"), fill="black")
txt_word = canvas.create_text(280, 180, text="Word", font=("Arial", 36, "bold"), fill="black")

def on_right_clicked():
    pass

def on_wrong_clicked():
    pass

img_wrong = PhotoImage(file=IMG_WRONG)
btn_wrong = Button(image = img_wrong, highlightthickness=0, command=on_wrong_clicked)
btn_wrong.grid(row=1, column=0)

img_right = PhotoImage(file=IMG_RIGHT)
btn_right = Button(image = img_right, highlightthickness=0, command=on_right_clicked)
btn_right.grid(row=1, column=1)

window.mainloop()