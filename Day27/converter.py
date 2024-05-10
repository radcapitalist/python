
import tkinter

window = tkinter.Tk()

KM_PER_MILE = 1.609344

window.title("Miles to Kilometers")
window.minsize(100, 100)
window.config(padx = 20, pady = 20)
window.geometry("+600+400")

def convert(miles):
    km = round(miles * KM_PER_MILE * 1000, 3) / 1000
    return '%.2f' % km

def calc_clicked():
    miles = input_miles.get()
    if miles.isdigit():
        lbl_n_km.config(text = convert(float(miles)))
    else:
        lbl_n_km.config(text = "")

def on_enter(event):
    calc_clicked()

input_miles = tkinter.Entry(width = 10)
lbl_miles = tkinter.Label(text = "miles", font = ("Arial", 14))
lbl_isequal = tkinter.Label(text = "is equal to", font = ("Arial", 14))
lbl_n_km = tkinter.Label(text = "", font = ("Arial", 14))
lbl_km = tkinter.Label(text = "km", font = ("Arial", 14))
btn_calc = tkinter.Button(text = "Calculate", command = calc_clicked)

input_miles.grid(row = 0, column = 1)
input_miles.bind("<Return>", on_enter)
lbl_miles.grid(row = 0, column = 2)
lbl_isequal.grid(row = 1, column = 0)
lbl_n_km.grid(row = 1, column = 1)
lbl_km.grid(row = 1, column = 2)
btn_calc.grid(row = 2, column = 1)

window.mainloop()
