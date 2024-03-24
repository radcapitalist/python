

import hangman_words as words
import hangman_art as art
import random

correct_guesses = []
incorrect_guesses = []

puzzle = random.choice(words.word_list)
puzzle_lower = puzzle.lower();

def print_puzzle():
    all_correct = True
    output = "";
    for letter in puzzle:
        if letter.lower() in correct_guesses:
            output += letter
        elif letter == ' ':
            output += ' '
        else:
            output += '_'
            all_correct = False
    print(f"{output}\n");
    return all_correct

def compute_lives():
    return 6 - len(incorrect_guesses)

def print_status():
    print(art.stages[compute_lives()])
    print()

done = False;
print(art.logo)
print_status()
print_puzzle()

while not done:
    letter = input('Guess a letter: ')
    if letter in correct_guesses or letter in incorrect_guesses:
        print(f'You already guessed "{letter}"!')
    elif letter in puzzle_lower:
        print(f'"{letter}" is in the puzzle!')
        correct_guesses.append(letter)
    else:
        incorrect_guesses.append(letter)
        print('"{}" is NOT in the puzzle! You\'ve had {} incorrect guesses.'.format(letter, len(incorrect_guesses)))
    print_status()
    winner = print_puzzle()
    loser = compute_lives() == 0
    if winner:
        print('You win!')
    elif loser:
        print('You lose! Here is the answer:\n\n' + puzzle + '\n')
    if winner or loser:
        done = True
