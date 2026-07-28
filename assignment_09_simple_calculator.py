# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    print("\n" + "=" * 30)
    print("     SIMPLE CALCULATOR")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def exponentiation(a, b):
    return a ** b


def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ")
        
        if choice == "1":
            a, b = get_numbers()
            result = addition(a, b)
            print(f"Result: {a} + {b} = {result}")
        
        elif choice == "2":
            a, b = get_numbers()
            result = subtraction(a, b)
            print(f"Result: {a} - {b} = {result}")
        
        elif choice == "3":
            a, b = get_numbers()
            result = multiplication(a, b)
            print(f"Result: {a} * {b} = {result}")
        
        elif choice == "4":
            a, b = get_numbers()
            result = division(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {a} / {b} = {result:.2f}")
        
        elif choice == "5":
            a, b = get_numbers()
            result = modulus(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {a} % {b} = {result}")
        
        elif choice == "6":
            a, b = get_numbers()
            result = exponentiation(a, b)
            print(f"Result: {a} ** {b} = {result}")
        
        elif choice == "7":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a number from 1 to 7.")