alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

def encrypt_decrypt(direction, text, shift):
    if direction == 'decode':
        shift = -shift
    cipher_text = ""
    for letter in text:
        if not letter in alphabet:
            cipher_text += letter
        else:
            pos = alphabet.index(letter)
            shiftpos = (pos + shift) % 26
            cipher_text += alphabet[shiftpos]

    if direction == 'encode':
        print(f"The encoded text is {cipher_text}")
    else:
        print(f"The decoded text is {cipher_text}")

again = "yes"
while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypt_decrypt(direction, text, shift)

    again = input("Again? yes/no: ")
