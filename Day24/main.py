#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

F_ORIG = "./Input/Letters/starting_letter.txt"
F_NAMES = "./Input/Names/invited_names.txt"
F_OUTDIR = "./Output/ReadyToSend/"
FNAME_TMPLT = "letter_to_[NAME].txt"

def compose_letter(name):
    with open(f"{F_ORIG}") as f:
        text = f.read()
        text = text.replace("[name]", name, -1)
    return text

def write_letter(text, name):
    fname = FNAME_TMPLT
    fname = fname.replace("[NAME]", name, 1)
    fname = F_OUTDIR + fname
    with open(fname, "w") as f:
        f.write(text)

with open(f"{F_NAMES}") as f:
    while line := f.readline():
        name = line.strip()
        letter = compose_letter(name)
        write_letter(letter, name)
