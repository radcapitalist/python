
from tkinter import *
import requests
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_quote():
    kanye = "https://api.kanye.rest"
    response = requests.get(url=kanye)
    response.raise_for_status()
    quote = response.json()["quote"]
    print(quote)
    return quote

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=get_quote(), width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

def on_click():
    canvas.itemconfig(quote_text, text = get_quote())

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=on_click)
kanye_button.grid(row=1, column=0)



window.mainloop()