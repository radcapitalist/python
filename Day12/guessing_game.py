
from art import logo
from random import randint
from replit import clear

def intro():
    '''
    Print the logo and intro text and establish the level
    '''
    clear()
    print(logo)
    print("\nWelcome to the Number Guessing Game!")
    print("\nI'm thinking of a number between 1 and 100.")
    strLevel = input("Choose a difficulty level: Type 'easy' or 'hard': ").lower()
    if strLevel == "easy":
        return 10
    else:
        return 5

def play():
    number = randint(1, 100)
    guesses_remaining = intro()

    def make_a_guess():
        '''
        Allows the user to make a guess. Returns True if they guessed correct, False otherwise.
        Informs the user whether their guess was too high or too low.
        '''
        print(f"\nYou have {guesses_remaining} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"\n{guess} is the number!  You win!\n")
            return True
        elif guess > number:
            print(f"\n{guess} is too high.")
        else:
            print(f"\n{guess} is too low.")

        return False

    correct = False
    while correct == False and guesses_remaining > 0:
        correct = make_a_guess()
        if not correct:
            guesses_remaining -= 1
            if guesses_remaining > 0:
                print("Guess again.")


    if not correct:
        print("\nYou have run out of guesses; you lose.")

play()


