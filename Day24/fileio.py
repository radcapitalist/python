
from random import choice
import os

FNAME = "my_file.txt"

file = None
mode = "a+"
if os.path.exists(FNAME):
    mode = "r+"

words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliett", "kilo", "lima", "mike"]
def make_sentence():
    result = ""
    for i in range(0, 4):
        if not i == 0:
            result += " "
        result += choice(words)
    result += "\n"
    return result

with open(file = FNAME, mode = mode) as f:
    f.seek(0)
    old_data = f.read()
    print(f"Old data: {old_data}")
    f.seek(0)
    f.write(make_sentence())
    f.truncate()
    f.seek(0)
    new_data = f.read()
    print(f"New data: {new_data}")
