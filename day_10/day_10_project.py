from os import system
from art import logo

def clear():
    system("clear")

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("what's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"\n{num1} {operation_symbol} {num2} = {answer}")

        if input(f"\nType 'y' to continue calculationg with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()