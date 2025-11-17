'''Let's try a classic Computer Science project: simple calculator program! 🔢

Create a calculator.py program and define these five functions:

add(a, b) that adds two numbers a and b.
subtract(a, b) that subtracts two numbers a and b
multiply(a, b) that multiplies two numbers a and b.
divide(a, b) that divides two numbers a and b.
exp(a, b) that takes a to the exponent (or power) of b.
Make sure to return the result in each function definition.

Test your calculator by calling each function once to make sure that it works!'''

# Write code below 💖

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    return a / b

# Exponentiation
def exp(a, b):
    return a ** b

print(add(2, 3))
print(subtract(4, 2))
print(multiply(4, 3))
print(divide(9, 3))
print(exp(2, 3))

'''output:
5
2
12
3.0
8'''