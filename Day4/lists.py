
states = ["Deleware", "Pennsylvania", "New Jersey", "Georgia"]

print(states[-1])

states[1] = 'Pencilvania'
print(states)

states.append('North Carolina')
print(states)


import random
payer = states[random.randint(1, len(states) - 1)]
print(f'{payer} will be paying today.')