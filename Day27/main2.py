
import tkinter

window = tkinter.Tk()

window.title("First gui program")
window.minsize(640, 480)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text = "I am a label", font = ("Apple Chancery", 24, "bold"))
my_label.grid(row = 0, column = 0)
my_label.config(padx=10, pady=10)

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

def button_clicked():
    print("Clicked")
    my_label["text"] = input.get()

btn = tkinter.Button(text = "Click me", command=button_clicked)
btn.grid(row = 1, column = 1)
btn.config(padx=10, pady=10)

btn2 = tkinter.Button(text = "Other button")
btn2.grid(row = 0, column = 2)
btn2.config(padx=10, pady=10)


input = tkinter.Entry(width=10)
input.grid(row = 2, column = 3)

window.mainloop()

