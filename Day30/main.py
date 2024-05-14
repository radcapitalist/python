
import os
import pandas

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

DATA_FNAME = "nato_phonetic_alphabet.csv"

df_phonetic = pandas.read_csv(DATA_FNAME)

dict_phonetic = {row.letter: row.code for (index, row) in df_phonetic.iterrows()}

done = False
while not done:
    word = input("\nInput a word, or 'exit' to exit: ").upper()
    if word == 'EXIT':
        done = True
    else:
        try:
            phonetic = [dict_phonetic[letter] for letter in word]
            print(f"\n{phonetic}\n")
        except KeyError as message:
            print(f"Invalid character ({message}), please only use the alphabet.")
