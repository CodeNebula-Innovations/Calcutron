import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def square_root(x):
    if x < 0:
        return "Invalid input (negative number)"
    return math.sqrt(x)

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "sqrt"):
        if user_input != "sqrt":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else:
            num1 = float(input("Enter a number: "))

        if user_input == "add":
            print("Result: " + str(add(num1, num2)))
        elif user_input == "subtract":
            print("Result: " + str(subtract(num1, num2)))
        elif user_input == "multiply":
            print("Result: " + str(multiply(num1, num2)))
        elif user_input == "divide":
            print("Result: " + str(divide(num1, num2)))
        elif user_input == "sqrt":
            print("Result: " + str(square_root(num1)))
    else:
        print("Unknown input")