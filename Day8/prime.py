# Write your code below this line 👇

import math

def prime_checker(number):
    max_div = math.floor(math.sqrt(number))
    div = 2
    is_prime = True
    while div <= max_div:
        # print(f'Trying {div}...')
        quotient = number / div
        if quotient == math.floor(quotient):
            # Divisible, this is not a prime number
            is_prime = False
            break
        if div == 2:
            div += 1  # try three next
        else:
            div += 2  # try the next odd number
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)