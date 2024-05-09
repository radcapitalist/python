import tkinter.messagebox
import turtle
import os
import pandas
import tkinter

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

DATA_FNAME = "50_states.csv"
LEARN_FNAME = "states_to_learn.csv"
GIF = "blank_states_img.gif"

state_data = pandas.read_csv(DATA_FNAME)

screen = turtle.Screen()
screen.addshape(GIF)
screen.setup(width=725, height=491)

turtle.shape(GIF)
screen.tracer(0)

stateTurtle = turtle.Turtle()
stateTurtle.penup()
stateTurtle.color("black")
stateTurtle.hideturtle()

TEXT_FONT = "Arial"
TEXT_ALIGN = "center"
TEXT_SIZE = 10

aCorrect = []

def handle_guess(guess):
    global aCorrect
    guess = guess.title()
    found = state_data[state_data["state"] == guess]
    if found.empty:
        msg = f'"{guess}" is not a valid state name!'
        tkinter.messagebox.showinfo("Incorrect!", msg)
    else:
        row = found.index[0]
        found_info = {
            "state": state_data.state[row],
            "x": state_data.x[row],
            "y": state_data.y[row]
        }
        aCorrect.append(found_info["state"])
        stateTurtle.goto(found_info["x"], found_info["y"])
        stateTurtle.write(arg = found_info["state"], \
            align = TEXT_ALIGN, font=(TEXT_FONT, TEXT_SIZE, "normal"))

exit = False
while not exit:
    title = f"{len(aCorrect)}/50 Correct"
    guess = turtle.textinput(title, "Guess a state, or type 'exit' to quit: ")
    if guess == "exit":
        exit = True
    elif guess is None:
        exit = True
    elif guess == "":
        pass
    elif guess == "all":
        all_states = state_data["state"].to_list()
        for state in all_states:
            handle_guess(state)
    else:
        handle_guess(guess)

if exit:
    print(f"\nYou got {len(aCorrect)} states out of 50.")
    df_not_guessed = state_data[~state_data['state'].isin(aCorrect)]
    aNotGuessed = []
    print("\nStates you missed:\n")
    for (index, row) in df_not_guessed.iterrows():
        print(row.state)
        aNotGuessed.append(row.state)
    learn_dict = {
        "state": aNotGuessed
    }
    df_learn = pandas.DataFrame.from_dict(learn_dict)
    df_learn.to_csv(LEARN_FNAME)
    turtle.bye()
else:
    turtle.mainloop()
