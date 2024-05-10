
import tkinter

window = tkinter.Tk()

window.title("First gui program")
window.minsize(640, 480)

my_label = tkinter.Label(text = "I am a label", font = ("Apple Chancery", 24, "bold"))
my_label.pack(side="top")
my_label.config(text = "Better and better")

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(n, **ops):
    val = n
    val += ops['add']
    val *= ops['multiply']
    return val

label2 = tkinter.Label(text = add(2, 4, 6, 8, 10), font = ("Apple Chancery", 24, "bold"))
label2.pack(side="bottom")

label3 = tkinter.Label(text = calculate(3, add = 4, multiply = 5), font = ("Apple Chancery", 24, "bold"))
label3.pack(side="bottom")
label3["text"] = "changed text"

def button_clicked():
    print("Clicked")
    my_label["text"] = input.get()

btn = tkinter.Button(text = "Click me", command=button_clicked)
btn.pack(side = "top")

input = tkinter.Entry(width=10)
input.pack()

window.mainloop()

