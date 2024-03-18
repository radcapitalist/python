print("Thank you for choosing Python Pizza Deliveries!")
size = input('What size pizza do you want? S, M, or L: ')
add_pepperoni = input('Do you want pepperoni? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

bill = 0
valid = True
error = ''

if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2
else:
    if (size == 'M'):
        bill = 20
    elif (size == 'L'):
        bill = 25
    else:
        valid = False
        error = f'Specified size ("{size}") is not valid.'

    if valid and add_pepperoni == 'Y':
        bill += 3
        
if not valid:
    print('Invalid order: ' + error)
else:
    if (extra_cheese == 'Y'):
        bill += 1
    print(f'Your final bill is: ${bill}.')
