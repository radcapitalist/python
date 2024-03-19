rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import randint
from enum import Enum

graphics = [rock, paper, scissors]

class RockPaperScissors(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

nHuman = None
rpsHuman = None
humanChoice = input('\nEnter 1 for Rock, 2 for Paper, or 3 for Scissors: ')
try:
    nHuman = int(humanChoice)
    rpsHuman = list(RockPaperScissors)[nHuman - 1]
except Exception as e:
    print(f'Invalid choice: {str(e)}')
    raise SystemExit

# Choose for the robot
nRobot = randint(1, 3)
rpsRobot = list(RockPaperScissors)[nRobot - 1]

print(f'\nRobot has chosen:  {str(rpsRobot).split(".")[1]}')
print(graphics[rpsRobot.value])
print(f'You have chosen:   {str(rpsHuman).split(".")[1]}')
print(graphics[rpsHuman.value])
print()

if rpsRobot == rpsHuman:
    print('Tie')
elif rpsRobot == RockPaperScissors.Rock:
    if rpsHuman == RockPaperScissors.Paper:
        print('You win, Paper covers Rock')
    else: # Human chose Scissors
        print('You lose, Rock crushes Scissors')
elif rpsRobot == RockPaperScissors.Paper:
    if (rpsHuman == RockPaperScissors.Rock):
        print('You lose, Paper covers Rock')
    else: # Human chose Scissors
        print('You win, Rock crushes Scissors')
else: # robot chose Scissors
    if (rpsHuman == RockPaperScissors.Rock):
        print('You win, Rock crushes Scissors')
    else: # Human chose Paper
        print('You lose, Scissors cut Paper')

print()
