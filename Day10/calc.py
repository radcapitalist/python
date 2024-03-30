
from replit import clear
from art import logo

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def compute(first, operation, second):
    """
    Takes two numbers and an operation and computes the value of the equation
    """
    return operations[operation](first, second)

def print_operations():
    for key in operations:
        print(key)

def calculator():
    clear()
    print(logo)
    print()
    first = float(input("First number: "))

    done = False
    while not done:
        second = float(input("Next number: "))
        bOpInvalid = True
        while bOpInvalid:
            print_operations()
            operation = input("Which operation? ")
            if not operation in operations:
                print("Invalid operation, please try again!")
            else:
                bOpInvalid = False
        answer = compute(first, operation, second)
        print()
        print(f"{first} {operation} {second} = {answer}")
        print()
        another = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start anew: ")
        if another == "n":
            calculator()
        else:
            first = answer
            print()

calculator()
