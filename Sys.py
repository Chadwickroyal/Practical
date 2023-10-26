import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if len(sys.argv) < 4:
    print("Usage: Sys.py operation num1 num2")
else:
    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    print(result)
