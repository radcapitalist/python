
names_string = "Bob, Carol, Ted, Alice, Cheryl, Kim, Frances, Letel"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

index = random.randint(0, len(names) - 1)
payer = names[index]

print(f'{payer} is going to buy the meal today!');