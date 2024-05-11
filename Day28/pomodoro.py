
from tkinter import *
import os

###################
#
# TODO - Make the window pop to the front whenever the timer pops
#
###################

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

TOMATO = "tomato.png"

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#0000ff"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3

WORK_STATE = "Work"
SHORT_BREAK_STATE = "Short Break"
LONG_BREAK_STATE = "Long Break"
WORK_REST_REPS = 4
CHECK = "√"

rep_count = 0
state = None
reset = False
checks = ""

def on_start_clicked():
    global reset
    if state is None:
        reset = False
        countdown(0, 0)

def on_reset_clicked():
    global reset
    reset = True
    print("Reset clicked")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(100, 100)
window.config(padx = 100, pady = 50, bg = YELLOW)
window.geometry("+300+200")

canvas = Canvas(width = 230, height=264, bg = YELLOW, highlightthickness = 0)
tomato_png = PhotoImage(file = TOMATO)
canvas.create_image(110, 132, image = tomato_png)
canvas.grid(row = 1, column = 1)

txt = canvas.create_text(110, 154, text = "00:00", font = (FONT_NAME, 36), fill = "white")

lbl_state = Label(text="Click Start", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 48, "bold"))
lbl_state.grid(row = 0, column = 1)

lbl_checks = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 18))
lbl_checks.grid(row = 3, column = 1)

btn_start = Button(text = "Start", command = on_start_clicked, highlightthickness=0)
btn_start.grid(row = 2, column = 0)

btn_reset = Button(text = "Reset", command = on_reset_clicked, highlightthickness=0)
btn_reset.grid(row = 2, column = 2)

def update_display(state, minutes, seconds):
    disp_seconds = str(seconds)
    if seconds < 10:
        disp_seconds = "0" + str(seconds)
    canvas.itemconfig(txt, text = f"{minutes}:{disp_seconds}")
    color = None
    text = None
    if state is None:
        text = "Click Start"
        color = BLUE
    else:
        text = state
        color = GREEN
        if state == SHORT_BREAK_STATE:
            color = PINK
        elif state == LONG_BREAK_STATE:
            color = RED
    lbl_state.config(text = text, fg = color)
    lbl_checks.config(text = checks)
    

def countdown(minutes, seconds):
    global state, rep_count, reset, checks
    if reset:
        # User clicked Reset - shut it all down
        state = None
        rep_count = 0
        minutes = 0
        seconds = 0
        checks = ""
        reset = False
        update_display(state, minutes, seconds)
        return

    update_display(state, minutes, seconds)

    again = True
    if minutes > 0 or seconds > 0:
        seconds -= 1
        if seconds < 0:
            seconds = 59
            minutes -= 1
        window.after(30, countdown, minutes, seconds)
    else:
        # Our timer has finished.  Change the state and continue timing
        if state is None:
            state = LONG_BREAK_STATE

        if state == WORK_STATE:
            rep_count -= 1
            checks += CHECK
            if rep_count > 0:
                state = SHORT_BREAK_STATE
                window.after(30, countdown, SHORT_BREAK_MIN, 0)
            else:
                state = LONG_BREAK_STATE
                window.after(30, countdown, LONG_BREAK_MIN, 0)
        else: # Must have been in a rest state, time to work again
            # If we just finished a long break, reset the checks
            if state == LONG_BREAK_STATE:
                checks = ""
            state = WORK_STATE
            if rep_count == 0:
                rep_count = 4
            window.after(15, countdown, WORK_MIN, 0)
        
window.mainloop()
