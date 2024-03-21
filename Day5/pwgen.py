#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

totlen = nr_letters + nr_numbers + nr_symbols
# Make a list of all the character types that will be in the password
list = ['L'] * nr_letters
list.extend(['N'] * nr_numbers)
list.extend(['S'] * nr_symbols)

password = ''
for i in range(0, totlen):
    # For each character in the password, find a random index into the current list of character types
    # Remove the character type at that index
    # Generate a character of that type and append to the password
    # Loop until all of the character types in the list are gone
    currlen = len(list)
    list_index = random.randint(0, currlen - 1)
    char_type = list.pop(list_index)
    if (char_type == 'L'):
        password += letters[random.randint(0, 51)]
    elif (char_type == 'N'):
        password += numbers[random.randint(0, 9)]
    else: # symbol
        password += symbols[random.randint(0, 8)]

print("Generated password: ", password)
